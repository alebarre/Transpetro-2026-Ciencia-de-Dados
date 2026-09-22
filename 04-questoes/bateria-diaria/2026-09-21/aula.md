# Aula — Segunda, 21/09/2026 (Semana 1)

Conteúdo teórico de apoio às questões de `questoes.md`. Leia antes ou depois de responder — o objetivo é fixar a teoria por trás de cada tipo de questão cobrado hoje.

---

## Bloco 1 — Probabilidade (II.1): definições, axiomas, condicional

### 1. Definição clássica de probabilidade

Para um espaço amostral finito com resultados igualmente prováveis:

```
P(A) = (nº de casos favoráveis a A) / (nº de casos possíveis)
```

Vale sempre **0 ≤ P(A) ≤ 1**. É a base das questões 1 e 11 (lote de válvulas, tanques com vazamento).

### 2. Axiomas de probabilidade (Kolmogorov)

1. **Não negatividade**: P(A) ≥ 0 para qualquer evento A.
2. **Normalização**: P(S) = 1, em que S é o espaço amostral (evento certo). P(∅) = 0 (evento impossível).
3. **Aditividade**: se A e B são mutuamente exclusivos (não podem ocorrer juntos, A∩B = ∅), então P(A∪B) = P(A) + P(B).

Consequência direta: **complementaridade**. Se Aᶜ é o complementar de A,

```
P(A) + P(Aᶜ) = 1  →  P(Aᶜ) = 1 − P(A)
```

Qualquer alternativa com P(A) < 0, P(A) > 1, ou que quebre esses três axiomas está errada por definição — é o tipo de "pegadinha" das questões 7 e 17.

### 3. Regra geral da união (eventos não necessariamente exclusivos)

Quando A e B **podem** ocorrer juntos, somar P(A) + P(B) conta a interseção duas vezes. É preciso subtrair:

```
P(A∪B) = P(A) + P(B) − P(A∩B)
```

Se A e B forem mutuamente exclusivos, P(A∩B) = 0 e a fórmula "cai" na aditividade simples (questões 3 e 13). Quando há interseção não nula, esquecer de subtraí-la é o erro mais comum em prova (questões 4 e 14).

### 4. Probabilidade condicional

Mede a probabilidade de um evento **dado que outro já ocorreu**, ou seja, o espaço amostral é restringido ao evento condicionante:

```
P(A|B) = P(A∩B) / P(B),   com P(B) > 0
```

Isolando a interseção: **P(A∩B) = P(A|B) · P(B)** — é a forma cobrada na questão 15.

Atenção à ordem dos termos: em P(B|A), a condição é A (o que já aconteceu); a pergunta é sobre B. Trocar a ordem é o erro clássico de interpretação (questão 9).

**Duas formas de aparecer em prova:**

- **Explícita**, com dados de uma tabela de dupla entrada (ex.: turnos × incidentes). Nesses casos, o "total geral" costuma ser informação de contexto — o espaço amostral já fica restrito ao grupo mencionado na condição (questões 6 e 16).
- **Implícita**, por restrição do espaço amostral em enunciados de sorteio ("sabendo que o número é par...", "sabendo que é múltiplo de 3..."). Resolve-se listando diretamente os elementos do subconjunto condicionante e contando quantos satisfazem a segunda condição (questões 10 e 20), sem precisar escrever a fórmula.

### 5. Independência de eventos

A e B são **independentes** quando a ocorrência de um não muda a probabilidade do outro:

```
P(A∩B) = P(A) · P(B)
P(A|B) = P(A)   e   P(B|A) = P(B)
```

Não confundir independência com mutuamente exclusivos — são conceitos diferentes: eventos mutuamente exclusivos têm P(A∩B) = 0 (se um ocorre, o outro não pode ocorrer), enquanto eventos independentes têm P(A∩B) = P(A)·P(B), que só é zero se P(A) = 0 ou P(B) = 0. Dois eventos com probabilidade positiva não podem ser simultaneamente exclusivos e independentes (questões 8, 18 e 19).

