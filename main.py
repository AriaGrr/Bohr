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
#ow = 0 # Variável para armazenar a opção escolhida no menu de conversores  

# Constantes
h = 6.62607015 * 10 ** -34 # Constante de Planck em J.s
mE = 9.10938356 * 10 ** -31 # Massa do elétron em kg
hev=4.136*10**-15
c=3*10**8
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
E_foton=Decimal(0)
Freq_foton=Decimal(0)
Lamb_foton=Decimal(0)

num = Decimal(0) # Número 
num_c = Decimal(0) # Número convertido 1
num_c2 = Decimal(0) # Número convertido 2

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
    num_c2 = Decimal(0) # Número convertido

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

# Conversor de nm -> metros
def nm_metros(num):
    num_c = num / 1e9
    return num_c

# Conversor de metros -> cm
def metros_cm(num):
    num_c = num * 100
    return num_c

# Conversor de cm -> metros
def cm_metros(num):
    num_c = num / 100
    return num_c

# Conversor de metros -> km
def metros_km(num):
    num_c = num / 1000
    return num_c

# Conversor de km -> metros
def km_metros(num):
    num_c = num * 1000
    return num_c

# Conversor de metros -> mm
def metros_mm(num):
    num_c = num * 1000
    return num_c

# Conversor de mm -> metros
def mm_metros(num):
    num_c = num / 1000
    return num_c

# Conversor de metros -> um
def metros_um(num):
    num_c = num * 1e6
    return num_c

# Conversor de um -> metros
def um_metros(num):
    num_c = num / 1e6
    return num_c

# Conversor de metros -> pm
def metros_pm(num):
    num_c = num * 1e12
    return num_c

# Conversor de pm -> metros
def pm_metros(num):
    num_c = num / 1e12
    return num_c

# Conversor de eV -> J
def eV_J(num):
    num_c = num * 1.60217662 * (10 ** -19)
    return num_c

# Conversor de J -> eV
def J_eV(num):
    num_c = num / 1.60217662 * (10 ** -19)
    return num_c

# Conversor de eV -> cal
def eV_cal(num):
    num_c = num * 2.3900573613767 * (10 ** 20)
    return num_c

def E_foton_calc(ni,nf):
    ei=(-13.6/ni**2)
    ef=(-13.6/nf**2)
    E_foton=ef-ei
    return E_foton
def lamb_foton_calc(E_foton):
    Lamb_foton=hev*c/E_foton
    return Lamb_foton
def Freq_foton_calc(E_foton):
    Freq_foton=E_foton/hev
    return Freq_foton


# Opções do menu de conversores imbutido

# def conversores2(y):
#     global num_c, r, v, K, U, E, lE, lF, f, eF, ow, num

#     valor = y
#     print('Digite a saida desejada: ')
#     print (y)
#     if y == r or y == v or y == lE:
#         print('1 - cm')
#         print('2 - nm')
#         print('3 - km')
#         print('4 - mm')
#         print('5 - um')
#         print('6 - pm')
#         output = input()
#         if output == '1':
#             print ('Opção 1 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '2':
#             print ('Opção 2 selecionada...')
#             metros_nm(num)
#             print(f'{num:.4g} m = {num_c:.4g} nm')
#         elif output == '3':
#             print ('Opção 3 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '4':
#             print ('Opção 4 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '5':
#             print ('Opção 5 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '6':
#             print ('Opção 6 selecionada...')
#                 # Colocar logicas de conversão
#         else:
#             print('Opção inválida. Escolha uma opção válida.')

#     elif num == K or num == U or num == E:
#         print('1 - eV')
#         print('2 - J')
#         print('3 - cal')
#         print('4 - kcal')
#         print('5 - BTU')
#         print('6 - kWh')
#         print('7 - Wh')

#         output = input()
#         if output == '1':
#             print ('Opção 1 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '2':
#             print ('Opção 2 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '3':
#             print ('Opção 3 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '4':
#             print ('Opção 4 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '5':
#             print ('Opção 5 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '6':
#             print ('Opção 6 selecionada...')
#                 # Colocar logicas de conversão
#         elif output == '7':
#             print ('Opção 7 selecionada...')
#                 # Colocar logicas de conversão

# def conversores(y):
#     global ow, num, num_c, r, v, K, U, E, lE, lF, f, eF

#     print('Deseja fazer uma conversão? (S/N)')
#     op = input()

