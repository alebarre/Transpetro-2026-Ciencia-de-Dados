# Plano de Estudos – Transpetro 2026 – Ciência de Dados (Ênfase 8)

**Prova:** domingo, 29/11/2026 · **Banca:** Fundação Cesgranrio · **Edital:** nº 04 – TRANSPETRO/PSP/TERRA/NÍVEL SUPERIOR 2026.4
**Hoje:** 20/09/2026 · **Início:** segunda, 21/09/2026 · **10 semanas até a prova**
**Carga:** 2h (seg–sex) + 6h (sáb) = 16h/semana ≈ 160h úteis até a prova
**Inscrição:** prazo encerrou em 14/09 — confirme que está inscrito antes de continuar.

Este arquivo substitui os antigos `01-plano-geral.md` + `02-cronograma-semanal.md` + `03-rotina-diaria.md`. É o único lugar que você precisa abrir para saber o que fazer hoje. Os outros diretórios continuam com sua função de sempre: `03-checklist/` para marcar progresso, `04-questoes/` para achar questões e registrar erros, `05-revisao/` para o formulário de fórmulas, `06-simulados/` para os simulados e a estratégia de prova.

---

## Como funciona cada sessão

**Dia útil (2h = dois blocos de 50 min).** Cada bloco cobre 1 tema do calendário abaixo, sempre na mesma ordem — teoria primeiro, depois exercício:

```
0–5 min    Reler o caderno de erros dos últimos 7 dias (04-questoes/caderno-de-erros.md)
5–30 min   Teoria direta do tema do bloco: resumo curto ou vídeo de até 20 min. Só o essencial — não é para dominar o assunto, é para entender o suficiente e reconhecer nas questões.
30–50 min  Exercícios Cesgranrio sobre esse mesmo tema (10–15 questões). Toda questão errada ou chutada vai para o caderno de erros, com a pegadinha em uma linha.
```

Intervalo real de 10 min entre os dois blocos (levantar, água, sem celular). Ao final do dia, marque **T** (teoria) e **Q** (exercícios) no `03-checklist/checklist-edital.md` para os temas cobertos.

**Sábado (6h = três blocos de 2h)** nas semanas de conteúdo (1 a 7):

```
Bloco 1 (2h)  Revisão em massa: 40–50 questões cronometradas misturando os temas da semana.
Bloco 2 (2h)  Fechar lacunas: para cada erro/chute, teoria dirigida de 5–10 min + caderno de erros.
Bloco 3 (2h)  Aprofundamento do tema mais pesado da semana (indicado no calendário).
```

Nas semanas de simulado (8 e 9) o sábado inteiro é o simulado + correção (ver seção Simulados). Na semana da prova (10) o sábado é descanso total.

**Domingo:** descanso, sem estudo. **Regra geral:** um tema atrasado não empurra a semana — se sobrou, entra no bloco 3 do sábado; se não coube, marque "pendente" no checklist e siga em frente.

---

## Onde focar (prioridade dos blocos do edital)

O edital tem 12 blocos de Específicos, mas a prova não pesa igual. Estimativa própria a partir do padrão Cesgranrio em provas parecidas (não é dado oficial):

| Prioridade | Blocos | Questões estimadas (de 50) |
|---|---|---|
| 🔴 Alta | VII Classes de Modelos, II Probabilidade e Estatística, IX Programação e Ferramentas, VI Modelagem | ~31 |
| 🟡 Média | V Preparação de Dados, III Bases de Dados, VIII NLP, I Matemática | ~14 |
| 🟢 Baixa | X Visualização, XI+XII Governança, IV Gestão de Projetos | ~5 |

Gerais (20 questões): **nunca deixe zero em Português ou Inglês** — zero em qualquer um elimina, mesmo com nota alta em Específicos. Ordem de prioridade no dia a dia: 1º garantir base sólida nos blocos vermelhos, 2º não negligenciar Português/Inglês.

---

## Calendário dia a dia

Todo dia útil tem 2 temas (um por bloco de 50 min). "Revisão em massa" no sábado = questões misturadas dos temas da própria semana.

