r'C:\nova-pasta\teste.txt'

f = open('teste.txt', 'w')
f.write('Olá !\n')
f.close()

# f = open('teste.txt', 'a')
# f.write('flamengo não é time !\n')
# f.close()

# f = open('teste.txt', 'a')
# f.write('time é vasco da gama !\n')
# f.close()

# f = open('teste.txt', 'a')
# f.write('flamengo é seleção !\n')
# f.close()

# with open('teste.txt', 'r') as f:
#     leitura1 = f.read() 

# with open('teste.txt', 'r') as f:
#     leitura = f.read()
#     leitura1 = f.read() 


with open('teste.txt', 'r') as f:
    print(f.read())