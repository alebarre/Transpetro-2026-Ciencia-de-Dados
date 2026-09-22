---
name: abrir-bateria
description: Cria a bateria diária de questões do dia (questoes.md + resolucao.md + aula.md) no mesmo padrão já estabelecido — 20 questões por bloco (10 iniciais + 10 extras), estilo Cesgranrio, com aula teórica correspondente. Use ao começar uma sessão de estudo do dia, ou quando o usuário pedir "bateria de hoje"/"bateria do dia X".
---

Ao ser invocada, esta regra monta a pasta do dia em `04-questoes/bateria-diaria/<data>/`, sempre com o mesmo conteúdo: `questoes.md`, `resolucao.md` e `aula.md`. Use `04-questoes/bateria-diaria/2026-09-21/` como referência de padrão (formato, tom, nível de dificuldade, tamanho) para tudo que for gerado.

## 1. Descobrir a data e o tema do dia

- Data: hoje, ou a data que o usuário indicar (formato `AAAA-MM-DD` para a pasta).
- Abra `02-plano/01-plano-geral.md` e localize a linha da tabela de cronograma cujo dia bate com essa data (coluna 1, formato "Seg 21/09"). As colunas seguintes trazem o tema do **Bloco 1 — Específicos** (ex.: "II.1 Probabilidade...") e do **Bloco 2 — Gerais** (Português ou Inglês, alternando por dia, às vezes ambos).
- Se a data não estiver na tabela (feriado marcado, dia fora do calendário, ou usuário pedindo algo fora do plano), pergunte ao usuário qual tema usar em vez de supor.
- Se a pasta `04-questoes/bateria-diaria/<data>/` já existir com `questoes.md` preenchido, avise o usuário e pergunte se é para sobrescrever antes de continuar.

## 2. Gerar `questoes.md`

Estrutura fixa, replicando o cabeçalho e a formatação de `2026-09-21/questoes.md`:

```
# Bateria do dia — <Dia da semana>, <DD/MM/AAAA> (Semana <N>)

Temas do dia (`02-plano/01-plano-geral.md`): **Bloco 1** — <tema específicos>. **Bloco 2** — <tema gerais>.

Responda tudo antes de olhar `resolucao.md`. Anote no `04-questoes/caderno-de-erros.md` toda questão errada ou chutada.

---

## Bloco 1 — <nome do bloco específicos>

**1.** ... até **20.**

---

## Bloco 2 — <nome do bloco gerais>

(se o bloco for de compreensão de texto, inclua um texto de contexto Transpetro/dutos/refino antes das primeiras ~5 questões, como no exemplo)

**1.** ... até **20.** (ou até a quantidade que o dia pedir — o padrão é 20)
```

Regras de conteúdo, herdadas do padrão já validado:

- **20 questões por bloco** (10 iniciais + 10 "extras", numeradas em sequência única de 1 a 20 — não reinicie a numeração dentro do bloco).
- 5 alternativas (A–E) por questão, estilo Cesgranrio: enunciados objetivos, uma alternativa claramente correta, distratores plausíveis (erro de cálculo comum, extrapolação do texto, confusão conceitual), nunca ambíguos.
- Contextualize com cenários de refinaria/logística de petróleo e derivados quando o tema permitir (matemática, estatística, banco de dados, ML aplicado etc.) — é a "marca" da bateria, como nas questões de tanques, dutos, turnos de refino já usadas.
- Nível de dificuldade e extensão do enunciado equivalentes aos exemplos de `2026-09-21/questoes.md` — nem trivial demais, nem de pós-graduação.
- Se o Bloco 2 do dia for compreensão de texto, escreva um texto novo (2 parágrafos, ~120-180 palavras, tema Transpetro/dutos/dados/petróleo) e baseie as primeiras questões de compreensão nele; as demais (gramática/estilo) não precisam do texto.

## 3. Gerar `resolucao.md`

Mesmo padrão de `2026-09-21/resolucao.md`: para cada questão, "**N. Resposta: X**" seguido de uma explicação objetiva (1–4 linhas) que:
- aplica a fórmula/regra ao caso da questão (não só repete a resposta);
- quando fizer sentido, explica por que as alternativas erradas mais tentadoras (pegadinhas) estão erradas — isso alimenta o caderno de erros depois.

## 4. Gerar `aula.md`

Mesmo padrão de `2026-09-21/aula.md`: uma aula teórica por bloco, cobrindo cada regra/conceito usado nas 20 questões daquele bloco (com referência a qual(is) número(s) de questão ilustram cada ponto), fechando com uma tabela-resumo quando o bloco for de fórmulas (matemática/estatística/ML) e com uma seção "Como usar esta aula" ao final, idêntica em espírito à existente.

## 5. Não gerar `resultado.json`

Esse arquivo só é criado no fechamento do dia (regra `/fechar-bateria`), depois que o usuário responde às questões. Não crie nem preencha aqui.

## 6. Resumo final

Diga ao usuário que a bateria do dia está pronta, quantas questões há em cada bloco, e lembre que ao final da sessão é para invocar `/fechar-bateria`.
