import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm, t

# Defina uma semente para os números aleatórios, garantindo resultados repetíveis
np.random.seed(42)

# Classe para o Teorema Central do Limite
class TeoremaCentralLimite:
    def __init__(self, tamanho_amostra, n_simulacoes, media, desvio_padrao):
        self.tamanho_amostra = tamanho_amostra
        self.n_simulacoes = n_simulacoes
        self.media = media
        self.desvio_padrao = desvio_padrao
        self.amostras = []

    def gerar_amostras(self):
        for _ in range(self.n_simulacoes):
            amostra = np.random.normal(self.media, self.desvio_padrao, self.tamanho_amostra)
            self.amostras.append(np.mean(amostra))

    def calcular_probabilidade(self, z):
        return norm.cdf(z)

    def plotar_distribuicao(self):
        plt.hist(self.amostras, bins=30, density=True, alpha=0.6, color='g')
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, np.mean(self.amostras), np.std(self.amostras))
        plt.plot(x, p, 'k', linewidth=2)
        plt.title('Distribuição da Média das Amostras (Teorema Central do Limite)')
        
        # Adiciona o cálculo da probabilidade ao gráfico
        prob_z_1_96 = self.calcular_probabilidade(1.96)
        plt.figtext(0.15, 0.8, f'Probabilidade para z=1.96: {prob_z_1_96:.4f}', color="blue")
        
        plt.show()

# Classe para Covariância
class Covariancia:
    def __init__(self, dados_x, dados_y):
        self.dados_x = np.array(dados_x)
        self.dados_y = np.array(dados_y)

    def calcular_covariancia(self):
        return np.cov(self.dados_x, self.dados_y)[0, 1]

    def calcular_pearson(self):
        return np.corrcoef(self.dados_x, self.dados_y)[0, 1]

    def plotar_dados(self):
        plt.scatter(self.dados_x, self.dados_y)
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Dispersão de Dados X vs Y')
        
        # Adiciona o cálculo de Pearson e Corrcoef ao gráfico
        cov = self.calcular_covariancia()
        pearson = self.calcular_pearson()
        plt.figtext(0.15, 0.8, f'Covariância: {cov:.4f}', color="blue")
        plt.figtext(0.15, 0.75, f'Coeficiente de Pearson: {pearson:.4f}', color="blue")
        
        plt.show()

# Classe para o Teste t-Student
class TStudent:
    def __init__(self, amostra, media_populacao):
        self.amostra = np.array(amostra)
        self.media_populacao = media_populacao
        self.media_amostra = np.mean(amostra)
        self.desvio_padrao_amostra = np.std(amostra, ddof=1)
        self.tamanho_amostra = len(amostra)

    def calcular_t_stat(self):
        return (self.media_amostra - self.media_populacao) / (self.desvio_padrao_amostra / np.sqrt(self.tamanho_amostra))

    def calcular_p_valor(self, t_stat):
        return (1 - t.cdf(abs(t_stat), df=self.tamanho_amostra - 1)) * 2

    def plotar_distribuicao(self, t_stat):
        x = np.linspace(-4, 4, 1000)
        y = t.pdf(x, df=self.tamanho_amostra - 1)
        plt.plot(x, y, label='Distribuição t-Student')
        plt.axvline(x=t_stat, color='r', linestyle='--', label=f'Estatística t = {t_stat:.2f}')
        plt.title('Distribuição t-Student')
        plt.legend()
        
        # Adiciona o resultado do teste de hipótese ao gráfico
        resultado_hipotese = self.testar_hipotese()
        plt.figtext(0.15, 0.8, f'Resultado do Teste de Hipótese: {resultado_hipotese}', color="blue")
        
        plt.show()

    def testar_hipotese(self, alpha=0.05):
        t_stat = self.calcular_t_stat()
        p_valor = self.calcular_p_valor(t_stat)
        return "Rejeita a hipótese nula" if p_valor < alpha else "Não rejeita a hipótese nula"

# -------------------------
# Instanciando e executando cada classe
# -------------------------

# Exemplo de uso para o Teorema Central do Limite
tcl = TeoremaCentralLimite(tamanho_amostra=30, n_simulacoes=1000, media=0, desvio_padrao=1)
tcl.gerar_amostras()
tcl.plotar_distribuicao()
print("Probabilidade para z=1.96:", tcl.calcular_probabilidade(1.96))

# Exemplo de uso para Covariância
cov = Covariancia(dados_x=[1, 2, 3, 4, 5], dados_y=[2, 4, 6, 8, 10])
print("Covariância:", cov.calcular_covariancia())
print("Coeficiente de Pearson:", cov.calcular_pearson())
cov.plotar_dados()

# Exemplo de uso para t-Student
t_student = TStudent(amostra=[2.3, 2.5, 2.1, 2.6, 2.8], media_populacao=2.5)
t_stat = t_student.calcular_t_stat()
print("Estatística t:", t_stat)
print("p-valor:", t_student.calcular_p_valor(t_stat))
t_student.plotar_distribuicao(t_stat)
print("Resultado do teste de hipótese:", t_student.testar_hipotese())