### Resumo rápido

| Situação | Fórmula |
|---|---|
| Casos igualmente prováveis | P(A) = favoráveis / possíveis |
| Complementar | P(Aᶜ) = 1 − P(A) |
| União, mutuamente exclusivos | P(A∪B) = P(A) + P(B) |
| União, caso geral | P(A∪B) = P(A) + P(B) − P(A∩B) |
| Condicional | P(A\|B) = P(A∩B) / P(B) |
| Independência | P(A∩B) = P(A) · P(B) |

---

## Bloco 2 — Português: compreensão de texto + estilo Cesgranrio

### 1. Compreensão de texto

- **Tipologia textual**: identifique se o texto narra (sucessão de fatos), descreve (características), disserta/expõe (apresenta e explica ideias), instrui (dá ordens/procedimentos) ou tem função poética. O texto de hoje é **dissertativo-expositivo**: apresenta um tema (transporte dutoviário) e o explica com dados e relações de causa/efeito (questão 9).
- **Ideia central × detalhes**: a ideia central costuma aparecer resumida na conclusão do texto ou no período que amarra os parágrafos ("é esse equilíbrio [...] que sustenta a confiabilidade"). Cuidado com alternativas que generalizam demais ("totalmente", "completa", "dispensa") — normalmente extrapolam o que o texto realmente afirma (questões 1, 3 e 10).
- **Retomada anafórica**: expressões como "esse equilíbrio", "essa infraestrutura" retomam uma ideia dita antes, não uma palavra isolada. Releia a frase anterior para identificar exatamente o que está sendo retomado (questão 2).
- **Substituição lexical (sinônimos em contexto)**: a troca de uma palavra só é válida se preservar o sentido *naquele contexto específico* — não basta ser sinônimo em dicionário (questões 4 e 14).
- **Relações lógico-discursivas (conectivos)**: cada conectivo marca um tipo de relação entre as ideias:
  - Adição: e, também, além disso
  - Contraste/oposição (adversativa): mas, porém, entretanto, contudo, todavia, no entanto
  - Causa: porque, já que, uma vez que
  - Conclusão: portanto, logo, assim, por conseguinte
  - Explicação: pois, porquanto
  
  "Entretanto" e "porém" são intercambiáveis como adversativas (questões 5 e 15).

### 2. Concordância verbal

Casos clássicos de prova:

- **Verbos impessoais** (não têm sujeito, ficam sempre na 3ª pessoa do singular): "haver" no sentido de existir ("Deve haver mais avanços"); "fazer" indicando tempo decorrido ("Faz dois anos que...").
- **Voz passiva sintética** (verbo + "se" = pronome apassivador): o verbo concorda com o sujeito paciente, que deve ser identificável. "Alugam-se equipamentos" (sujeito: equipamentos, plural → verbo plural). Se o sujeito for indeterminado (verbo intransitivo ou transitivo indireto + se), o verbo fica invariável na 3ª do singular: "Precisa-se de técnicos".
- **Sujeito de "existir"**: concorda normalmente com o sujeito, ao contrário de "haver" — "Existem diversos sistemas" (não "existe").

(questão 6)

### 3. Crase

Crase = fusão da preposição "a" (exigida por algum termo da oração) com o artigo feminino "a(s)".

**Regra prática**: só há crase antes de palavra feminina que admita o artigo "a". Por isso:

- **Não há crase** antes de pronomes indefinidos, demonstrativos ou pessoais que não admitem artigo: "a diversos", "a possíveis", "a qualquer", "a ela".
- **Não há crase** na locução "a partir de" — é fixa e nunca leva acento grave, mesmo antes de data.
- **Há crase** quando o verbo/termo regente exige "a" e o substantivo seguinte é feminino e determinado: "entregue à imprensa", "atenta à situação" (quando "situação" vier determinada por artigo).

(questão 7)

### 4. Pontuação — expressões intercaladas

