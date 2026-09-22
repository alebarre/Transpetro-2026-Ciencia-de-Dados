# Dashboard — link publicado

**URL atual:** https://claude.ai/artifact/WKickXLWRrWUsGc5imHJd8
**Última atualização:** 2026-09-21 (bateria do dia 1: Probabilidade 15/20, Português 15/18, 2h de estudo)

O link é privado (só quem tem acesso à sua conta consegue abrir).

## Como atualizar (feito pelo assistente, aqui documentado para referência)

1. Escrever/atualizar o `resultado.json` do dia em `04-questoes/bateria-diaria/<data>/`.
2. Rodar `python3 07-dashboard/aggregate.py` (regenera `07-dashboard/dados.json`).
3. Republicar o Artifact com `file_path=07-dashboard/dashboard.html`, `files={"dados.json": "07-dashboard/dados.json"}` e `url` igual à URL acima — isso atualiza a mesma página, sem gerar um link novo.
4. Atualizar a data em "Última atualização" acima.

`dados.json` é gerado pelo script — não editar à mão.
