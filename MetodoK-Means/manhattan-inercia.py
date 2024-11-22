import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd

# Dados dos passageiros da Logan
data = {
    'Ano': [2018]*12 + [2019]*12,
    'Mes': [
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro',
        'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho',
        'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro'
    ],
    'Passageiros': [
        2576261, 2605070, 3197326, 3508607, 3705129, 3843131,
        3999933, 4044126, 3393644, 3677923, 3296694, 3093944,
        2710036, 2716724, 3457362, 3647276, 3879343, 3946406,
        4072082, 4120937, 3547546, 3771212, 3264105, 3389382
    ]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Usar apenas a coluna de Passageiros para o KMeans
X = df[['Passageiros']].values

# Definindo o número de clusters
k = 5

# Criando o modelo KMeans com distância Manhattan
kmeans_manhattan = KMeans(n_clusters=k, random_state=0)
kmeans_manhattan.fit(X)

# Atribuindo os rótulos aos dados
df['Cluster'] = kmeans_manhattan.labels_

# Calculando a inércia
inertia = kmeans_manhattan.inertia_
print(f"Inércia (Manhattan): {inertia}")

# Plotando os resultados
plt.figure(figsize=(10,6))
plt.scatter(df['Mes'], df['Passageiros'], c=df['Cluster'], cmap='viridis')
plt.title('K-Means Clustering dos Passageiros da Logan (Distância Manhattan)')
plt.xlabel('Meses')
plt.ylabel('Número de Passageiros')
plt.xticks(rotation=45)
plt.grid()
plt.colorbar(label='Cluster')
plt.tight_layout()

# Salvando a imagem
plt.savefig('kmeans_manhattan_inertia.png')
plt.show()