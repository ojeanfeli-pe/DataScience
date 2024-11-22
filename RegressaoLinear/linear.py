import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from sklearn.metrics import r2_score

# Dados
meses = np.arange(1, 25)  # 12 meses para 2018 e 12 meses para 2019
voos_internacionais = [
    3864, 3664, 4257, 4516, 4763, 4817, 5095, 5054, 4742, 4517, 3986, 4404,  # 2018
    4039, 3667, 4523, 4847, 4907, 4955, 5260, 5190, 4586, 4388, 3959, 4155   # 2019
]

# Função para a regressão linear
def linear_model(x, a, b):
    return a * x + b

# Função para a regressão logística (não linear)
def logistic_model(x, a, b, c):
    return c / (1 + np.exp(-(x - b) / a))

# Regressão Linear
params_linear, _ = curve_fit(linear_model, meses, voos_internacionais)
linear_fit = linear_model(meses, *params_linear)

# Regressão Logística
params_logistic, _ = curve_fit(logistic_model, meses, voos_internacionais, maxfev=10000)
logistic_fit = logistic_model(meses, *params_logistic)

# Cálculo do R^2
r2_linear = r2_score(voos_internacionais, linear_fit)
r2_logistic = r2_score(voos_internacionais, logistic_fit)

# Gráfico
plt.figure(figsize=(10, 6))
plt.scatter(meses, voos_internacionais, color='black', label='Dados reais')
plt.plot(meses, linear_fit, color='blue', label=f'Regressão Linear (R² = {r2_linear:.4f})')
plt.plot(meses, logistic_fit, color='red', label=f'Regressão Logística (R² = {r2_logistic:.4f})')
plt.xlabel('Mês')
plt.ylabel('Voos Internacionais')
plt.title('Regressão Linear vs Logística para Voos Internacionais da Logan')
plt.legend()
plt.grid(True)
plt.show()

# Exibe os parâmetros ajustados
print(f'Parâmetros da Regressão Linear: a = {params_linear[0]}, b = {params_linear[1]}')
print(f'Parâmetros da Regressão Logística: a = {params_logistic[0]}, b = {params_logistic[1]}, c = {params_logistic[2]}')
print(f'R² Regressão Linear: {r2_linear}')
print(f'R² Regressão Logística: {r2_logistic}')