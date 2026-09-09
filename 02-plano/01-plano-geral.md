# Plano Geral – 12 semanas (07/09 → 29/11/2026)

## 1. Diagnóstico honesto do edital

O programa da ênfase 8 tem **12 blocos** e é largo demais para ser "estudado inteiro" em 180h. Ele foi escrito como lista de tudo que um cientista de dados pode encontrar, não como lista do que a Cesgranrio vai perguntar. A banca, historicamente (BNDES 2024 Ciência de Dados, BB 2023 TI, Petrobras 2024/2025 TI), concentra as questões em:

1. conceitos literais e comparações ("qual a diferença entre X e Y", "qual afirmativa é correta sobre Z");
2. leitura de código curto em Python/Pandas/SQL, com a pergunta "qual a saída?";
3. contas pequenas de estatística e de métricas (matriz de confusão, média/variância, Bayes, IC);
4. interpretação de texto em Português e Inglês.

Ela raramente cobra dedução matemática longa, e quase nunca cobra o que exige contexto de projeto real.

## 2. Distribuição estimada das 50 questões por bloco

Estimativa própria feita a partir do padrão das provas Cesgranrio de Ciência de Dados/TI (não é dado oficial; o edital não define pesos por bloco). Use para priorizar, não como certeza.

| Bloco | Questões estimadas | Prioridade | Horas-alvo (de ~125h de Específicos) |
|---|---|---|---|
| VII – Classes de Modelos | 9 | 🔴 Alta | 24h |
| II – Probabilidade e Estatística | 8 | 🔴 Alta | 22h |
| IX – Programação e Ferramentas (Python, SQL, Power BI) | 8 | 🔴 Alta | 22h |
| VI – Modelagem (métricas, validação, regularização) | 6 | 🔴 Alta | 14h |
| V – Qualidade e Preparação de Dados | 4 | 🟡 Média | 9h |
| III – Dados e Bases de Dados | 4 | 🟡 Média | 9h |
| VIII – NLP | 3 | 🟡 Média | 7h |
| I – Matemática | 3 | 🟡 Média | 6h |
| X – Visualização e Storytelling | 2 | 🟢 Baixa | 4h |
| XI + XII – Governança de Dados e de IA | 2 | 🟢 Baixa | 4h |
| IV – Gestão de Projetos (CRISP-DM etc.) | 1 | 🟢 Baixa | 2h |
| Simulados e revisão transversal | – | – | ~15h (dentro dos sábados) |

Os 4 blocos vermelhos somam ~31 das 50 questões. Dominá-los já coloca você acima do corte de eliminação (25) e perto da meta.

**Gerais (≈55h):** Português 30h, Inglês 25h. Não subestime: são 20 pontos com conteúdo finito e previsível, e valem para a classificação final.

## 3. Metas numéricas

| Momento | Específicos | Português | Inglês |
|---|---|---|---|
| Fim da semana 7 (25/10) – questões avulsas por tema | ≥ 60% | ≥ 65% | ≥ 65% |
| Simulado 1 (31/10) | ≥ 30/50 | ≥ 6/10 | ≥ 6/10 |
| Simulado 3 (14/11) | ≥ 35/50 | ≥ 7/10 | ≥ 7/10 |
| Dia da prova (meta) | 36+/50 | 8/10 | 8/10 |

A nota de corte real da ênfase não é conhecida (primeira vez que a Transpetro abre Ciência de Dados neste formato). 36/50 + 16/20 = 52/70 é uma meta competitiva para 16 posições.

## 4. As três fases

### Fase 1 – Cobertura dirigida (semanas 1–7: 07/09 a 25/10) · 112h

- Cada semana cobre **3 trilhas em paralelo** para não saturar: **A** Estatística/Matemática, **B** Machine Learning, **C** Programação e Dados. A sexta-feira pega um bloco secundário (**D**).
- Método por sessão de 50 min: **10 questões Cesgranrio do tema → ler teoria só do que errou/não sabia (20–25 min) → mais 5–10 questões → anotar no caderno de erros.** Se não houver questões suficientes do tema, use teoria enxuta (resumo/aula curta) e depois questões de bancas parecidas (FGV, Cebraspe) só para fixar.
- Português e Inglês: 2 sessões/semana cada, sempre com questões Cesgranrio (a banca repete o estilo há anos).

### Fase 2 – Consolidação e simulados (semanas 8–10: 26/10 a 15/11) · 48h

- Segunda a sexta: revisão por bloco em ordem de prioridade, com baterias de 20 questões e leitura do caderno de erros.
- Sábados: **simulado completo cronometrado (4h30)** + correção com análise de erro (2h). Simulados 1, 2 e 3.
- Aqui você fecha os blocos verdes (governança, gestão de projetos, visualização), que são "decoreba" de rendimento rápido.

### Fase 3 – Reta final (semanas 11–12: 16/11 a 29/11) · ~20h

- Semana 11: simulado 4 no sábado 21/11; dias úteis só caderno de erros + formulário + questões dos blocos vermelhos.
- Semana 12: segunda a quinta em revisão leve (formulário, caderno de erros, 20 questões/dia). Sexta 27/11: pegar cartão de confirmação, checar local. Sábado 28/11: **descanso**. Domingo 29/11: prova.

## 5. Por que este plano difere da sugestão da outra IA

O plano anterior era razoável na filosofia (estudo reverso, sábado de volume, descanso no domingo) e foi mantido nisso. As diferenças:

1. **Foi feito sobre o edital real**, não sobre um "mapa de calor" genérico. O edital cobra coisas que o plano anterior não mencionava e que rendem questões fáceis: séries temporais, regressão (ANOVA, hipóteses clássicas), Power BI, governança de IA, NLP, sistemas de recomendação, normas vetoriais e SVD.
2. **Considera a regra de habilitação** (ranking só por Específicos até 2× vagas+CR). Isso justifica 70/30 e não 50/50.
3. **Tem datas**, feriados (07/09, 12/10, 02/11, 15/11, 20/11) e simulados marcados. O feriado vira um "sábado extra" de 4h se você quiser antecipar tópico atrasado.
4. **Tem um checklist do edital linha a linha** para que nada fique invisível.

## 6. Regras de execução

- **Sem aulas longas.** Vídeo só até 20 min e só para o tópico que você errou. Aula de 2h não cabe numa rotina de 2h/dia.
- **Código se lê, não se escreve.** Para Python/SQL, abra o Google Colab, cole o código da questão, rode, mude uma linha, veja o que acontece. 15 min disso valem mais que 1h de curso.
- **Caderno de erros é obrigatório** (modelo em `04-questoes/caderno-de-erros.md`). Toda questão errada ou acertada no chute vai para lá com a "pegadinha" em uma linha.
- **Revisão espaçada:** os primeiros 10 min de toda sessão são para reler o caderno de erros dos últimos 7 dias.
- **Um tema atrasado não empurra a semana.** Se sobrou, entra no sábado (bloco 3) ou no feriado; se não coube, marca no checklist como "pendente" e segue o cronograma.
- **Celular em outro cômodo** durante os blocos de 50 min.
