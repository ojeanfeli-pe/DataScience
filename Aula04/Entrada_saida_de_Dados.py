"""
EXEMPLO DE LER OS ARQUIVOS . TXT ( O ARQUIVO DEVE ESTAR NO MESMO DIRETÓRIO)
"""
# -*- coding: utf-8 -*-

resultados = []
dados = open('dadosvibracoes.txt', 'r')
"LÊ EM LINHAS E IGNORA O CABEÇALHO"
linhas = dados.readlines() [1:]
dados.close()

for linha in linhas:
    #split as linhas nos campos
    field = linha.split()
    #Converte o texto em numeros
    frequencia = float(field[0])
    vv = float(field[1])
    hh = float(field[2])
    #agruoa e adiciona os resultados
    todos = [frequencia, vv, hh]
    resultados.append(todos)
    
dados = open('dadosvibracoes.txt', 'r')
cabecalho = dados.readlines() [0]
print(cabecalho)
dados.close()

for i in resultados: print(i)