#     if op == 'S' or 's':
#         ow = 1
#     if ow == 1:
#         print('Escolha o valor que deseja converter: ')
#         x = input()
#         if y == 1:
#             if x == 1:
#                 conversores2(r)
#                 ow = 0
#                 conversores(1)
#             elif x == 2:
#                 conversores2(v)
#                 ow = 0
#                 conversores(1)
#             elif x == 3:
#                 conversores2(K)
#                 ow = 0
#                 conversores(1)
#             elif x == 4:
#                 conversores2(U)
#                 ow = 0
#                 conversores(1)
#             elif x == 5:
#                 conversores2(E)
#                 ow = 0
#                 conversores(1)
#             elif x == 6:
#                 conversores2(lE)
#                 ow = 0
#                 conversores(1)
        
#         else:
#             print('Opção inválida. Escolha uma opção válida.')

#     else:
#         input('Pressione Enter para continuar...')
        
# def escolhas1():
#     print('Digite o número da opção que deseja converter: ')
#     option = input()
#     if option == '1':
#         print('Opção 1 selecionada...')
#         conversores(r)

#     elif option == '2':
#         print('Opção 2 selecionada...')
#         conversores(v)

#     elif option == '3':
#         print('Opção 3 selecionada...')
#         conversores(K)

#     elif option == '4':
#         print('Opção 4 selecionada...')
#         conversores(U)

#     elif option == '5':
#         print('Opção 5 selecionada...')
#         conversores(E)

#     elif option == '6':
#         print('Opção 6 selecionada...')
#         conversores(lE)

#     else:
#         print('Opção inválida. Escolha uma opção válida.')

def conversor1():
    global num, num_c, num_c2
    a = ''
    b = ''

    print('Digite o número que deseja converter: ')
    num = float(input())
    print('Digite a unidade de medida do número: ')
    # Correto
    print('1 - m')
    #
    print('2 - cm')
    #
    print('3 - nm')
    #
    print('4 - km')
    #
    print('5 - mm')
    #
    print('6 - um')
    #
    print('7 - pm')
    entrada = input('Escolha uma opção: ')
    print (entrada)
    if entrada == '1':
        num_c = num
    elif entrada == '2':
        num_c = cm_metros(num)
    elif entrada == '3':
        num_c = nm_metros(num)
    elif entrada == '4':
        num_c = km_metros(num)
    elif entrada == '5':
        num_c = mm_metros(num)
    elif entrada == '6':
        num_c = um_metros(num)
    elif entrada == '7':
        num_c = pm_metros(num)

    print (num_c)
    
    if entrada == '1':
        a = 'm'
    elif entrada == '2':
        a = 'cm'
    elif entrada == '3':
        a = 'nm'
    elif entrada == '4':
        a = 'km'
    elif entrada == '5':
        a = 'mm'
    elif entrada == '6':
        a = 'um'
    elif entrada == '7':
        a = 'pm'

    print('Digite a unidade de medida desejada: ')
    #
    print('1 - m')
    #
    print('2 - cm')
    # Correto
    print('3 - nm')
    #
    print('4 - km')
    #
    print('5 - mm')
    #
    print('6 - um')
    #
    print('7 - pm')
    saida = input('Escolha uma opção: ')
    if saida == '1':
        num_c2 = num_c
    elif saida == '2':
        num_c2 = metros_cm(num_c)
    elif saida == '3':
        num_c2 = metros_nm(num_c)
    elif saida == '4':
        num_c2 = metros_km(num_c)
    elif saida == '5':
        num_c2 = metros_mm(num_c)
    elif saida == '6':
        num_c2 = metros_um(num_c)
    elif saida == '7':
        num_c2 = metros_pm(num_c)
    else:
        print('Opção inválida. Escolha uma opção válida.')
    
    if saida == '1':
        b = 'm'
    elif saida == '2':
        b = 'cm'
    elif saida == '3':
        b = 'nm'
    elif saida == '4':
        b = 'km'
    elif saida == '5':
        b = 'mm'
    elif saida == '6':
        b = 'um'
    elif saida == '7':
        b = 'pm'

    print(f'Entrada: {num} {a}')
    print(f'Saída: {num_c2} {b}')
    # Precisa de unidades de

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

    # conversores(1)
    
    input('Pressione Enter para continuar...')
    limpar_variaveis()
    menu()

        

# Entrada: n inicial e final ; Saida: eF, f e lF.
def opcao2():
    global n, eF, f, lF, r, v, K, U, E, lE,E_foton,Freq_foton,Lamb_foton
    print('Digite o número quântico inicial (ni): ')
    ni = int(input())
    print('Digite o número quântico final (nf): ')
    nf = int(input())
    E_foton_calc(ni,nf)
    lamb_foton_calc(E_foton)
    Freq_foton_calc(E_foton)
    
    print('Energia do fóton (eF):', E_foton, 'eV')
    print('Frequência do fóton (f):', Freq_foton, 'Hz')
    print('Comprimento de onda (lambda) do Fóton (lF):', Lamb_foton, 'm')


