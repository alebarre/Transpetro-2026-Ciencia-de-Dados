# Formulário Rápido – o que mais cai e precisa estar na ponta da língua

Leia nos 10 minutos iniciais das sessões e inteiro nos dias 26 e 27/11. Complete com o que descobrir nas questões.

## Estatística descritiva
- Média = Σx/n · Mediana = valor central (média dos dois centrais se n par) · Moda = mais frequente.
- Variância populacional σ² = Σ(x−μ)²/N · Variância amostral s² = Σ(x−x̄)²/(n−1) · DP = √var · Amplitude = máx − mín.
- Coeficiente de variação = DP/média. Quartis: Q1 = 25%, Q2 = mediana, Q3 = 75%; IQR = Q3 − Q1; outlier (boxplot) fora de [Q1 − 1,5·IQR, Q3 + 1,5·IQR].
- Assimetria: média > mediana ⇒ cauda à direita (positiva).

## Probabilidade
- P(A∪B) = P(A) + P(B) − P(A∩B) · Independentes ⇔ P(A∩B) = P(A)·P(B).
- Condicional: P(A|B) = P(A∩B)/P(B). Total: P(B) = Σ P(B|Aᵢ)·P(Aᵢ).
- **Bayes:** P(A|B) = P(B|A)·P(A) / P(B).
- Bernoulli(p): E = p, Var = p(1−p). Binomial(n,p): E = np, Var = np(1−p), P(X=k) = C(n,k)pᵏ(1−p)ⁿ⁻ᵏ.
- Poisson(λ): E = Var = λ, P(X=k) = e⁻ᵏλᵏ/k!. Exponencial(λ): E = 1/λ, Var = 1/λ², sem memória.
- Uniforme(a,b): E = (a+b)/2, Var = (b−a)²/12. Normal: z = (x−μ)/σ; 68–95–99,7%.
- LGN: média amostral → μ. **TCL:** média amostral ~ Normal(μ, σ²/n) para n grande, qualquer distribuição original.

## Inferência
- Erro padrão da média = σ/√n. IC média (σ conhecido): x̄ ± z·σ/√n (z = 1,96 para 95%; 1,645 para 90%; 2,576 para 99%). σ desconhecido: t com n−1 gl.
- IC proporção: p̂ ± z·√(p̂(1−p̂)/n).
- Erro tipo I = rejeitar H0 verdadeira (α). Erro tipo II = não rejeitar H0 falsa (β). Poder = 1 − β. p-valor < α ⇒ rejeita H0.
- Qui-quadrado: independência (tabela de contingência, gl = (l−1)(c−1)) e aderência (gl = k−1). Teste F: comparação de variâncias / ANOVA.
- Correlação: Pearson (linear, −1 a 1), Spearman (monotônica, postos). Correlação ≠ causalidade.

## Métricas de classificação (matriz de confusão)
| | Previsto + | Previsto − |
|---|---|---|
| Real + | TP | FN |
| Real − | FP | TN |
- Accuracy = (TP+TN)/total · **Precision** = TP/(TP+FP) · **Recall** (sensibilidade) = TP/(TP+FN) · Especificidade = TN/(TN+FP).
- F1 = 2·P·R/(P+R). ROC: eixo x = FPR = FP/(FP+TN), eixo y = TPR = recall; AUC 0,5 = aleatório, 1 = perfeito.
- Recall importa quando FN custa caro (doença, fraude). Precision importa quando FP custa caro (spam bloqueando e-mail bom).
- Accuracy engana com classes desbalanceadas.

## Métricas de regressão
- MAE = média|erro| · MSE = média(erro²) · RMSE = √MSE (mesma unidade de y) · R² = 1 − SSres/SStot · R² ajustado penaliza nº de variáveis.

