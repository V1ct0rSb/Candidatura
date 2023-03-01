import json

# Leitura do Json
with open('questao03/faturamentoMensal.json', 'r') as arquivo:
    dados = json.load(arquivo)

# Maior e menor faturamento
faturamentos = [item['revenue'] for item in dados['data']]
menorFatura = min(faturamentos)
maiorFatura = max(faturamentos)

# Media de faturamento
faturaTotal = sum(faturamentos)
diasNoMes = len(dados['data'])
mediaFatura = faturaTotal / diasNoMes

# Faturamento acima da média
acimaMedia = sum(1 for faturamento in faturamentos if faturamento > mediaFatura)

# Saida
print(f"Menor faturamento diário:{menorFatura}" )
print(f"Maior faturamento diário: {maiorFatura}")
print(f"Número de dias com faturamento acima da média: {acimaMedia}")