# Entrada: n inicial ou final + f ou lF (absorvido) ; Saida: n final ou n inicial.
def opcao3():
    # Mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE
    print('Opções de entradas:')
    # Retorna n final
    print("selecione o n que o exercicio oferece e a lambida/frequencia(emitido): ")
    print('1 - n final + f') 
    print('2 - n final + lF ')
    # Retorna n inicial
    print('3 - n inicial + f')
    print('4 - n inicial + lF')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        nf = float(input('Digite o número quântico final (nf)(): '))
        freq_foton = float(input('Digite a frequência (f) em Hz: '))
        Ei = -13.6/nf ** 2 + hev * freq_foton
        print(f"Ei: {Ei:.3f} eV")
        ni = round((-13.6/Ei) ** 0.5)
        print('Número quântico inicial (ni):', ni)
    elif option == '2':
        print('Opção 2 selecionada...')
        nf = float(input('Digite o número quântico final (nf): '))
        lamb_foton = float(input("Digite o comprimento de onda do fóton em m: "))
        Ei = (-13.6/nf ** 2) + ((hev*c) / lamb_foton)
        print(f"Ei: {Ei:.3f} eV")
        ni = round((-13.6/Ei) ** 0.5)                        
        print('Número quântico inicial (ni):', ni)
    elif option == '3':
        print('Opção 3 selecionada...')
        ni = float(input('Digite o número quântico inicial (ni): '))
        freq_foton = float(input("Digite a frequência do fóton em Hz: "))
        Ef = -13.6/ni ** 2 - hev * freq_foton
        print(f"Ef: {Ef:.3f} eV")
        nf = round((-13.6/Ef) ** 0.5)
        print('Número quântico final (nf):', nf)
    elif option == '4':
        print('Opção 4 selecionada...')
        ni = float(input('Digite o número quântico final (ni): '))
        lamb_foton = float(input("Digite o comprimento de onda do fóton em m: "))
        Ef = (-13.6/ni ** 2) - ((hev*c) / lamb_foton)
        print(f"Ef: {Ef:.3f} eV")
        nf = round((-13.6/Ef) ** 0.5)                        
        print('Número quântico inicial (nf):', nf)
    
        


# Entrada: n inicial ou final + f ou lF (emitido) ; Saida: n final ou n inicial.
def opcao4():
    # Mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE
    print("selecione o n que a questão deseja achar (absorve)")
    print('1 - n final + f') 
    print('2 - n final + lF ')
    # Retorna n inicial
    print('3 - n inicial + f')
    print('4 - n inicial + lF')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        n = float(input('Digite o número quântico final (n)(): '))
        freq_foton = float(input('Digite a frequência (f) em Hz: '))
        Ei = -13.6/n ** 2 + hev * freq_foton
        print(f"Ei: {Ei:.3f} eV")
        nf = round((-13.6/Ei) ** 0.5)
        print('Número quântico inicial (nf):', nf)
    elif option == '2':
        print('Opção 2 selecionada...')
        n = float(input('Digite o número quântico final (n): '))
        lamb_foton = float(input("Digite o comprimento de onda do fóton em m: "))
        Ei = (-13.6/n ** 2) + ((hev*c) / lamb_foton)
        print(f"Ei: {Ei:.3f} eV")
        nf = round((-13.6/Ei) ** 0.5)                        
        print('Número quântico inicial (nf):', nf)
    elif option == '3':
        print('Opção 3 selecionada...')
        nf = float(input('Digite o número quântico inicial (nf): '))
        freq_foton = float(input("Digite a frequência do fóton em Hz: "))
        Ef = -13.6/nf ** 2 - hev * freq_foton
        print(f"Ef: {Ef:.3f} eV")
        ni = round((-13.6/Ef) ** 0.5)
        print('Número quântico final (ni):', ni)
    elif option == '4':
        print('Opção 4 selecionada...')
        nf = float(input('Digite o número quântico final (nf): '))
        lamb_foton = float(input("Digite o comprimento de onda do fóton em m: "))
        Ef = (-13.6/nf ** 2) - ((hev*c) / lamb_foton)
        print(f"Ef: {Ef:.3f} eV")
        ni = round((-13.6/Ef) ** 0.5)                        
        print('Número quântico inicial (ni):', ni)
    input('Pressione Enter para continuar...')
    menu()