Expressões explicativas, apositivas ou concessivas intercaladas no meio da oração (como "mesmo pequenos") devem vir **isoladas por vírgulas dos dois lados**, nunca de um lado só, e nunca separando sujeito/verbo ou verbo/complemento sem justificativa sintática:

```
"Os vazamentos, mesmo pequenos, podem gerar impactos ambientais."
```

(questão 8)

### 5. Regência verbal

Cada verbo exige uma preposição específica (ou nenhuma) para introduzir seu complemento — é a regência. Os mais cobrados em prova:

| Verbo | Regência | Exemplo |
|---|---|---|
| Chegar / ir | a (não "em"/"no") | chegar **ao** local |
| Obedecer / desobedecer | a | obedece **às** normas |
| Preferir | a (nunca "do que") | prefere dutos **a** caminhões |
| Visar (= aspirar a) | a | visa **ao** cargo |
| Assistir (= presenciar) | a | assistiu **ao** treinamento |
| Aspirar (= desejar) | a | aspira **ao** cargo |

(questão 11)

### 6. Colocação pronominal

Três posições possíveis do pronome átono: **próclise** (antes do verbo), **ênclise** (depois do verbo) e **mesóclise** (no meio do verbo, só em futuro do presente/pretérito, uso raro e formal).

**Palavras atrativas** que obrigam a próclise: advérbios de negação ("não"), pronomes indefinidos, relativos, conjunções subordinativas, e início de frase com essas palavras. Por isso "Não se identificou" está correto, mas "Não identificou-se" fere a regra. Também não se inicia oração com pronome oblíquo átono na norma-padrão ("Se identificou..." está errado).

(questão 12)

### 7. Porque / por que / porquê / por quê

| Forma | Uso | Exemplo |
|---|---|---|
| **por que** (separado, sem acento) | perguntas diretas/indiretas; equivale a "pelo qual/pela qual" | "Não sabemos **por que** o vazamento ocorreu." |
| **porque** (junto, sem acento) | resposta, explicação, causa | "O vazamento ocorreu **porque** a válvula falhou." |
| **por quê** (separado, com acento) | final de frase, geralmente interrogativa | "Ele não relatou o incidente, **por quê**?" |
| **o porquê** (junto, com acento, substantivo) | precedido de artigo/determinante | "Ninguém sabe **o porquê** da falha." |

(questão 13)

### 8. Ambiguidade

Ocorre quando um pronome, ou a ordem das palavras, permite mais de uma interpretação. Pronomes como "ele/ela/seu/sua" referindo-se a mais de um substantivo anterior são a causa mais comum: "Maria avisou Ana que ela seria transferida" — "ela" pode ser Maria ou Ana. Corrige-se explicitando o referente ("que a própria Ana seria transferida" ou "que Maria seria transferida").

(questão 16)

### 9. Vozes verbais

- **Voz ativa**: sujeito pratica a ação. "Os técnicos instalaram os sensores."
- **Voz passiva analítica**: sujeito da ativa vira **agente da passiva** (introduzido por "por"); objeto direto da ativa vira **sujeito paciente**. "Os sensores foram instalados **pelos** técnicos."
- **Voz passiva sintética**: verbo + "se" (pronome apassivador), sem agente expresso. "Instalaram-se os sensores."

Erro comum de prova: inverter os papéis (fazer o agente virar paciente) ou usar "por" com sentido trocado.

(questão 17)

### 10. Onde / aonde

- **Onde**: ideia de permanência, lugar estático — usado com verbos como "ficar", "estar", "morar". "A refinaria onde os sensores foram instalados fica no litoral."
- **Aonde**: ideia de movimento, direção, destino — usado com verbos como "ir", "chegar". "Aonde ele foi ontem?"

Teste rápido: se dá para responder com "para lá", use "aonde"; se dá para responder só com "lá", use "onde".

(questão 18)

---

## Como usar esta aula

1. Leia a teoria de um bloco.
2. Refaça as questões desse bloco em `questoes.md` sem consultar `resolucao.md`.
3. Confira o gabarito e registre erros/chutes em `04-questoes/caderno-de-erros.md`.
