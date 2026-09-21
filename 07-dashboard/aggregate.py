#!/usr/bin/env python3
"""Gera 07-dashboard/dados.json a partir dos arquivos do plano de estudos.

Fontes lidas (somente leitura):
  - 03-checklist/checklist-edital.md      -> cobertura do edital (T/Q/R)
  - 04-questoes/bateria-diaria/*/resultado.json -> questoes resolvidas por dia
  - 06-simulados/registro-simulados.md    -> resultado dos simulados vs meta
  - 02-plano/01-plano-geral.md            -> rotulos de semana (periodo/tema)
  - 02-plano/02-registro-semanal.md       -> horas de estudo por semana (se preenchido)

Nao editar dados.json a mao: ele e sobrescrito toda vez que este script roda.
Uso: python3 07-dashboard/aggregate.py
"""
import json
import re
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DASH = ROOT / "07-dashboard"
HOJE = date.today()
INICIO = date(2026, 9, 21)   # segunda da semana 1
PROVA = date(2026, 11, 29)
TOTAL_SEMANAS = 10

BLOCO_ORDEM = ["PT", "EN", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]


def semana_de(d: date) -> int:
    if d < INICIO:
        return 0
    n = (d - INICIO).days // 7 + 1
    return min(n, TOTAL_SEMANAS)


def bloco_canonico(tema: str) -> str:
    m = re.match(r"^(PT|EN|[IVXLC]+)", tema.strip(), re.IGNORECASE)
    if not m:
        return tema
    tok = m.group(1)
    return tok if tok in ("PT", "EN") else tok.upper()


# ---------------------------------------------------------------------------
# 1. Checklist do edital -> cobertura T/Q/R por bloco
# ---------------------------------------------------------------------------
def parse_checklist():
    path = ROOT / "03-checklist/checklist-edital.md"
    text = path.read_text(encoding="utf-8")
    header_re = re.compile(r"^### (?:([IVXLC]+) – )?(.+?) \(")
    item_re = re.compile(r"^- \[([ xX])\] T \[([ xX])\] Q \[([ xX])\] R ·")

    blocos = {}
    atual = None
    for line in text.splitlines():
        m = header_re.match(line)
        if m:
            roman, nome = m.group(1), m.group(2).strip()
            if "Língua Portuguesa" in nome:
                codigo = "PT"
            elif "Língua Inglesa" in nome:
                codigo = "EN"
            elif roman:
                codigo = roman
            else:
                codigo = None
            if codigo:
                atual = codigo
                blocos[codigo] = {"bloco": codigo, "nome": nome, "itens": 0, "T": 0, "Q": 0, "R": 0}
            else:
                atual = None
            continue
        m = item_re.match(line)
        if m and atual:
            t, q, r = (g.strip().lower() == "x" for g in m.groups())
            b = blocos[atual]
            b["itens"] += 1
            b["T"] += int(t)
            b["Q"] += int(q)
            b["R"] += int(r)
    return blocos


def pct(n, d):
    return round(100.0 * n / d, 1) if d else 0.0


def resumo_cobertura(blocos):
    ordem = [c for c in BLOCO_ORDEM if c in blocos]
    por_bloco = []
    tot_itens = tot_t = tot_q = tot_r = 0
    for c in ordem:
        b = blocos[c]
        por_bloco.append({
            "bloco": c, "nome": b["nome"], "itens": b["itens"],
            "T": pct(b["T"], b["itens"]), "Q": pct(b["Q"], b["itens"]), "R": pct(b["R"], b["itens"]),
        })
        tot_itens += b["itens"]; tot_t += b["T"]; tot_q += b["Q"]; tot_r += b["R"]
    geral = {"itens_total": tot_itens, "T": pct(tot_t, tot_itens), "Q": pct(tot_q, tot_itens), "R": pct(tot_r, tot_itens)}
    return geral, por_bloco


# ---------------------------------------------------------------------------
# 2. Baterias diarias -> questoes resolvidas, acertos, streak
# ---------------------------------------------------------------------------
def parse_baterias():
    pasta = ROOT / "04-questoes/bateria-diaria"
    dias = []
    if pasta.exists():
        for sub in sorted(pasta.iterdir()):
            f = sub / "resultado.json"
            if f.exists():
                try:
                    dias.append(json.loads(f.read_text(encoding="utf-8")))
                except (json.JSONDecodeError, OSError):
                    continue
    dias.sort(key=lambda d: d["date"])
    return dias