# Função opcao_5: Trata tanto a conversão de f ou lambda para E, quanto de E para f e lambda
def opcao_5():
  global E_foton, Freq_foton, Lamb_foton
  print("Escolha o tipo de cálculo:")
  print(
      "1 - Dada a frequência (f) ou comprimento de onda (λ) do fóton, calcular a energia (E) do fóton."
  )
  print(
      "2 - Dada a energia (E) do fóton, calcular a frequência (f) e o comprimento de onda (λ) do fóton."
  )
  escolha = input("Digite sua opção (1 ou 2): ")

  if escolha == '1':
    sub_escolha = input(
        "Digite 'f' para frequência ou 'lambda' para comprimento de onda: ")
    if sub_escolha == 'f':
      Freq_foton = float(input("Digite a frequência do fóton em Hz: "))
      E_foton = h * Freq_foton  # E = hf
    elif sub_escolha == 'lambda':
      Lamb_foton = float(
          input("Digite o comprimento de onda do fóton em metros: "))
      E_foton = (h * c) / Lamb_foton  # E = hc/λ
    else:
      print("Opção inválida.")
      return
    # Mostra os resultados em Joules e em eV
    E_foton_eV = E_foton / eV_J(1)
    print(f"Energia do fóton: {E_foton:.3e} J ou {E_foton_eV:.3e} eV")

  elif escolha == '2':
    E_foton = float(input("Digite a energia do fóton em elétron-volts (eV): "))
    Freq_foton = E_foton / hev  # f = E/h, novamente usando hev
    Lamb_foton = (hev * c) / E_foton  # λ = c/f, calculando diretamente em eV
    print(f"Frequência do fóton: {Freq_foton:.3e} Hz")
    print(f"Comprimento de onda do fóton: {Lamb_foton:.3e} m")

  else:
    print("Opção inválida.")


# Menus 

# Função para o menu de conversores
def menu_conversores():
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
        conversor1()
        limpar_variaveis()

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
        input('Pressione Enter para continuar...')

    else:
        print('Opção inválida. Escolha uma opção válida.')


# Function to call the menu
def menu():
  global n, eF, f, lF, r, v, K, U, E, lE
  clear_screen()
  print('Opções de cálculo:')
  print('1 - Dados n: Calcular r, v, lE, K, U, E')
  print('2 - Dados n inicial e n final: Calcular eF, f e lF')
  print('3 - Dados n inicial/final e f/lF (emitido): Calcular n final/inicial')
  print(
      '4 - Dados n inicial/final e f/lF (absorvido): Calcular n final/inicial')
  print('5 - Calcular energia ou f/lF do fóton dado f/lF ou energia')
  print('0 - Voltar/Sair')

  option = input('Escolha uma opção: ')

  if option == '1':
    opcao1()
  elif option == '2':
    opcao2()
  elif option == '3':
    opcao3()
  elif option == '4':
    opcao4()
  elif option == '5':
    opcao_5()
  elif option == '0':
    clear_screen()
    return
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

  input('Pressione Enter para continuar...')
  menu()

# Menu principal
while True:
    clear_screen()

    if teste == Decimal(0):
        print('O átomo de Bohr e quantização com Python')
        print('Desenvolvedores: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo Santos Linna, Victor Merker Binda')
        print('O programa "Átomo de Bohr" simula o comportamento de elétrons em átomos de Bohr, permitindo calcular diversas propriedades físicas como velocidade do elétron, energia do fóton, raio da órbita, energia cinética, potencial e total. O programa se baseia no modelo de átomo de Bohr, que descreve o átomo como um sistema de elétrons que orbitam um núcleo atômico. O modelo assume que os elétrons só podem se mover em órbitas circulares com raios específicos e quantizados. A energia de cada órbita é também quantizada, o que significa que os elétrons só podem ter certos valores de energia.')#Dizer caso queiram alguma modificação no texto.
        print('Funcionalidades:')
        print('/n Cálculo de diversas propriedades físicas do átomo de Bohr')
        print('/n Conversão de unidades')
        print('/n Interface amigável e fácil de usar')
        print('/n Limitações:')
        print('/n O modelo de Bohr é um modelo simplificado e não leva em consideração todos os aspectos da estrutura atômica.')
        print('/n O programa pode apresentar resultados imprecisos para alguns átomos e para alguns cálculos.:')
        # Opinar e se necessario modificar a descrição
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
        menu_conversores()

    elif option == '3':
        print('Limpando variáveis...')
        limpar_variaveis()

    elif option == '0':
        break
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')

print('Finalizando...')
