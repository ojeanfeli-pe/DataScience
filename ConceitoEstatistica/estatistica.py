# Importando as bibliotecas necessárias
import numpy as np  # Para cálculos numéricos e vetoriais
import statistics as stats  # Para operações estatísticas básicas
from scipy import stats as sp_stats  # Para operações estatísticas mais avançadas
import pandas as pd  # Para manipulação de dados

class Estatistica:
    def __init__(self, data):
        """
        Inicializa a classe Estatistica com os dados.
        :param data: Lista de dados numéricos.
        """
        if isinstance(data, (list, np.ndarray)):
            self.data = np.array(data)
        else:
            raise ValueError("Os dados devem ser uma lista ou um array numpy.")
    
    def media(self):
        """
        Calcula a média dos dados.
        Média é a soma de todos os valores dividida pelo número de valores.
        :return: Média dos dados.
        """
        return np.mean(self.data)

    def mediana(self):
        """
        Calcula a mediana dos dados.
        Mediana é o valor central de um conjunto de dados ordenado.
        :return: Mediana dos dados.
        """
        return np.median(self.data)

    def moda(self):
        """
        Calcula a moda dos dados.
        Moda é o valor que aparece com mais frequência no conjunto de dados.
        :return: Moda dos dados.
        """
        return stats.mode(self.data)

    def variancia(self):
        """
        Calcula a variância dos dados.
        Variância mede a dispersão dos dados em relação à média.
        :return: Variância dos dados.
        """
        return np.var(self.data)

    def desvio_padrao(self):
        """
        Calcula o desvio padrão dos dados.
        Desvio padrão é a raiz quadrada da variância e representa a dispersão dos dados.
        :return: Desvio padrão dos dados.
        """
        return np.std(self.data)

    def coeficiente_variacao(self):
        """
        Calcula o coeficiente de variação.
        Coeficiente de variação é a relação entre o desvio padrão e a média.
        :return: Coeficiente de variação dos dados.
        """
        return self.desvio_padrao() / self.media()

    def quartis(self):
        """
        Calcula os quartis dos dados.
        Quartis dividem os dados em quatro partes iguais.
        :return: Primeiro, segundo (mediana) e terceiro quartis.
        """
        return np.percentile(self.data, [25, 50, 75])

    def intervalo_confianca(self, confidence=0.95):
        """
        Calcula o intervalo de confiança para a média.
        Intervalo de confiança é a faixa dentro da qual a verdadeira média populacional está com uma certa confiança.
        :param confidence: Nível de confiança (por padrão, 95%).
        :return: Intervalo de confiança para a média dos dados.
        """
        n = len(self.data)
        m = self.media()
        se = sp_stats.sem(self.data)  # Erro padrão da média
        h = se * sp_stats.t.ppf((1 + confidence) / 2., n-1)
        return m - h, m + h

    def skewness(self):
        """Calcula a assimetria dos dados."""
        return sp_stats.skew(self.data)
    
    def kurtosis(self):
        """Calcula a curtose dos dados."""
        return sp_stats.kurtosis(self.data)
    
    def boxplot(self):
        """Cria um boxplot dos dados."""
        import matplotlib.pyplot as plt
        
        plt.boxplot(self.data)
        plt.title('Boxplot dos Dados')
        plt.ylabel('Valores')
        plt.show()
        
    def histograma(self, bins=10):
        """Cria um histograma dos dados."""
        import matplotlib.pyplot as plt
        
        plt.hist(self.data, bins=bins, alpha=0.7, color='blue')
        plt.title('Histograma dos Dados')
        plt.xlabel('Valores')
        plt.ylabel('Frequência')
        plt.show()
    
    def resumo_estatistico(self):
        """
        Retorna um resumo estatístico básico dos dados.
        Inclui média, mediana, moda, variância, desvio padrão e coeficiente de variação.
        :return: Dicionário com o resumo estatístico.
        """
        return {
            'Média': self.media(),
            'Mediana': self.mediana(),
            'Moda': self.moda(),
            'Variância': self.variancia(),
            'Desvio Padrão': self.desvio_padrao(),
            'Coeficiente de Variação': self.coeficiente_variacao(),
            'Quartis': self.quartis()
        }

# Exemplo de uso da classe Estatistica
dados = [10, 20, 20, 30, 40, 50, 60, 70, 80, 90, 100]

estatistica = Estatistica(dados)

# Imprimindo cada resultado
print("Média:", estatistica.media())
print("Mediana:", estatistica.mediana())
print("Moda:", estatistica.moda())
print("Variância:", estatistica.variancia())
print("Desvio Padrão:", estatistica.desvio_padrao())
print("Coeficiente de Variação:", estatistica.coeficiente_variacao())
print("Quartis:", estatistica.quartis())
print("Intervalo de Confiança:", estatistica.intervalo_confianca())
print("Resumo Estatístico:", estatistica.resumo_estatistico())

# Gerando gráficos
estatistica.boxplot()  # Exibe o boxplot
estatistica.histograma(bins=5)  # Exibe o histograma com 5 bins