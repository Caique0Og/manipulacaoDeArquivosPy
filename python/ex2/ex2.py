
##Exercício 2: Manipulação de Arquivos CSV
##Escreva um programa que crie um arquivo CSV chamado alunos.csv, com as colunas "Nome" e "Idade".
##O programa deve inserir os dados de três alunos e, em seguida, 
# #ler o arquivo e exibir os dados no console.

# colunas = ['Nome', 'Idade']

# linhas = [['Giovana', 24], ['sihyeon', 25],['beomgyu', 23]]

# import csv


# with open('alunos.csv', 'w', newline='',
# encoding='utf-8') as arquivo_csv:
#     escritor = csv.writer(arquivo_csv, delimiter=';')
#     escritor.writerow(colunas)
#     escritor.writerows(linhas)



with open('alunos.csv', 'r') as f:
    print(f.read())

# f = open('mensagens.txt', 'w')
# f.write('')
# f.close()