## Viés × variância, regularização, validação
- Alto viés = underfitting (modelo simples demais). Alta variância = overfitting (treino ótimo, teste ruim).
- Lasso (L1) zera coeficientes ⇒ seleção de variáveis. Ridge (L2) encolhe sem zerar. Elastic net = mistura. Dropout, early stopping, batch norm = redes neurais.
- K-fold: k partições, treina k vezes. LOOCV: k = n. Bootstrap: reamostragem com reposição. Holdout: treino/validação/teste (validação para hiperparâmetros; teste só no final).
- Desbalanceamento: oversampling (SMOTE gera sintéticos), undersampling, `class_weight`.

## Modelos – resumo em uma linha
- Regressão logística: sigmoide, saída probabilidade, linear no logit. KNN: preguiçoso, depende de escala e de k. SVM: maximiza margem, kernel para não linear, C regula tolerância.
- Árvore CART: divisões por Gini/entropia; interpretável; overfita se profunda. Random Forest = bagging de árvores + subconjunto de features. Boosting = sequencial, corrige erros (AdaBoost, GBM, XGBoost, LightGBM, CatBoost). Stacking = meta-modelo sobre previsões.
- Naive Bayes: assume independência entre atributos; bom para texto.
- K-Means: k fixo, centróides, sensível a outliers e escala, elbow/silhueta. Hierárquico: dendrograma. DBSCAN: densidade, acha ruído, não exige k. GMM: clusters probabilísticos.
- PCA: componentes ortogonais de máxima variância (não supervisionado). LDA (discriminante): maximiza separação entre classes (supervisionado). t-SNE: só visualização. Autoencoder: rede que comprime e reconstrói.
- Regressão linear: MQO; hipóteses: linearidade, erros com média 0, homocedasticidade, sem autocorrelação, sem multicolinearidade, normalidade dos erros. F-test = significância global; t = coeficiente individual. Log-log: coeficiente = elasticidade.
- Séries temporais: estacionária = média/variância constantes (teste ADF). ACF corta ⇒ MA(q); PACF corta ⇒ AR(p). ARIMA(p,d,q), d = diferenciações. Suavização exponencial (Holt-Winters = tendência + sazonalidade).
- Redes neurais: ReLU (oculta), sigmoide (binária), softmax (multiclasse). Loss: MSE (regressão), cross-entropy (classificação). Backprop = gradiente da loss. Época = passagem completa; batch = subconjunto por atualização. CNN = imagens (convolução, pooling). RNN/LSTM/GRU = sequências. GAN = gerador × discriminador.
- Recomendação: colaborativa (usuários parecidos ou itens parecidos), conteúdo (atributos do item), híbrida. Cold start = item/usuário novo sem histórico.
- Causalidade: RCT (experimento), diff-in-diff, RDD, variáveis instrumentais, propensity score matching.

## NLP
- Pipeline: limpeza → tokenização → stop words → stemming (corta) / lematização (dicionário). BoW e TF-IDF = frequência (TF × log(N/df)). Word2Vec (CBOW, skip-gram), GloVe = embeddings estáticos; BERT/ELMo = contextuais. LDA = tópicos. Transformer = atenção, sem recorrência.

## Python / Pandas / NumPy / SQL
- Índice começa em 0; fatia `a[1:3]` exclui o 3; `range(5)` = 0..4; `//` divisão inteira, `%` resto, `**` potência.
- Lista mutável e ordenada; tupla imutável; set sem duplicatas e sem ordem; dict chave→valor. `is` compara identidade, `==` valor.
- Pandas: `df.loc[rótulo]`, `df.iloc[posição]`; `groupby().agg()`; `merge(how='inner|left|right|outer')`; `concat`; `dropna`, `fillna`; `isnull().sum()`; `apply`; `pivot_table`; `value_counts`; `describe()`.
- NumPy: `axis=0` opera pelas linhas (resultado por coluna), `axis=1` pelas colunas (resultado por linha). Broadcasting. `reshape`, `shape`.
- Scikit-learn: `fit` (treina), `transform` (aplica), `fit_transform`, `predict`, `predict_proba`. `train_test_split(test_size=)`. `StandardScaler` (z), `MinMaxScaler` (0–1). `Pipeline`, `GridSearchCV(cv=)`.
- SQL: ordem lógica FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY. WHERE filtra linhas antes de agrupar; HAVING filtra grupos. `COUNT(*)` conta NULL, `COUNT(col)` não. `INNER` só casamentos; `LEFT` mantém todas da esquerda com NULL. `NULL = NULL` é desconhecido: use `IS NULL`. `UNION` remove duplicatas, `UNION ALL` não.
- Serialização: `pickle` (binário Python), `json` (texto).

