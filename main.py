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
ow = 0 # Variável para armazenar a opção escolhida no menu de conversores  

# Constantes
h = 6.62607015 * 10 ** -34 # Constante de Planck em J.s
mE = 9.10938356 * 10 ** -31 # Massa do elétron em kg

# Variaveis
n = Decimal(0) # Número quântico
ni = Decimal(0) # Número quântico inicial
nf = Decimal(0) # Número quântico final
eF = Decimal(0) # Energia do fóton absorvido/emitido
f = Decimal(0) # Frequência do fóton absorvido/emitido
lF = Decimal (0) # Comprimento de onda (lambda) do fóton absorvido/emitido
r = Decimal (0) # Raio da órbita
v = Decimal (0) # Velocidade
K = Decimal (0) # Energia cinética
U = Decimal (0) # Energia potencial
E = Decimal (0) # Energia total
lE = Decimal (0) # Comprimento de onda do elétron

num = Decimal(0) # Número 
num_c = Decimal(0) # Número convertido

# Função para limpar a tela do terminal
def clear_screen():
    print('\033[H\033[J')

# Limpa as variaveis
def limpar_variaveis():
    # Variaveis
    n = Decimal(0) # Número quântico (estado)
    ni = Decimal(0) # Número quântico inicial
    nf = Decimal(0) # Número quântico final
    eF = Decimal(0) # Energia do fóton absorvido/emitido
    f = Decimal(0) # Frequência do fóton absorvido/emitido
    lF = Decimal (0) # Comprimento de onda (lambda) do fóton absorvido/emitido
    r = Decimal (0) # Raio da órbita
    v = Decimal (0) # Velocidade
    K = Decimal (0) # Energia cinética
    U = Decimal (0) # Energia potencial
    E = Decimal (0) # Energia total
    lE = Decimal (0) # Comprimento de onda do elétron
    num = Decimal(0) # Número 
    num_c = Decimal(0) # Número convertido

# Funções para cálculos

# Cálculo do raio da órbita (m)
def raio_orbita():
    #r = Decimal((n ** 2) * (h ** 2) / (4 * (math.pi ** 2) * 9.10938356 * (10 ** -31) * (9 * (10 ** 9))))
    r = (n ** 2) * 5.29 * (10 ** -11)
    return r

# Cálculo da velocidade (m/s)
def velocidade():
    #v = Decimal(2 * math.pi * (3 * (10 ** 8)) / lE)
    v = 2.187 * (10 ** 6) / n
    return v

# Cálculo do comprimento de onda De Broglie do elétron (m)
def comprimento_onda_eletron():
    #lE = Decimal(h / (9.10938356 * (10 ** -31) * v))
    #lE = Decimal(5,29 * (10 ** -11) / n)
    lE = h / (mE * v)
    return lE

# Cálculo da energia cinética (eV)
def energia_cinetica():
    #K = Decimal((1 / 2) * (9.10938356 * (10 ** -31)) * (v ** 2))
    K = +13.6 / n ** 2
    return K

# Cálculo da energia potencial (eV)
def energia_potencial():
    #U = Decimal(-1 * (9 * (10 ** 9)) * (1.60217662 * (10 ** -19)) / r)
    U = -27.2 / n ** 2
    return U

# Cálculo da energia total (eV)
def energia_total():
    #E = Decimal(K + U)
    E = -13.6 / (n ** 2)
    return E

# Funções para conversões
# Todos os conversores vão para uma unidade padrão e depois convertem para a unidade desejada

# Conversor de metros -> nm
def metros_nm(num):
    num_c = num * 1e9
    return num_c

# Opções do menu de conversores imbutido

