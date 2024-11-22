import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score, silhouette_samples
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

# Cálculo da pontuação da silhueta para distância Manhattan
silhouette_avg = silhouette_score(X, kmeans_manhattan.labels_, metric='manhattan')
print(f"Pontuação média da silhueta (Manhattan): {silhouette_avg}")

# Calculando os valores da silhueta para cada amostra
sample_silhouette_values = silhouette_samples(X, kmeans_manhattan.labels_, metric='manhattan')

# Criando um gráfico de silhueta para distância Manhattan
plt.figure(figsize=(10,6))
y_lower = 10

for i in range(k):
    # Agregando os valores da silhueta para amostras pertencentes ao cluster i e ordenando-os
    ith_cluster_silhouette_values = sample_silhouette_values[kmeans_manhattan.labels_ == i]
    ith_cluster_silhouette_values.sort()
    
    size_cluster_i = ith_cluster_silhouette_values.shape[0]
    y_upper = y_lower + size_cluster_i
    
    plt.fill_betweenx(np.arange(y_lower, y_upper), 
                      ith_cluster_silhouette_values,
                      alpha=0.7)
    
    # Adicionando um rótulo no gráfico
    plt.text(-0.05, y_lower + 0.5 * size_cluster_i, str(i))
    
    # Atualizando o limite inferior para o próximo cluster
    y_lower = y_upper + 10  

plt.title('Gráfico de Silhueta para K-Means Clustering (Manhattan)')
plt.xlabel('Valor da Silhueta')
plt.ylabel('Cluster')
plt.axvline(x=silhouette_avg, color="red", linestyle="--")
plt.yticks([])
plt.xlim([-0.1, max(sample_silhouette_values) + 0.1])
plt.tight_layout()

# Salvando a imagem do gráfico de silhueta
plt.savefig('silhouette_plot_manhattan_passageiros_logan.png')
plt.show()