def resumo_questoes(dias, semana_labels):
    por_dia = []
    por_semana = {n: {"semana": n, "periodo": semana_labels.get(n, {}).get("periodo", ""),
                       "tema": semana_labels.get(n, {}).get("tema", ""),
                       "total": 0, "acertos": 0} for n in range(1, TOTAL_SEMANAS + 1)}
    por_mes = {}
    por_bloco = {}
    total_geral = acertos_geral = 0

    for dia in dias:
        d = date.fromisoformat(dia["date"])
        tot_dia = sum(b["total"] for b in dia["blocks"])
        ace_dia = sum(b["acertos"] for b in dia["blocks"])
        blocos_dia = [{"label": b.get("label", ""), "tema": b.get("tema", []), "topic": b.get("topic", ""),
                       "total": b["total"], "acertos": b["acertos"], "pct": pct(b["acertos"], b["total"])}
                      for b in dia["blocks"]]
        por_dia.append({"date": dia["date"], "type": dia.get("type", "bateria"),
                         "total": tot_dia, "acertos": ace_dia, "pct": pct(ace_dia, tot_dia),
                         "blocks": blocos_dia})
        total_geral += tot_dia
        acertos_geral += ace_dia

        sem = semana_de(d)
        if sem in por_semana:
            por_semana[sem]["total"] += tot_dia
            por_semana[sem]["acertos"] += ace_dia

        mes = dia["date"][:7]
        por_mes.setdefault(mes, {"mes": mes, "total": 0, "acertos": 0})
        por_mes[mes]["total"] += tot_dia
        por_mes[mes]["acertos"] += ace_dia

        for b in dia["blocks"]:
            for tema in b.get("tema", []):
                cod = bloco_canonico(tema)
                bb = por_bloco.setdefault(cod, {"bloco": cod, "total": 0, "acertos": 0})
                bb["total"] += b["total"]
                bb["acertos"] += b["acertos"]

    for s in por_semana.values():
        s["pct"] = pct(s["acertos"], s["total"]) if s["total"] else None
    for m in por_mes.values():
        m["pct"] = pct(m["acertos"], m["total"]) if m["total"] else None
    ranking_bloco = []
    for cod in BLOCO_ORDEM:
        if cod in por_bloco and por_bloco[cod]["total"] >= 5:
            b = por_bloco[cod]
            ranking_bloco.append({"bloco": cod, "total": b["total"], "acertos": b["acertos"], "pct": pct(b["acertos"], b["total"])})
    ranking_bloco.sort(key=lambda b: b["pct"])

    return {
        "total_resolvidas": total_geral,
        "total_acertos": acertos_geral,
        "pct_acerto_geral": pct(acertos_geral, total_geral) if total_geral else None,
        "por_dia": por_dia,
        "por_semana": list(por_semana.values()),
        "por_mes": sorted(por_mes.values(), key=lambda m: m["mes"]),
        "por_bloco_edital": ranking_bloco,
    }


def calc_streak(dias):
    datas = sorted({date.fromisoformat(d["date"]) for d in dias})
    if not datas:
        return {"atual": 0, "recorde": 0}
    recorde = atual_run = 1
    melhor_final = datas[0]
    for i in range(1, len(datas)):
        if (datas[i] - datas[i - 1]).days == 1:
            atual_run += 1
        else:
            atual_run = 1
        recorde = max(recorde, atual_run)
    # streak "atual": roda terminando na ultima data, valida so se ainda nao quebrou
    fim = datas[-1]
    run = 1
    i = len(datas) - 1
    while i > 0 and (datas[i] - datas[i - 1]).days == 1:
        run += 1
        i -= 1
    atual = run if (HOJE - fim).days <= 1 else 0
    return {"atual": atual, "recorde": recorde}


# ---------------------------------------------------------------------------
# 3. Semanas do plano -> rotulos (periodo/tema) para a visao semanal
# ---------------------------------------------------------------------------
def parse_semanas_plano():
    path = ROOT / "02-plano/01-plano-geral.md"
    text = path.read_text(encoding="utf-8")
    rex = re.compile(r"^### Semana (\d+) · (.+?) · (.+?)\s*$")
    labels = {}
    for line in text.splitlines():
        m = rex.match(line)
        if m:
            n, periodo, tema = m.groups()
            labels[int(n)] = {"periodo": periodo.strip(), "tema": tema.strip()}
    return labels


# ---------------------------------------------------------------------------
# 4. Horas de estudo (registro semanal, preenchimento manual opcional)
# ---------------------------------------------------------------------------
def parse_horas_semanais():
    path = ROOT / "02-plano/02-registro-semanal.md"
    text = path.read_text(encoding="utf-8")
    horas = {}
    for line in text.splitlines():
        if not line.startswith("|"):
            continue
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) < 3 or not cols[0].isdigit():
            continue
        semana = int(cols[0])
        h = cols[2]
        m = re.search(r"(\d+(?:[.,]\d+)?)", h)
        horas[semana] = float(m.group(1).replace(",", ".")) if m else None
    return horas