### Semana 1 · 21–27/09 · Fundamentos

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 21/09 | II.1 Probabilidade: definições, axiomas, condicional | PT: compreensão de texto + estilo Cesgranrio |
| Ter 22/09 | IV Ciclo de vida de projetos; CRISP-DM, TDSP, OSEMN; Scrum/Kanban | IX.1 Python básico: tipos, listas/dicts/sets, controle de fluxo, funções, escopo |
| Qua 23/09 | II.3 Estatística descritiva: média/mediana/moda, variância/DP/amplitude, quartis/percentis | EN: estratégia de leitura (skimming, cognatos, falsos cognatos) |
| Qui 24/09 | VI.1 + VI.3 Pipeline de treino; matriz de confusão, accuracy, precision, recall, F1, ROC-AUC | IX.2 Pandas: DataFrame, `loc/iloc`, filtros, `groupby`, `merge`, `dropna/fillna` |
| Sex 25/09 | III.1–2 Tipos de dados (nominal/ordinal/discreto/contínuo), tidy data, formatos (csv/json/xml), metadados | PT: ortografia + significação das palavras |
| Sáb 26/09 | Revisão em massa (40–50 questões dos temas acima) | Aprofundamento: ROC-AUC, curva ROC, threshold — praticar no Colab com `sklearn.metrics` |
| Dom 27/09 | Descanso | |

### Semana 2 · 28/09–04/10 · Distribuições e métricas

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 28/09 | II.2 Variáveis aleatórias: Bernoulli, Binomial, Poisson (esperança, variância, quando usar) | PT: coesão textual (referência, conectivos) |
| Ter 29/09 | VI.3 Métricas de regressão (MSE/RMSE/MAE/R²/R² ajustado); viés×variância; over/underfitting | IX.2 NumPy: arrays, shape, broadcasting, `axis`, operações vetorizadas |
| Qua 30/09 | II.2 Uniforme, Normal (padronização z), Exponencial | EN: itens gramaticais (tempos verbais, modais, conectores) |
| Qui 01/10 | VI.4 Regularização (lasso/ridge/elastic net, dropout, early stopping, batch norm) + VI.6 K-fold, LOOCV, bootstrap | IX.2 Matplotlib/Seaborn: tipos de gráfico e leitura de código de plot |
| Sex 02/10 | XI Governança de dados (DMBOK): objetivos, qualidade, integridade, privacidade | EN: 15 questões |
| Sáb 03/10 | Revisão em massa | Aprofundamento: VI.5 dados desbalanceados (over/undersampling, SMOTE, pesos) |
| Dom 04/10 | Descanso | |

### Semana 3 · 05–11/10 · Bayes, TCL, SQL e preparação de dados

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 05/10 | II.4 Independência, probabilidade total, teorema de Bayes (exercícios numéricos) | PT: emprego de tempos e modos verbais |
| Ter 06/10 | V.3–4 Problemas de qualidade (ausentes, duplicatas, outliers, imputação), limpeza, data profiling | IX.3 SQL: SELECT, WHERE, ORDER BY, agregação, GROUP BY/HAVING |
| Qua 07/10 | II.4–5 Lei dos grandes números, TCL + distribuição amostral da média e da proporção | EN: vocabulário técnico de TI/energia |
| Qui 08/10 | V.5–6 Normalização×padronização, discretização, encoding; feature engineering e seleção | IX.3 SQL: JOINs (inner/left/right/full), subconsultas, DISTINCT, CASE, NULL |
| Sex 09/10 | V.1–2 + V.7 Metadados/linhagem, web scraping, amostragem, treino/validação/teste, cross-validation | PT: classes de palavras |
| Sáb 10/10 | Revisão em massa | Aprofundamento: SQL no Colab/SQLite (15 exercícios de JOIN + GROUP BY + subquery) |
| Dom 11/10 | Descanso | |

### Semana 4 · 12–18/10 · Inferência e classificadores
> Segunda 12/10 é feriado (Nossa Senhora Aparecida): sessão normal de 2h.

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 12/10 (feriado) | II.6 Estimação pontual/intervalar, intervalos de confiança (z e t) | PT: coordenação e subordinação |
| Ter 13/10 | VII.3 Regressão logística (sigmoide, odds) + KNN (k, distância, escalonamento) | III.4–5 SGBD, transações (ACID), índices, integridade; modelo ER, chaves, modelo relacional |
| Qua 14/10 | II.6 Testes de hipóteses: H0/H1, erro tipo I/II, poder, p-valor; testes z e t; teste de proporções; teste A/B | EN: falsos cognatos |
| Qui 15/10 | VII.3 Árvores de decisão (CART, Gini, entropia, poda), Random Forest, Naive Bayes | III.5 NoSQL: chave-valor, colunar, documentos, grafos; estruturado×semi×não estruturado |
| Sex 16/10 | II.5 Qui-quadrado, t de Student, F + II.6 testes qui-quadrado (independência e aderência) | PT: pontuação |
| Sáb 17/10 | Revisão em massa | Aprofundamento: VII.3 SVM (margem, kernel, C) + tabela comparativa de classificadores |
| Dom 18/10 | Descanso | |