def conversores(y):
    global num, num_c, ow

    print('Deseja fazer uma conversão? (S/N)')
    op = input()

    if op == 'S' or 's':
        ow = 1
    while ow == 1:
        ow = 0
        print('Escolha o valor que deseja converter: ')
        x = input()
        if y == 1:
            if x == 1:
                num == r
            elif x == 2:
                num == v
            elif x == 3:
                num == K
            elif x == 4:
                num == U
            elif x == 5:
                num == E
            elif x == 6:
                num == lE
        elif y == 2:
            if x == 1:
                num == 1
            elif x == 2:
                num == 1
            elif x == 3:
                num == 1
            elif x == 4:
                num == 1
            elif x == 5:
                num == 1
            elif x == 6:
                num == 1
            elif x == 7:
                num == 1
        elif y == 3:
            if x == 1:
                num == 1
            elif x == 2:
                num == 1
            elif x == 3:
                num == 1
            elif x == 4:
                num == 1
            elif x == 5:
                num == 1
            elif x == 6:
                num == 1
        elif y == 4:
            if x == 1:
                num == 1
            elif x == 2:
                num == 1
            elif x == 3:
                num == 1
            elif x == 4:
                num == 1
            elif x == 5:
                num == 1
            elif x == 6:
                num == 1
        elif y == 5:
            if x == 1:
                num == 1
            elif x == 2:
                num == 1
            elif x == 3:
                num == 1
            elif x == 4:
                num == 1
            elif x == 5:
                num == 1
            elif x == 6:
                num == 1
        elif y == 6:
            if x == 1:
                num == 1
        else:
            print('Opção inválida. Escolha uma opção válida.')
        print('Digite a saida desejada: ')
        if x == r or x == v or x == lE:
            print('1 - cm')
            print('2 - nm')
            print('3 - km')
            print('4 - mm')
            print('5 - um')
            print('6 - pm')
            output = input()
            if output == '1':
                print ('Opção 1 selecionada...')
                # Colocar logicas de conversão
            elif output == '2':
                print ('Opção 2 selecionada...')
                metros_nm(num)
                print(f'{num:.4g} m = {num_c:.4g} nm')
            elif output == '3':
                print ('Opção 3 selecionada...')
                # Colocar logicas de conversão
            elif output == '4':
                print ('Opção 4 selecionada...')
                # Colocar logicas de conversão
            elif output == '5':
                print ('Opção 5 selecionada...')
                # Colocar logicas de conversão
            elif output == '6':
                print ('Opção 6 selecionada...')
                # Colocar logicas de conversão
            else:
                print('Opção inválida. Escolha uma opção válida.')
            

        elif x == K or x == U or x == E:
            print('1 - eV')
            print('2 - J')
            print('3 - cal')
            print('4 - kcal')
            print('5 - BTU')
            print('6 - kWh')
            print('7 - Wh')

            output = input()
            if output == '1':
                print ('Opção 1 selecionada...')
                # Colocar logicas de conversão
            elif output == '2':
                print ('Opção 2 selecionada...')
                # Colocar logicas de conversão
            elif output == '3':
                print ('Opção 3 selecionada...')
                # Colocar logicas de conversão
            elif output == '4':
                print ('Opção 4 selecionada...')
                # Colocar logicas de conversão
            elif output == '5':
                print ('Opção 5 selecionada...')
                # Colocar logicas de conversão
            elif output == '6':
                print ('Opção 6 selecionada...')
                # Colocar logicas de conversão
            elif output == '7':
                print ('Opção 7 selecionada...')
                # Colocar logicas de conversão

        conversores(y)
        
    else:
        input('Pressione Enter para continuar...')
        
def escolhas1():
    print('Digite o número da opção que deseja converter: ')
    option = input()
    if option == '1':
        print('Opção 1 selecionada...')
        conversores(r)

    elif option == '2':
        print('Opção 2 selecionada...')
        conversores(v)

    elif option == '3':
        print('Opção 3 selecionada...')
        conversores(K)

    elif option == '4':
        print('Opção 4 selecionada...')
        conversores(U)

    elif option == '5':
        print('Opção 5 selecionada...')
        conversores(E)

    elif option == '6':
        print('Opção 6 selecionada...')
        conversores(lE)

    else:
        print('Opção inválida. Escolha uma opção válida.')

