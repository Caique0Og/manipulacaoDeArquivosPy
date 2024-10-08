##Exercício 1: Manipulação de Arquivos de Texto Simples
##Crie um programa em Python que escreva cinco frases em um arquivo de texto chamado mensagens.txt.
##Em seguida, leia e exiba o conteúdo do arquivo.


f = open('mensagens.txt', 'w')
f.write('Olá Mundo!\n')
f.write('Olá Mundo1!\n')
f.write('Olá Mundo2!\n')
f.write('Olá Mundo3!\n')
f.write('Olá Mundo5!\n')
f.close()


with open('mensagens.txt', 'r') as f:
    print(f.read())