### Semana 5 · 19–25/10 · Regressão, ensembles, clustering, Big Data

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 19/10 | II.7 Correlação×causalidade, Pearson, Spearman, parcial | PT: concordância verbal e nominal |
| Ter 20/10 | VII.5 Bagging×boosting: AdaBoost, Gradient Boosting, XGBoost, LightGBM, CatBoost; stacking | III.3 + III.6 Data warehouse×mart×lake×lakehouse; nuvem; Big Data (Hadoop, HDFS, MapReduce, Spark, Parquet) |
| Qua 21/10 | VII.4 Regressão linear simples/múltipla: MQO, hipóteses clássicas, R², F-test, resíduos | EN: texto longo + referência e conectores |
| Qui 22/10 | VII.2 Clusterização: K-Means (inércia, elbow, silhueta), hierárquico, GMM, DBSCAN | IX.2 Scikit-learn: `fit/predict/transform`, `train_test_split`, `Pipeline`, `GridSearchCV` |
| Sex 23/10 | VII.4 Testes de significância, ANOVA, modelos log-log/lin-log/log-lin/inverso | PT: regência verbal e nominal |
| Sáb 24/10 | Revisão em massa | Aprofundamento: VI.2 otimização de hiperparâmetros (grid/random search, AutoML) + VI.7 data-centric AI |
| Dom 25/10 | Descanso | |

### Semana 6 · 26/10–01/11 · Álgebra linear, redes neurais, redução de dimensionalidade

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 26/10 | I.2 Vetores e matrizes: operações, tipos, transformações lineares, sistemas lineares | PT: crase |
| Ter 27/10 | VII.10 Redes neurais: arquitetura, ativação (ReLU/sigmoid/tanh/softmax), forward, backprop, loss, otimizadores, épocas, batch | IX.2 TensorFlow/Keras/PyTorch: leitura de código (Sequential, Dense, compile/fit) |
| Qua 28/10 | I.2 Normas (L1, L2, infinita, p, Minkowski, Chebyshev), autovalores/autovetores | EN: phrasal verbs e vocabulário técnico |
| Qui 29/10 | VII.10 CNN, RNN, LSTM, GRU, GAN, embeddings, multimodais (o que é, diferença) | VII.1 PCA, LDA, ICA, t-SNE, autoencoders |
| Sex 30/10 | I.2 Cholesky e SVD (conceito, quando se aplica) + I.1 Cálculo: derivadas, derivadas parciais, máximos/mínimos, gradiente | PT: colocação pronominal |
| Sáb 31/10 | Revisão em massa | Aprofundamento: estatística inteira (bloco II) — 30 questões cronometradas |
| Dom 01/11 | Descanso | |

### Semana 7 · 02–08/11 · Séries temporais, NLP, Power BI, visualização
> Segunda 02/11 é feriado (Finados): sessão normal de 2h.

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 02/11 (feriado) | VII.7 Séries temporais: componentes, ACF/PACF, estacionaridade, AR/MA/ARMA/ARIMA, suavização exponencial, decomposição, ARIMAX, cointegração | PT: bateria mista 20 questões |
| Ter 03/11 | VIII.1–2 NLP: pré-processamento (stop words, stemming, lematização), BoW, N-grams, TF-IDF, Word2Vec/GloVe, Doc2Vec/BERT/ELMo | IX.4 Power BI: importação, modelagem (relacionamentos, esquema estrela), medidas×colunas calculadas (DAX básico), visuais |
| Qua 04/11 | VII.8 Tópicos em regressão: painel, GLM, Poisson, quantílica, espacial, VAR, ECM, GARCH (conceito e quando usar) | EN: bateria mista 15 questões |
| Qui 05/11 | VIII.3–5 LDA/NMF, modelos de linguagem, transformers, tarefas de NLP (classificação, sentimento, NER, sumarização, POS, tradução) | X.1–4 Tipos de gráfico, princípios de design, dashboards, storytelling |
| Sex 06/11 | VII.9 Modelos causais: experimentos/quase-experimentos, RDD, variáveis instrumentais, diff-in-diff, pareamento + VII.6 sistemas de recomendação | PT: revisão dos erros das 7 semanas |
| Sáb 07/11 | Revisão em massa | Aprofundamento: XII governança e IA responsável (viés, envenenamento, ataques adversariais, alucinação) + IX.2 bibliotecas restantes (NLTK, spaCy, Hugging Face, PySpark, Streamlit) |
| Dom 08/11 | Descanso · **Checkpoint:** o checklist deve estar com T marcado em praticamente todos os itens. Conteúdo novo termina aqui. | |

