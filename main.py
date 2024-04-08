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

# Constantes
h = Decimal(6.62607015 * 10 ** -34) # Constante de Planck em J.s

# Variaveis
n = Decimal(0) # Número quântico
eF = Decimal(0) # Energia do fóton absorvido/emitido
f = Decimal(0) # Frequência do fóton absorvido/emitido
lF = Decimal (0) # Comprimento de onda (lambda) do fóton absorvido/emitido
r = Decimal (0) # Raio da órbita
v = Decimal (0) # Velocidade
K = Decimal (0) # Energia cinética
U = Decimal (0) # Energia potencial
E = Decimal (0) # Energia total
lE = Decimal (0) # Comprimento de onda do elétron

# Função para limpar a tela do terminal
def clear_screen():
    print('\033[H\033[J')

# Limpa as variaveis
def limpar_variaveis():
    # Variaveis
    n = Decimal(0) # Número quântico (estado)
    eF = Decimal(0) # Energia do fóton absorvido/emitido
    f = Decimal(0) # Frequência do fóton absorvido/emitido
    lF = Decimal (0) # Comprimento de onda (lambda) do fóton absorvido/emitido
    r = Decimal (0) # Raio da órbita
    v = Decimal (0) # Velocidade
    K = Decimal (0) # Energia cinética
    U = Decimal (0) # Energia potencial
    E = Decimal (0) # Energia total
    lE = Decimal (0) # Comprimento de onda do elétron

# Funções para cálculos

# Cálculo do raio da órbita
def raio_orbita():
    r = Decimal((n ** 2) * (h ** 2) / (4 * (math.pi ** 2) * 9.10938356 * (10 ** -31) * (9 * (10 ** 9))))
    return r

# Cálculo da velocidade
def velocidade():
    v = Decimal(2 * math.pi * (3 * (10 ** 8)) / lE)
    return v

# Cálculo do comprimento de onda do fóton
def comprimento_onda_eletron():
    lE = Decimal(h / (9.10938356 * (10 ** -31) * v))
    return lE

# Cálculo da energia cinética
def energia_cinetica():
    K = Decimal((1 / 2) * (9.10938356 * (10 ** -31)) * (v ** 2))
    return K

# Cálculo da energia potencial
def energia_potencial():
    U = Decimal(-1 * (9 * (10 ** 9)) * (1.60217662 * (10 ** -19)) / r)
    return U

# Cálculo da energia total
def energia_total():
    E = Decimal(K + U)
    return E

# Funções para opções do menu de calculos
def opcao1():
    global n, eF, f, lF, r, v, K, U, E, lE

def opcao2():
    global n, eF, f, lF, r, v, K, U, E, lE

def opcao3():
# mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE

def opcao4():
# mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE

def opcao5():
# Retorna E em [J] e [eV].
    global n, eF, f, lF, r, v, K, U, E, lE

def opcao6():
# Entrada E em [J] ou [eV].
    global n, eF, f, lF, r, v, K, U, E, lE

# Função para o menu de equações
def menu():
    global n, eF, f, lF, r, v, K, U, E, lE
    clear_screen()
    print('Opções de entradas:')
    # 
    print('1 - n:')
    print('Retorna r, v, lE, K, U, E.')
    # 
    print('2 - n inicial e final:')
    print('Retorna eF, f e lF.')
    # 
    print('3 - n inicial ou final + f ou lF (absorvido):')
    print('Retorna n final ou n inicial.')
    # 
    print('4 - n inicial ou final + f ou lF (emitido):')
    print('Retorna n final ou n inicial.')
    # 
    print('5 - f ou lF:')
    print('Retorna E.')
    # 
    print('6 - E:')
    print('Retorna f e lF.')

    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        opcao1()
        limpar_variaveis()

    elif option == '2':
        print('Opção 2 selecionada...')
        opcao2()
        limpar_variaveis()

    elif option == '3':
        print('Opção 3 selecionada...')
        opcao3()
        limpar_variaveis()

    elif option == '4':
        print('Opção 4 selecionada...')
        opcao4()
        limpar_variaveis()

    elif option == '5':
        print('Opção 5 selecionada...')
        opcao5()
        limpar_variaveis()

    elif option == '6':
        print('Opção 6 selecionada...')
        opcao6()
        limpar_variaveis()

    elif option == '0':
        clear_screen()
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    menu()

# Menu principal
while True:
    clear_screen()

    if teste == Decimal(0):
        print('O átomo de Bohr e quantização com Python')
        print('Desenvolvedores: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo Santos Linna, Victor Merker Binda')
        # Melhorar a descrição do programa
        print('Descrição')
        #
        print('Pressione Enter para continuar...')
        input() 
        teste = Decimal(1)

    print('Opções:')
    print('1 - Cálculos')
    print('2 - Limpar variáveis')
    print('0 - Sair')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Redirecionando para o menu de cálculos...')
        menu()

    elif option == '2':
        print('Limpando variáveis...')
        limpar_variaveis()

    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')
