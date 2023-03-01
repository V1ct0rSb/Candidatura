# Dicionario
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# Total de faturamento
total = sum(faturamento.values())

# Percentual de faturamento e add no dicionario
for estado, valor in faturamento.items():
    percent = round((valor / total) * 100, 2)
    faturamento[estado] = {'Valor': valor, 'Percentual': percent}

# Maior e menor percentual por estado
estadoMax = max(
    faturamento, key=lambda estado: faturamento[estado]['Percentual'])
estadoMin = min(
    faturamento, key=lambda estado: faturamento[estado]['Percentual'])

# Saida
print(faturamento)
print('=-' * 10)

print(f'''O estado com o maior percentual é {estadoMax} com {faturamento[estadoMax]["Percentual"]:.2f}%
O estado com o maior percentual é {estadoMin} com {faturamento[estadoMin]["Percentual"]:.2f}%
''')