# Opções do menu de cálculos

# Entrada: n ; Saida: r, v, lE, K, U, E.
def opcao1():
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Digite o número quântico (n): ')
    n = float(input())
    r = raio_orbita()
    v = velocidade()
    K = energia_cinetica()
    U = energia_potencial()
    E = energia_total()
    lE = comprimento_onda_eletron()
    clear_screen()
    print('Entrada:')
    print(f'Número quântico (n): {n}')
    print('Saída:')
    print(f'1 - Raio da órbita (r): {r:.4g} m')
    print(f'2 - Velocidade (v): {v:.4g} m/s')
    print(f'3 - Energia cinética (K): {K:.4g} eV')
    print(f'4 - Energia potencial (U): {U:.4g} eV')
    print(f'5 - Energia total (E): {E:.4g} eV')
    print(f'6 - Comprimento de onda do elétron (lE): {lE:.4g} m')

    conversores(1)
    
    input('Pressione Enter para continuar...')
    limpar_variaveis()
    menu()

        

# Entrada: n inicial e final ; Saida: eF, f e lF.
def opcao2():
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Digite o número quântico inicial (ni): ')
    ni = Decimal(input())
    print('Digite o número quântico final (nf): ')
    nf = Decimal(input())
    eF = Decimal(13.6 * ((1 / (ni ** 2)) - (1 / (nf ** 2))))
    f = Decimal(eF / h)
    lF = Decimal(3 * (10 ** 8) / f)
    print('Energia do fóton (eF):', eF, 'eV')
    print('Frequência do fóton (f):', f, 'Hz')
    print('Comprimento de onda (lambda) do Fóton (lF):', lF, 'm')


# Entrada: n inicial ou final + f ou lF (absorvido) ; Saida: n final ou n inicial.
def opcao3():
    # Mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Opções de entradas:')
    # Retorna n final
    print('1 - n inicial + f') 
    print('2 - n inicial + lF (absorvido)')
    # Retorna n inicial
    print('3 - n final + f')
    print('4 - n final + lF (absorvido)')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        ni = Decimal(input('Digite o número quântico inicial (ni): '))
        f = Decimal(input('Digite a frequência (f) em Hz: '))
        nf = Decimal(ni + 1)
        print('Número quântico final (nf):', nf)
    elif option == '2':
        print('Opção 2 selecionada...')
        ni = Decimal(input('Digite o número quântico inicial (ni): '))
        lF = Decimal(input('Digite o comprimento de onda (lambda) do Fóton (lF) em m: '))
        nf = Decimal(ni + 1)
        print('Número quântico final (nf):', nf)
    elif option == '3':
        print('Opção 3 selecionada...')
        nf = Decimal(input('Digite o número quântico final (nf): '))
        f = Decimal(input('Digite a frequência (f) em Hz: '))
        ni = Decimal(nf - 1)
        print('Número quântico inicial (ni):', ni)
    elif option == '4':
        print('Opção 4 selecionada...')
        nf = Decimal(input('Digite o número quântico final (nf): '))
        lF = Decimal(input('Digite o comprimento de onda (lambda) do Fóton (lF) em m: '))
        ni = Decimal(nf - 1)
        print('Número quântico inicial (ni):', ni)