# ---------------------------------------------------------------------------
# 5. Simulados: registro vs meta
# ---------------------------------------------------------------------------
def parse_simulados():
    path = ROOT / "06-simulados/registro-simulados.md"
    text = path.read_text(encoding="utf-8")

    metas = {}
    for m in re.finditer(r"Simulado (\d+) ≥ (\d+)/50 e ≥ (\d+)/20", text):
        n, esp, ger = m.groups()
        metas[int(n)] = {"especificos": int(esp), "gerais": int(ger)}

    datas = {}
    for line in text.splitlines():
        if line.startswith("|") and "Sáb" in line:
            cols = [c.strip() for c in line.strip("|").split("|")]
            if cols[0].isdigit():
                dm = re.search(r"(\d{2})/(\d{2})", cols[1])
                if dm:
                    dd, mm = dm.groups()
                    datas[int(cols[0])] = f"2026-{mm}-{dd}"

    registros = {}
    in_registro = False
    for line in text.splitlines():
        if line.startswith("## Registro"):
            in_registro = True
            continue
        if in_registro and line.startswith("## "):
            break
        if in_registro and line.startswith("|"):
            cols = [c.strip() for c in line.strip("|").split("|")]
            if cols and cols[0].isdigit():
                n = int(cols[0])
                especificos = cols[2] if len(cols) > 2 else ""
                portugues = cols[3] if len(cols) > 3 else ""
                ingles = cols[4] if len(cols) > 4 else ""
                registros[n] = {
                    "especificos": int(especificos) if especificos.isdigit() else None,
                    "portugues": int(portugues) if portugues.isdigit() else None,
                    "ingles": int(ingles) if ingles.isdigit() else None,
                }

    todos = sorted(set(metas) | set(datas) | set(registros))
    simulados = []
    for n in todos:
        reg = registros.get(n, {})
        meta = metas.get(n, {})
        feito = reg.get("especificos") is not None
        simulados.append({
            "numero": n,
            "data": datas.get(n),
            "meta_especificos": meta.get("especificos"),
            "meta_gerais": meta.get("gerais"),
            "especificos": reg.get("especificos"),
            "portugues": reg.get("portugues"),
            "ingles": reg.get("ingles"),
            "status": "concluido" if feito else "pendente",
        })
    return simulados


def risco_eliminacao(simulados):
    feitos = [s for s in simulados if s["status"] == "concluido"]
    if not feitos:
        return {"zero_pt": False, "zero_en": False, "abaixo_corte_especificos": False, "abaixo_corte_gerais": False}
    ultimo = feitos[-1]
    gerais = (ultimo["portugues"] or 0) + (ultimo["ingles"] or 0)
    return {
        "zero_pt": ultimo["portugues"] == 0,
        "zero_en": ultimo["ingles"] == 0,
        "abaixo_corte_especificos": (ultimo["especificos"] or 0) < 25,
        "abaixo_corte_gerais": gerais < 10,
    }


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    blocos = parse_checklist()
    geral, por_bloco = resumo_cobertura(blocos)

    anterior = {}
    dados_path = DASH / "dados.json"
    if dados_path.exists():
        try:
            anterior = json.loads(dados_path.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            anterior = {}
    historico = anterior.get("cobertura", {}).get("historico", [])
    historico = [h for h in historico if h["date"] != HOJE.isoformat()]
    historico.append({"date": HOJE.isoformat(), "T": geral["T"], "Q": geral["Q"], "R": geral["R"]})
    historico.sort(key=lambda h: h["date"])

    semana_labels = parse_semanas_plano()
    dias = parse_baterias()
    questoes = resumo_questoes(dias, semana_labels)
    streak = calc_streak(dias)
    horas = parse_horas_semanais()
    for s in questoes["por_semana"]:
        s["horas_feitas"] = horas.get(s["semana"])

    simulados = parse_simulados()

    dados = {
        "meta": {
            "gerado_em": HOJE.isoformat(),
            "hoje": HOJE.isoformat(),
            "prova": PROVA.isoformat(),
            "dias_para_prova": (PROVA - HOJE).days,
            "semana_atual": semana_de(HOJE),
            "total_semanas": TOTAL_SEMANAS,
        },
        "cobertura": {"geral": geral, "por_bloco": por_bloco, "historico": historico},
        "questoes": questoes,
        "streak": streak,
        "simulados": simulados,
        "risco_eliminacao": risco_eliminacao(simulados),
    }

    dados_path.write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"OK: {dados_path} atualizado ({questoes['total_resolvidas']} questoes, "
          f"{geral['T']}% cobertura T, {(PROVA - HOJE).days} dias para a prova)")


if __name__ == "__main__":
    main()
