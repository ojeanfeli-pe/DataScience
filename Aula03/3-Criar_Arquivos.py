texto = "Parabens"

print(texto)

f = open("meuArquivo.txt", "x") #metodo para criar um arquivo

dados_arquivo = "Arquivo criado com o meotodo 'x' "

f.write(dados_arquivo)

f.close()

print('Informações do arquivo criado')
print (dados_arquivo)

# Criar dados com numeros

dados = [1.6, 3.4, 5.5, 9.4]

f = open("dadosExemplo2Criar.txt", "x")
"Escreve os dados no arquivo criado"

for valor in dados:

    grava = str(valor)
    f.write(grava)
    f.write("\n")

f.close()