## Dados e arquitetura
- DW: integrado, histórico, esquema estrela/floco de neve (fato + dimensões). Data mart: DW departamental. Data lake: bruto, schema-on-read. Lakehouse: lake + transações/ACID (Delta, Iceberg).
- ACID: atomicidade, consistência, isolamento, durabilidade. Índice acelera leitura, custa escrita. NoSQL: chave-valor (Redis), documentos (MongoDB), colunar (Cassandra), grafos (Neo4j).
- Hadoop = HDFS (armazenamento distribuído) + MapReduce (processamento em disco). Spark = em memória, mais rápido, RDD/DataFrame, PySpark. Parquet = colunar, comprimido.
- CRISP-DM: entendimento do negócio → dos dados → preparação → modelagem → avaliação → implantação. OSEMN: obtain, scrub, explore, model, interpret. TDSP: Microsoft, iterativo.

## Governança e IA responsável
- DMBOK: áreas de conhecimento (governança, qualidade, metadados, segurança, arquitetura…). Linhagem = rastro do dado. LGPD: titular, controlador, operador, bases legais, dados sensíveis.
- Riscos de IA: viés algorítmico; envenenamento (dados de treino adulterados); ataque adversarial (entrada manipulada engana o modelo); ataque de inferência (descobrir se um dado estava no treino); roubo/extração de modelo; alucinação (LLM inventa). IA responsável: transparência, explicabilidade, justiça, responsabilização, segurança, conformidade.

## Álgebra linear e cálculo
- Normas de v: L1 = Σ|vᵢ| (Manhattan), L2 = √Σvᵢ² (Euclidiana), L∞ = máx|vᵢ| (Chebyshev), Lp = (Σ|vᵢ|ᵖ)^(1/p) (Minkowski). Lasso usa L1, ridge usa L2.
- Av = λv (autovalor λ, autovetor v). PCA = autovetores da matriz de covariância. SVD: A = UΣVᵀ. Cholesky: A = LLᵀ (A simétrica definida positiva).
- Derivada = taxa de variação; gradiente = vetor de derivadas parciais; descida do gradiente: w ← w − η·∇L. Máximo/mínimo: derivada zero, sinal da segunda derivada.

## Português – lembretes
- Crase: a + a (preposição + artigo feminino). Não há crase antes de masculino, verbo, pronome pessoal, palavra no plural com "a" singular. Facultativa antes de nome feminino próprio e pronome possessivo feminino.
- Concordância: sujeito composto antes do verbo ⇒ plural. "Haver" existencial e "fazer" temporal são impessoais (singular). Verbo + "se" apassivador concorda com o sujeito paciente.
- Regência: assistir (a) = ver; visar (a) = ter em vista; preferir X a Y (nunca "do que"); obedecer a; aspirar a = desejar.
- Coesão: referência (ele, este, tal), substituição, elipse, conectores (adversativo, concessivo, conclusivo, explicativo).

## Inglês – lembretes
- Falsos cognatos: actually (na verdade), eventually (por fim), pretend (fingir), library (biblioteca), fabric (tecido), sensible (sensato), assist (ajudar), attend (comparecer), realize (perceber), support (apoiar).
- Conectores: however/nevertheless (mas), although/despite (embora), therefore/thus (portanto), moreover/furthermore (além disso), whereas (enquanto que), unless (a menos que).
- Modais: must (obrigação/dedução), should (conselho), may/might (possibilidade), can/could (capacidade/possibilidade).
