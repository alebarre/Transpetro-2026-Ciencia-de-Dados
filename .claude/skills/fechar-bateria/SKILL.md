---
name: fechar-bateria
description: Fecha a bateria diária de questões — pergunta questões erradas por bloco (e quais números) e horas estudadas, depois atualiza resultado.json, caderno-de-erros.md e o registro semanal. Use ao final de cada sessão de estudo do dia.
---

Ao ser invocada, esta regra fecha o dia de estudo. Siga os passos abaixo, nesta ordem.

## 1. Descobrir a data e a pasta do dia

- Use a data de hoje (ou a data que o usuário indicar) para localizar `04-questoes/bateria-diaria/<data>/`.
- Leia `questoes.md` dessa pasta para saber quantos blocos existem hoje, o total de questões por bloco e os temas (ex.: "Probabilidade (II.1)", "Português").
- Leia `resolucao.md` (e `aula.md`, se existir) da mesma pasta — serão a fonte de "Pegadinha" e "Regra" para o caderno de erros.

## 2. Perguntar os indicadores ao usuário

Pergunte, em uma única mensagem, objetivamente:

1. Quantas questões erradas em cada bloco do dia (ex.: Probabilidade/Específicos, Português, Inglês — conforme o que existir na bateria de hoje).
2. **Quais números** de questão foram errados ou acertados no chute em cada bloco (necessário para preencher o caderno de erros linha a linha — sem isso, não adivinhe).
3. Quantas horas de estudo foram feitas hoje.

Não prossiga sem os números das questões erradas — a contagem sozinha não é suficiente para o caderno de erros.

## 3. Atualizar `resultado.json` da pasta do dia

Crie ou atualize `04-questoes/bateria-diaria/<data>/resultado.json` seguindo exatamente este esquema (é o que `07-dashboard/aggregate.py` espera):

```json
{
  "date": "AAAA-MM-DD",
  "type": "bateria",
  "blocks": [
    {
      "label": "<nome do bloco, ex.: Probabilidade (II.1)>",
      "tema": ["<código do edital: II, PT, EN, VII, ...>"],
      "topic": "<assunto do dia, como no cabeçalho de questoes.md>",
      "total": <nº de questões do bloco>,
      "acertos": <total - erradas>
    }
  ]
}
```

Um objeto em `blocks` por bloco do dia.

## 4. Atualizar `04-questoes/caderno-de-erros.md`

Para cada questão errada (ou acertada no chute) informada pelo usuário:

- Abra a questão correspondente em `questoes.md` e sua explicação em `resolucao.md`.
- Adicione **uma linha** na tabela da seção correta (Estatística e Matemática, Português, etc.):
  - **Data**: a data de hoje.
  - **Fonte**: `Bateria diária <data>, questão nº <n>`.
  - **Tema**: o assunto específico da questão (ex.: "Probabilidade condicional", "Regência verbal").
  - **Pegadinha**: em uma frase, o que induziu ao erro (baseie-se no enunciado + na explicação da resolução).
  - **Regra**: o que lembrar da próxima vez (baseie-se na regra teórica em `resolucao.md`/`aula.md`).
- Não invente pegadinha/regra genérica — extraia da questão e da resolução reais.

## 5. Atualizar `02-plano/02-registro-semanal.md`

- Identifique a semana corrente pela tabela (coluna "Período").
- **Horas feitas**: some as horas informadas hoje ao que já estiver na célula da semana (se vazia, apenas insira o valor de hoje).
- **Questões feitas**: some o total de questões do dia (soma de todos os blocos) ao que já estiver na célula.
- **% acerto Específicos / % acerto PT / % acerto EN**: recalcule a partir do acumulado da semana (não apenas do dia), no formato `NN% (acertos/total)`, atualizando a coluna correspondente a cada bloco que teve questões hoje. Se a semana já tinha um valor, some os acertos e totais antes de recalcular a porcentagem — não sobrescreva substituindo pelo valor do dia isolado.

## 6. Atualizar `03-checklist/checklist-edital.md` (cobertura do edital)

Sem este passo, a aba "Edital" do dashboard fica zerada mesmo com baterias registradas — `aggregate.py` lê cobertura só daqui, não de `questoes.md`/`resultado.json`.

- Releia o cabeçalho de `questoes.md` de hoje para saber exatamente qual(is) item(ns) numerado(s) do edital foram tratados (ex.: "II.1 Probabilidade: definições, axiomas, condicional" → item 1 da seção II; "PT: compreensão de texto + estilo Cesgranrio" pode tocar vários itens de Língua Portuguesa se a bateria trouxe questões de gramática além de compreensão — confira `aula.md`/`resolucao.md` de hoje para ver quais regras específicas foram explicadas).
- Para cada item do edital efetivamente coberto hoje, marque `[x]` em:
  - **T** (teoria vista) — se `aula.md` (ou equivalente) explicou a regra/conceito desse item hoje.
  - **Q** (≥ 10 questões) — só se esse item específico (não o bloco inteiro) acumulou 10 ou mais questões praticadas, somando hoje com dias anteriores. Um bloco com 20 questões no total mas espalhadas em 8 subtemas diferentes não dá Q a nenhum subtema isoladamente — conte por item, não por bloco.
  - **R** (revisado) — só na Fase 2 do plano (revisão), não em dias normais de bateria.
- Não desmarque um `[x]` já existente.

## 7. Atualizar o dashboard

Depois de salvar `resultado.json`, o caderno de erros e o registro semanal, rode:

```
python3 07-dashboard/aggregate.py
```

Isso regenera `07-dashboard/dados.json` a partir dos arquivos atualizados. Nunca edite `dados.json` manualmente. Confira a saída do comando (ele imprime um resumo com nº de questões e dias até a prova) para garantir que rodou sem erro antes de seguir.

## 8. Republicar o dashboard (Artifact)

O `dados.json` local só é o que alimenta o link publicado depois de republicado. Leia `07-dashboard/LINK.md` para pegar a URL atual, então:

1. Se este é o início da conversa (artifact ainda não lido nesta sessão), leia o artifact primeiro com `Artifact` `action: "read"` e a URL de `LINK.md`.
2. Publique novamente com `Artifact` `action: "publish"`, `url` = a mesma URL de `LINK.md`, `file_path` = `07-dashboard/dashboard.html`, `files` = `{"dados.json": "07-dashboard/dados.json"}`. Como `dados.json` é gerado por script e nunca editado à mão, é esperado publicar sem tê-lo lido antes — nesse caso, inclua `overwrite_unread: ["dados.json"]`.
3. Atualize a linha "Última atualização" em `07-dashboard/LINK.md` com a data de hoje e um resumo curto do resultado (ex.: "Probabilidade 15/20, Português 15/18, 2h de estudo").

## 9. Resumo final

Depois de aplicar as edições e rodar o `aggregate.py`, responda ao usuário com um resumo curto: o que foi atualizado em cada arquivo (incluindo que o dashboard foi regenerado), sem repetir o conteúdo das tabelas.
