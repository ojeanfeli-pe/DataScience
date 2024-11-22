import pandas as pd
import matplotlib.pyplot as plt
import statistics

# Dados fornecidos
data = {
    'Ano': [2018]*12 + [2019]*12,
    'Mes': ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'] * 2,
    'Voos': [
        2576261.00, 2605207.00, 3197326.00, 3508607.00, 3705129.00, 3843131.00,
        3999933.00, 4044126.00, 3393644.00, 3677923.00, 3296694.00, 3093944.00,
        2710036.00, 2716724.00, 3457362.00, 3647276.00, 3879343.00, 3946406.00,
        4072082.00, 4120937.00, 3547546.00, 3771212.00, 3264105.00, 3389382.00
    ],
    'Taxa_Ocupacao': [
        638.00, 679.00, 828.00, 864.00, 882.00, 917.00, 911.00, 921.00, 918.00,
        917.00, 804.00, 655.00, 629.00, 725.00, 812.00, 877.00, 878.00, 898.00,
        900.00, 888.00, 895.00, 907.00, 803.00, 717.00
    ]
}

# Criando um DataFrame
df = pd.DataFrame(data)

# Cálculo de média, mediana e desvio padrão
media_voos = df['Voos'].mean()
mediana_voos = df['Voos'].median()
desvio_padrao_voos = df['Voos'].std()

media_taxa_ocupacao = df['Taxa_Ocupacao'].mean()
mediana_taxa_ocupacao = df['Taxa_Ocupacao'].median()
desvio_padrao_taxa_ocupacao = df['Taxa_Ocupacao'].std()

# Exibindo os resultados
print(f"Média de Voos: {media_voos:.2f}")
print(f"Mediana de Voos: {mediana_voos:.2f}")
print(f"Desvio Padrão de Voos: {desvio_padrao_voos:.2f}")

print(f"Média de Taxa de Ocupação: {media_taxa_ocupacao:.2f}")
print(f"Mediana de Taxa de Ocupação: {mediana_taxa_ocupacao:.2f}")
print(f"Desvio Padrão de Taxa de Ocupação: {desvio_padrao_taxa_ocupacao:.2f}")

# Gerando gráficos
plt.figure(figsize=(12, 6))

# Gráfico de Voos
plt.subplot(1, 2, 1)
plt.plot(df['Mes'], df['Voos'], marker='o')
plt.title('Voos Internacionais por Mês')
plt.xlabel('Mes')
plt.ylabel('Número de Voos')
plt.xticks(rotation=45)
plt.grid()

# Gráfico de Taxa de Ocupação
plt.subplot(1, 2, 2)
plt.plot(df['Mes'], df['Taxa_Ocupacao'], marker='o', color='orange')
plt.title('Taxa de Ocupação de Hotelaria por Mês')
plt.xlabel('Mes')
plt.ylabel('Taxa de Ocupação (%)')
plt.xticks(rotation=45)
plt.grid()


plt.tight_layout()
plt.show()