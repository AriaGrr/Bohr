# Turma 725, Equipe 1:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Paulo Andre de Oliveira Hirata, RA: 24.123.086-1
# Diogo Santos Linna, RA: 24.123.003-6
# Victor Merker Binda, RA:

# Bibliotecas
import math
from decimal import Decimal

# Variaveis globais
teste = Decimal(0) # Variável para testar se é a primeira vez que o programa é executado

# Função para limpar a tela do terminal
def clear_screen():
    print('\033[H\033[J')

# Menu principal
while True:
    clear_screen()

    if teste == Decimal(0):
        print('OEM: Ondas Eletromagnéticas com Python')
        print('Desenvolvedores: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo Santos Linna, Victor Merker Binda')
        # Melhorar a descrição do programa
        print('Descrição')
        #
        print('Pressione Enter para continuar...')
        input() 
        teste = Decimal(1)

    print('Opções:')
    print('1 - Teste')
    print('2 - Teste')
    print('3 - Teste')
    print('0 - Sair')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Teste')

    elif option == '2':
        print('Teste')

    elif option == '3':
        print('Limpando variáveis...')

    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')