# Entrada: n inicial ou final + f ou lF (emitido) ; Saida: n final ou n inicial.
def opcao4():
    # Mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Opções de entradas:')
    print('1 - n inicial + f')
    print('2 - n inicial + lF (emitido)')
    print('3 - n final + f')
    print('4 - n final + lF (emitido)')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        ni = Decimal(input('Digite o número quântico inicial (ni): '))
        f = Decimal(input('Digite a frequência (f) em Hz: '))
        nf = Decimal(ni + 1)
        print('Número quântico final (nf):', nf)
    elif option == '2':
        print('Opção 2 selecionada...')
        ni = Decimal(input('Digite o número quântico inicial (ni): '))
        lF = Decimal(input('Digite o comprimento de onda (lambda) do Fóton (lF) em m: '))
        nf = Decimal(ni + 1)
        print('Número quântico final (nf):', nf)
    elif option == '3':
        print('Opção 3 selecionada...')
        nf = Decimal(input('Digite o número quântico final (nf): '))
        f = Decimal(input('Digite a frequência (f) em Hz: '))
        ni = Decimal(nf - 1)
        print('Número quântico inicial (ni):', ni)
    elif option == '4':
        print('Opção 4 selecionada...')
        nf = Decimal(input('Digite o número quântico final (nf): '))
        lF = Decimal(input('Digite o comprimento de onda (lambda) do Fóton (lF) em m: '))
        ni = Decimal(nf - 1)
        print('Número quântico inicial (ni):', ni)
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    menu()

# Entrada: f ou lF; Saida: E.
def opcao5():
    # Retorna E em [J] e [eV].
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Opções de entradas:')
    print('1 - Frequência (f)')
    print('2 - Comprimento de onda (lambda) do Fóton (lF)')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        # Corrigir a entrada
        f = Decimal(input('Digite a frequência (f) em Hz: '))
        lF = Decimal(3 * (10 ** 8) / f)
        E = Decimal(6.62607015 * (10 ** -34) * f)
        print('Comprimento de onda (lambda) do Fóton (lF):', lF, 'm')
        print('Energia do fóton (E):', E, 'J')
    elif option == '2':
        print('Opção 2 selecionada...')
        lF = Decimal(input('Digite o comprimento de onda (lambda) do Fóton (lF) em m: '))
        f = Decimal(3 * (10 ** 8) / lF)
        E = Decimal(6.62607015 * (10 ** -34) * f)
        print('Frequência (f):', f, 'Hz')
        print('Energia do fóton (E):', E, 'J')
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    menu()



# Entrada: E ; Saida: f e lF.
def opcao6():
    # Entrada E em [J] ou [eV].
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Digite a energia do fóton (E) em J: ')
    E = Decimal(input())
    f = Decimal(E / 6.62607015 * (10 ** -34))
    lF = Decimal(3 * (10 ** 8) / f)
    print('Frequência do fóton (f):', f, 'Hz')
    print('Comprimento de onda (lambda) do Fóton (lF):', lF, 'm')
    
    input('Pressione Enter para continuar...')
    menu()
    
# Menus 

# Função para o menu de conversores
def menu():
    global n, eF, f, lF, r, v, K, U, E, lE
    clear_screen()
    print('Opções de entradas:')
    # 
    print('1 - m / cm / nm / km / mm / um / pm')
    # 
    print('2 - eV / J / cal / kcal / BTU / kWh / Wh')
    # 
    print('3 - ')
    # 
    print('4 - ')
    # 
    print('5 - ')
    # 
    print('6 - ')

    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')

    elif option == '2':
        print('Opção 2 selecionada...')


    elif option == '3':
        print('Opção 3 selecionada...')


    elif option == '4':
        print('Opção 4 selecionada...')


    elif option == '5':
        print('Opção 5 selecionada...')


    elif option == '6':
        print('Opção 6 selecionada...')

    elif option == '0':
        clear_screen()
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    menu()

# Função para o menu de equações
def menu():
    global n, eF, f, lF, r, v, K, U, E, lE
    clear_screen()
    print('Opções de entradas:')
    # Correta
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
    print('2 - Conversores')
    print('3 - Limpar variáveis')
    print('0 - Sair')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Redirecionando para o menu de cálculos...')
        menu()

    elif option == '2':
        print('Redirecionando para o menu de conversores...')

    elif option == '3':
        print('Limpando variáveis...')
        limpar_variaveis()

    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')