---

### Semana 8 · 09–15/11 · Revisão dos blocos vermelhos + Simulado 1

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 09/11 | Revisão II (Estatística): 20 questões direcionadas ao caderno de erros | PT: 15 questões |
| Ter 10/11 | Revisão VII (Classes de Modelos): 20 questões | Revisão IX (Python/SQL): 15 questões com leitura de código |
| Qua 11/11 | Revisão VI (Modelagem/métricas): 20 questões | EN: 15 questões |
| Qui 12/11 | Revisão V + III (preparação e bases de dados): 20 questões | Revisão I (Matemática): 15 questões |
| Sex 13/11 | PT + EN: 10+10 questões cronometradas (25 min) | Caderno de erros completo (leitura) |
| Sáb 14/11 | **SIMULADO 1** — 4h30, 70 questões (ver `06-simulados/`) | Correção e análise de erros (1h30) |
| Dom 15/11 | Descanso (feriado — Proclamação da República) | |

### Semana 9 · 16–22/11 · Pontos fracos do Simulado 1 + Simulado 2
> Sexta 20/11 é feriado (Consciência Negra): sessão leve.

| Dia | Bloco 1 | Bloco 2 |
|---|---|---|
| Seg 16/11 | Pior bloco do Simulado 1: 25 questões direcionadas | PT: 15 questões |
| Ter 17/11 | 2º pior bloco do Simulado 1: 25 questões | Revisão VIII (NLP) + X (visualização): 15 questões |
| Qua 18/11 | 3º pior bloco do Simulado 1: 25 questões | EN: 15 questões |
| Qui 19/11 | Revisão XI+XII (governança) + IV (gestão de projetos): 15 questões | Formulário rápido: revisar e completar |
| Sex 20/11 (feriado) | Caderno de erros inteiro (leitura) | Formulário rápido (leitura) — sessão leve |
| Sáb 21/11 | **SIMULADO 2** — 4h30 | Correção e análise de erros (1h30) |
| Dom 22/11 | Descanso | |

### Semana 10 · 23–29/11 · Semana da prova (sem conteúdo novo)

| Dia | Atividade |
|---|---|
| Seg 23/11 | 20 questões mistas leves (pontos fracos do Simulado 2) + caderno de erros |
| Ter 24/11 | **Imprimir o Cartão de Confirmação de Inscrição** (Cesgranrio). 20 questões + formulário rápido |
| Qua 25/11 | 20 questões leves + caderno de erros. Conferir local de prova, trajeto, documento com foto |
| Qui 26/11 | Leitura do formulário rápido. 10 questões de PT + 10 de EN |
| Sex 27/11 | Leitura leve do formulário. Separar documento com foto, caneta preta transparente, água. Dormir cedo |
| Sáb 28/11 | **Descanso total** |
| **Dom 29/11** | **PROVA.** Chegar com 1h de antecedência. Estratégia detalhada em `06-simulados/estrategia-de-prova.md` |

---

## Metas numéricas

| Momento | Específicos (/50) | Português (/10) | Inglês (/10) |
|---|---|---|---|
| Checkpoint fim da semana 7 (08/11) | ≥ 60% nas questões avulsas por tema | ≥ 65% | ≥ 65% |
| Simulado 1 (14/11) | ≥ 30 | ≥ 6 | ≥ 6 |
| Simulado 2 (21/11) | ≥ 35 | ≥ 7 | ≥ 7 |
| Dia da prova (meta) | 36+ | 8 | 8 |

Corte de eliminação (não é meta, é o mínimo absoluto): 25/50 em Específicos, 10/20 em Gerais, e nunca zero em Português ou Inglês.
