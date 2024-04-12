
# Turma 725, Equipe 1:
# Marjorie Luize Martins Costa, RA: 24223084-5
# Paulo Andre de Oliveira Hirata, RA: 24.123.086-1
# Diogo Santos Linna, RA: 24.123.003-6
# Victor Merker Binda, RA:

# Bibliotecas
import math
from decimal import Decimal

# Variaveis globais
teste = 0 # Variável para testar se é a primeira vez que o programa é executado
#ow = 0 # Variável para armazenar a opção escolhida no menu de conversores  

# Constantes
h = 6.62607015 * 10 ** -34 # Constante de Planck em J.s
h2 = 4.135667696 * 10 ** -15 # Constante de Planck em eV.s
mE = 9.10938356 * 10 ** -31 # Massa do elétron em kg
hev = 4.136*10**-15
c = 3*10**8

# Variaveis
n = 0 # Número quântico
ni = 0 # Número quântico inicial
nf = 0 # Número quântico final
eF = 0 # Energia do fóton absorvido/emitido (eV)
f = 0 # Frequência do fóton absorvido/emitido (Hz)
lF = 0 # Comprimento de onda (lambda) do fóton absorvido/emitido (m)
r = 0 # Raio da órbita (m)
v = 0 # Velocidade (m/s)
K = 0 # Energia cinética (eV)
U = 0 # Energia potencial (eV)
E = 0 # Energia total (eV)
lE = 0 # Comprimento de onda do elétron (m)


num = 0 # Número 
num_c = 0 # Número convertido 1
num_c2 = 0 # Número convertido 2

# Função para limpar a tela do terminal
def clear_screen():
    print('\033[H\033[J')

# Limpa as variaveis
def limpar_variaveis():
    # Variaveis
    n = 0 # Número quântico (estado)
    ni = 0 # Número quântico inicial
    nf = 0 # Número quântico final
    eF = 0 # Energia do fóton absorvido/emitido
    f = 0 # Frequência do fóton absorvido/emitido
    lF = 0 # Comprimento de onda (lambda) do fóton absorvido/emitido
    r = 0 # Raio da órbita
    v = 0 # Velocidade
    K = 0 # Energia cinética
    U = 0 # Energia potencial
    E = 0 # Energia total
    lE = 0 # Comprimento de onda do elétron
    num = 0 # Número 
    num_c = 0 # Número convertido
    num_c2 = 0 # Número convertido

# Funções para conversões
# Todos os conversores vão para uma unidade padrão e depois convertem para a unidade desejada

# Conversor de eV -> J
def eV_J(num):
    #num_c = num * 1.60217662 * (10 ** -19)
    # num_c = num * 1.602 * (10 ** -19)
    num_c = num * 1.6022e-19
    return num_c

# Conversor de J -> eV
def J_eV(num):
    #num_c = num / 1.60217662 * (10 ** -19)
    # num_c = num / 1.602 * (10 ** -19)
    num_c = num * 6.242e+18
    return num_c

# Conversor de eV -> cal
def eV_cal(num):
    num_c = num * 2.3900573613767 * (10 ** 20)
    return num_c

# Conversor de cal -> eV
def cal_eV(num):
    num_c = num / 2.3900573613767 * (10 ** 20)
    return num_c

# Conversor de eV -> kcal
def eV_kcal(num):
    num_c = num * 2.3900573613767 * (10 ** 17)
    return num_c

# Conversor de kcal -> eV
def kcal_eV(num):
    num_c = num / 2.3900573613767 * (10 ** 17)
    return num_c

# Conversor de eV -> BTU
def eV_Btu(num):
    num_c = num * 3.826733324 * (10 ** 19)
    return num_c

# Conversor de BTU -> eV
def Btu_eV(num):
    num_c = num / 3.826733324 * (10 ** 19)
    return num_c

# Conversor de eV -> kWh
def eV_kWh(num):
    num_c = num * 2.7777777777778 * (10 ** -7)
    return num_c

# Conversor de kWh -> eV
def kWh_eV(num):
    num_c = num / 2.7777777777778 * (10 ** -7)
    return num_c

# Conversor de eV -> Wh
def eV_Wh(num):
    num_c = num * 3.6 * (10 ** -6)
    return num_c

# Conversor de eV -> Wh
def Wh_eV(num):
    num_c = num / 3.6 * (10 ** -6)
    return num_c

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

# Conversor de Hz -> kHz
def Hz_kHz(num):
    num_c = num / 1e3
    return num_c

# Conversor de kHz -> Hz
def kHz_Hz(num):
    num_c = num * 1e3
    return num_c

# Conversor de Hz -> MHz
def Hz_MHz(num):
    num_c = num / 1e6
    return num_c

# Conversor de MHz -> Hz
def MHz_Hz(num):
    num_c = num * 1e6
    return num_c

# Conversor de Hz -> GHz
def Hz_GHz(num):
    num_c = num / 1e9
    return num_c

# Conversor de GHz -> Hz
def GHz_Hz(num):
    num_c = num * 1e9
    return num_c

# Conversor de Hz -> THz
def Hz_THz(num):
    num_c = num / 1e12
    return num_c

# Conversor de THz -> Hz
def THz_Hz(num):
    num_c = num * 1e12
    return num_c

# Funções para cálculos

# eF por h*c e lF
def eF_lF():
    eF = (h2 * c) / lF
    return eF

# eF por h e f
def eF_f():
    eF = h2 * f
    return eF

# Alternativa 1

# Cálculo do raio da órbita (m)
def raio_orbita():
    r = (n ** 2) * 5.29 * (10 ** -11)
    return r

# Cálculo da velocidade (m/s)
def velocidade():
    v = 2.187 * (10 ** 6) / n
    return v

# Cálculo do comprimento de onda De Broglie do elétron (m)
def comprimento_onda_eletron():
    lE = h / (mE * v)
    return lE

# Cálculo da energia cinética (eV)
def energia_cinetica():
    K = +13.6 / n ** 2
    return K

# Cálculo da energia potencial (eV)
def energia_potencial():
    U = -27.2 / n ** 2
    return U

# Cálculo da energia total (eV)
def energia_total():
    E = -13.6 / (n ** 2)
    return E

# Alternativa 2

# Cálculo ei do fóton (eV) pelo n inicial
def ei_foton():
    ei = -13.6 / ni ** 2
    return ei

# Cálculo ef do fóton (eV) pelo n final
def ef_foton():
    ef = -13.6 / nf ** 2
    return ef

# Cálculo da energia do fóton (eV)
def energia_foton():
    eF = ef_foton() - ei_foton()
    return eF

# Função para cálculo de f
def freq_foton():
    f = eF / hev
    return f

# Função para cálculo de lF
def lamb_foton():
    lF = hev * c / eF
    return lF

# Alternativa 3

# Ei pelo nf e lF
def Ei_lF():
    Ei = (-13.6 / nf ** 2) + ((hev * c) / lF)
    return Ei

# Ni pelo nf e lF
def n_inicial_lF():
    ni = (-13.6/Ei_lF()) ** 0.5
    return ni

# Cálculo do Ei pelo nf e f
def Ei_f():
    Ei = -13.6 / nf ** 2 + hev * f
    return Ei

# Cálculo do n inicial pelo n final e f
def n_inicial_f():
    ni = (-13.6/Ei_f()) ** 0.5
    return ni

# Função para cálculo de nf por lf
def E_final_lf():
    Ef = (-13.6 / ni ** 2) - ((hev * c) / lF)
    return Ef

# Função para cálculo de nf por lf
def n_final_lf():
    nf = (-13.6/E_final_lf()) ** 0.5
    return nf

# Função para cálculo de nf por f
def E_final_f():
    Ef = -13.6 / ni ** 2 - hev * f
    return Ef

# Função para cálculo de nf por f
def n_final_f():
    nf = (-13.6/E_final_f()) ** 0.5
    return nf

# Alternativa 4

# Ei pelo ni e f


# Opções menu de conversores 

def conversor1():
    global num, num_c, num_c2
    a = ''
    b = ''
    print('Digite a unidade de medida do número da entrada: ')
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
    print('Digite o número que deseja converter: ')
    num = float(input())
    #print (entrada)
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

    # print (num_c)
    
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

    clear_screen()
    print(f'Entrada: {num} {a}')
    print(f'Saída: {num_c2} {b}')
    print(f'Saida arredondada: {num_c2:.4g} {b}')

def conversor2():
    global num, num_c, num_c2
    a = ''
    b = ''
    print('Digite a unidade de medida do número da entrada: ')
    #
    print('1 - eV')
    #
    print('2 - J')
    #
    print('3 - cal')
    #
    print('4 - kcal')
    #
    print('5 - BTU')
    #
    print('6 - kWh')
    #
    print('7 - Wh')
    entrada = input('Escolha uma opção: ')
    print('Digite o número que deseja converter: ')
    num = float(input())

    if entrada == '1':
        num_c = num
    elif entrada == '2':
        num_c = J_eV(num)
    elif entrada == '3':
        num_c = cal_eV(num)
    elif entrada == '4':
        num_c = kcal_eV(num)
    elif entrada == '5':
        num_c = Btu_eV(num)
    elif entrada == '6':
        num_c = kWh_eV(num)
    elif entrada == '7':
        num_c = Wh_eV(num)

    # print (num_c)

    if entrada == '1':
        a = 'eV'
    elif entrada == '2':
        a = 'J'
    elif entrada == '3':
        a = 'cal'
    elif entrada == '4':
        a = 'kcal'
    elif entrada == '5':
        a = 'BTU'
    elif entrada == '6':
        a = 'kWh'
    elif entrada == '7':
        a = 'Wh'

    print('Digite a unidade de medida desejada: ')
    #
    print('1 - eV')
    #
    print('2 - J')
    #
    print('3 - cal')
    #
    print('4 - kcal')
    #
    print('5 - BTU')
    #
    print('6 - kWh')
    #
    print('7 - Wh')
    saida = input('Escolha uma opção: ')
    if saida == '1':
        num_c2 = num_c
    elif saida == '2':
        num_c2 = eV_J(num_c)
    elif saida == '3':
        num_c2 = eV_cal(num_c)
    elif saida == '4':
        num_c2 = eV_kcal(num_c)
    elif saida == '5':
        num_c2 = eV_Btu(num_c)
    elif saida == '6':
        num_c2 = eV_kWh(num_c)
    elif saida == '7':
        num_c2 = eV_Wh(num_c)
    else:
        print('Opção inválida. Escolha uma opção válida.')

    if saida == '1':
        b = 'eV'
    elif saida == '2':
        b = 'J'
    elif saida == '3':
        b = 'cal'
    elif saida == '4':
        b = 'kcal'
    elif saida == '5':
        b = 'BTU'
    elif saida == '6':
        b = 'kWh'
    elif saida == '7':
        b = 'Wh'

    clear_screen()
    print(f'Entrada: {num} {a}')
    print(f'Saída: {num_c2} {b}')
    print(f'Saida arredondada: {num_c2:.4g} {b}')

def conversor3():
    global num, num_c, num_c2
    a = ''
    b = ''
    print('Digite a unidade de medida do número da entrada: ')
    # 
    print('1 - Hz')
    #
    print('2 - kHz')
    #
    print('3 - MHz')
    #
    print('4 - GHz')
    #
    print('5 - THz')
    entrada = input('Escolha uma opção: ')
    print('Digite o número que deseja converter: ')
    num = float(input())

    if entrada == '1':
        num_c = num
    elif entrada == '2':
        num_c = kHz_Hz(num)
    elif entrada == '3':
        num_c = MHz_Hz(num)
    elif entrada == '4':
        num_c = GHz_Hz(num)
    elif entrada == '5':
        num_c = THz_Hz(num)

    # print (num_c)

    if entrada == '1':
        a = 'Hz'
    elif entrada == '2':
        a = 'kHz'
    elif entrada == '3':
        a = 'MHz'
    elif entrada == '4':
        a = 'GHz'
    elif entrada == '5':
        a = 'THz'

    print('Digite a unidade de medida desejada: ')
    #
    print('1 - Hz')
    #
    print('2 - kHz')
    #
    print('3 - MHz')
    #
    print('4 - GHz')
    #
    print('5 - THz')
    saida = input('Escolha uma opção: ')
    if saida == '1':
        num_c2 = num_c
    elif saida == '2':
        num_c2 = Hz_kHz(num_c)
    elif saida == '3':
        num_c2 = Hz_MHz(num_c)
    elif saida == '4':
        num_c2 = Hz_GHz(num_c)
    elif saida == '5':
        num_c2 = Hz_THz(num_c)
    else:
        print('Opção inválida. Escolha uma opção válida.')

    if saida == '1':
        b = 'Hz'
    elif saida == '2':
        b = 'kHz'
    elif saida == '3':
        b = 'MHz'
    elif saida == '4':
        b = 'GHz'
    elif saida == '5':
        b = 'THz'

    clear_screen()
    print(f'Entrada: {num} {a}')
    print(f'Saída: {num_c2} {b}')
    print(f'Saida arredondada: {num_c2:.4g} {b}')

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
    print(f'Raio da órbita (r): {r:.4g} m')
    print(f'Velocidade (v): {v:.4g} m/s')
    print(f'Energia cinética (K): {K:.4g} eV')
    print(f'Energia potencial (U): {U:.4g} eV')
    print(f'Energia total (E): {E:.4g} eV')
    print(f'Comprimento de onda do elétron (lE): {lE:.4g} m')
    input('Pressione Enter para continuar...')
    limpar_variaveis()

# Entrada: n inicial e final ; Saida: eF, f e lF.
def opcao2():
    global n, eF, f, lF, r, v, K, U, E, lE, ni, nf
    
    ni = int(input('Digite o número quântico inicial (ni): '))
    nf = int(input('Digite o número quântico final (nf): '))
    
    eF = energia_foton()
    f = freq_foton()
    lF = lamb_foton()
    
    clear_screen()
    print('Entrada:')
    print(f'Número quântico inicial (ni): {ni}')
    print(f'Número quântico final (nf): {nf}')
    print('Saída:')
    print(f'Energia do fóton (eF): {eF:.4g} eV')
    print(f'Comprimento de onda (lambda) do fóton (lF): {lF:.4g} m')
    print(f'Frequência do fóton (f): {f:.4g} Hz')
    input('Pressione Enter para continuar...')
    limpar_variaveis()
    
# Entrada: n inicial ou final + f ou lF (emitido) ; Saida: n final ou n inicial.
def opcao3():
    # Mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE, ni, nf
    print('Entradas (emite):')
    # Retorna n inicial
    print('1 - n final + f') 
    print('2 - n final + lF ')
    # Retorna n final
    print('3 - n inicial + f')
    print('4 - n inicial + lF')
    print('0 - Voltar')
    option = input('Escolha uma opção: ')
    # Testar
    if option == '1':
        print('Digite o número quântico final (nf): ')
        nf = float(input())
        f = float(input('Digite a frequência do fóton (f) em Hz: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico final (nf): {nf}')
        print(f'Frequência do fóton (f): {f} Hz')
        print('Saída:')
        ni = n_inicial_f()
        print ('Número quântico inicial (ni) completo:', ni)
        ni = Decimal(ni)
        ni = ni.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico inicial (ni) com duas casas: ', ni)
        ni = round(ni)
        print(f'Número quântico inicial (ni) inteiro: {ni}')
    # Testar
    elif option == '2':
        print('Digite o número quântico final (nf): ')
        nf = float(input())
        lF = float(input('Digite o comprimento de onda do fóton (lF) em m: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico final (nf): {nf}')
        print(f'Comprimento de onda do fóton (lF): {lF} m')
        print('Saída:')
        ni = n_inicial_lF()
        print ('Número quântico inicial (ni) completo:', ni)
        ni = Decimal(ni)
        ni = ni.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico inicial (ni) com duas casas: ', ni)
        ni = round(ni)
        print(f'Número quântico inicial (ni) inteiro: {ni}')
    # Testar
    elif option == '3':
        print('Digite o número quântico inicial (ni): ')
        ni = float(input())
        f = float(input('Digite a frequência do fóton (f) em Hz: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico inicial (ni): {ni}')
        print(f'Frequência do fóton (f): {f} Hz')
        print('Saída:')
        nf = n_final_f()
        print ('Número quântico final (nf) completo:', nf)
        nf = Decimal(nf)
        nf = nf.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico final (nf) com duas casas: ', nf)
        nf = round(nf)
        print(f'Número quântico final (nf) inteiro: {nf}')
    # Testar
    elif option == '4':
        print('Digite o número quântico inicial (ni): ')
        ni = float(input())
        lF = float(input('Digite o comprimento de onda do fóton (lF) em m: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico inicial (ni): {ni}')
        print(f'Comprimento de onda do fóton (lF): {lF} m')
        print('Saída:')
        nf = n_final_lf()
        print ('Número quântico final (nf) completo:', nf)
        nf = Decimal(nf)
        nf = nf.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico final (nf) com duas casas: ', nf)
        nf = round(nf)
        print(f'Número quântico final (nf) inteiro: {nf}')
    elif option == '0':
        clear_screen()
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')

    input('Pressione Enter para continuar...')
    limpar_variaveis()

# Entrada: n inicial ou final + f ou lF (absorvido) ; Saida: n final ou n inicial.
def opcao4():
    # Mostrar a resposta de duas formas: número com duas casas decimais e em forma de número inteiro
    global n, eF, f, lF, r, v, K, U, E, lE, ni, nf
    print('Entradas (absorve):')
    # Retorna n final
    print('1 - n inicial + f')
    print('2 - n inicial + lF')
    # Retorna n inicial
    print('3 - n final + f')
    print('4 - n final + lF')
    print('0 - Voltar')
    option = input('Escolha uma opção: ')
    # Testar
    if option == '1':
        print('Digite o número quântico inicial (ni): ')
        nf = float(input())
        f = float(input('Digite a frequência do fóton (f) em Hz: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico inicial (ni): {nf}')
        print(f'Frequência do fóton (f): {f} Hz')
        print('Saída:')
        ni = n_inicial_f()
        print ('Número quântico final (nf) completo:', ni)
        ni = Decimal(ni)
        ni = ni.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico final (nf) com duas casas: ', ni)
        ni = round(ni)
        print(f'Número quântico final (nf) inteiro: {ni}')
    # Testar
    elif option == '2':
        print('Digite o número quântico inicial (ni): ')
        nf = float(input())
        lF = float(input('Digite o comprimento de onda do fóton (lF) em m: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico inicial (ni): {nf}')
        print(f'Comprimento de onda do fóton (lF): {lF} m')
        print('Saída:')
        ni = n_inicial_lF()
        print ('Número quântico final (nf) completo:', ni)
        ni = Decimal(ni)
        ni = ni.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico final (nf) com duas casas: ', ni)
        ni = round(ni)
        print(f'Número quântico final (nf) inteiro: {ni}')
    # Testar
    elif option == '3':
        print('Digite o número quântico final (nf): ')
        ni = float(input())
        f = float(input('Digite a frequência do fóton (f) em Hz: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico final (nf): {ni}')
        print(f'Frequência do fóton (f): {f} Hz')
        print('Saída:')
        E = E_final_f()
        nf = n_final_f()
        print ('Número quântico inicial (ni) completo:', nf)
        nf = Decimal(nf)
        nf = nf.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico inicial (ni) com duas casas: ', nf)
        nf = round(nf)
        print(f'Número quântico inicial (ni) inteiro: {nf}')
    # Testar
    elif option == '4':
        print('Digite o número quântico final (nf)): ')
        ni = float(input())
        lF = float(input('Digite o comprimento de onda do fóton (lF) em m: '))
        clear_screen()
        print('Entrada:')
        print(f'Número quântico final (nf): {ni}')
        print(f'Comprimento de onda do fóton (lF): {lF} m')
        print('Saída:')
        nf = n_final_lf()
        print ('Número quântico inicial (ni) completo:', nf)
        nf = Decimal(nf)
        nf = nf.quantize(Decimal('0.01'))
        # Concertar a precisão
        print(f'Número quântico inicial (ni) com duas casas: ', nf)
        nf = round(nf)
        print(f'Número quântico inicial (ni) inteiro: {nf}')
    input('Pressione Enter para continuar...')
    limpar_variaveis()

# Entrada: ef (em eV ou J) ; Saida: f/lF.
def opcao5():
    global n, eF, f, lF, r, v, K, U, E, lE, num_c, num_c2
    print('Entrada eF em:')
    # Correto
    print('1 - eV')
    #
    print('2 - J')
    option = input('Escolha uma opção: ')
    if option == '1':
        eF = float(input('Digite a energia do fóton (eF) em eV: '))
    elif option == '2':
        eFJ = float(input('Digite a energia do fóton (eF) em J: '))
        eF = J_eV(eFJ)
    else:
        print('Opção inválida. Escolha uma opção válida.')
    f = freq_foton()
    lF = lamb_foton()
    clear_screen()
    print('Entrada:')
    if option == '1':
        print(f'Energia do fóton (eF): {eF:.4g} eV')
        num_c = J_eV(eF)
        print(f'Energia do fóton (eF): {num_c:.4g} J')
    elif option == '2':
        print(f'Energia do fóton (eF): {eFJ:.4g} J')
        print(f'Energia do fóton (eF): {eF:.4g} eV')
    print('Saída:')
    print(f'Frequência do fóton (f): {f:.4g} Hz')
    print(f'Comprimento de onda (lambda) do fóton (lF): {lF:.4g} m')

    input('Pressione Enter para continuar...')
    limpar_variaveis()

# Entrada: f ou lF ; Saida: ef (em eV e em J).
def opcao6():
    global n, eF, f, lF, r, v, K, U, E, lE, num_c, num_c2
    print('Entrada:')
    print('1 - Frequência do fóton (f) em Hz')
    print('2 - Comprimento de onda do fóton (lF) em m')
    print('0 - Voltar')
    option = input('Escolha uma opção: ')
    if option == '1':
        f = float(input('Digite a frequência do fóton (f) em Hz: '))
        eF = eF_f()
    elif option == '2':
        lF = float(input('Digite o comprimento de onda do fóton (lF) em m: '))
        f = freq_foton()
        eF = eF_lF()
    elif option == '0':
        clear_screen()
        return
    else:
        print('Opção inválida. Escolha uma opção válida.')
    clear_screen()
    print('Entrada:')
    if option == '1':
        print(f'Frequência do fóton (f): {f:.4g} Hz')
    elif option == '2':
        print(f'Comprimento de onda do fóton (lF): {lF:.4g} m')
        
    print('Saída:')
    num_c = eV_J(eF)
    print(f'Energia do fóton (eF): {num_c:.4g} J')
    print(f'Energia do fóton (eF): {eF:.4g} eV')

    input('Pressione Enter para continuar...')
    limpar_variaveis()

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
    print('3 - Hz / kHz / MHz / GHz / THz')

    print('0 - Voltar!')
    option = input('Escolha uma opção: ')

    if option == '1':
        print('Opção 1 selecionada...')
        conversor1()
        limpar_variaveis()

    elif option == '2':
        print('Opção 2 selecionada...')
        conversor2()
        limpar_variaveis()

    elif option == '3':
        print('Opção 3 selecionada...')
        conversor3()
        limpar_variaveis()

    elif option == '0':
        clear_screen()

    else:
        print('Opção inválida. Escolha uma opção válida.')
        

# Function to call the menu
def menu():
  global n, eF, f, lF, r, v, K, U, E, lE
  clear_screen()
  print('Opções de cálculo:')
  # Correto
  print('1 - Entrada n')
  print('Saida: r, v, lE, K, U, E')
  # Correto
  print('2 - Entrada n inicial e n final')
  print('Saida: eF, f, lF')
  # Correto
  print('3 - Entrada n inicial ou final + f ou lF (emitido)')
  # Corrigir
  print('Saida: n final ou inicial')
  print('4 - Entrada n inicial ou final + f ou lF (absorvido)')
  #
  print('Saida: n final ou inicial')
  print('5 - Entrada eF (em eV ou J)')
  print('Saida: f/lF')
  #
  print('6 - Entrada f ou lF')
  print('Saida: eF (em eV e em J)')
  print('0 - Voltar')

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
    opcao5()
  elif option == '6':
    opcao6()
  elif option == '0':
    clear_screen()
    return
  else:
    print("Opção inválida. Por favor, escolha uma opção válida.")

  menu()

# Menu principal
while True:
    clear_screen()

    if teste == 0:
        print('O átomo de Bohr e quantização com Python')
        print('Desenvolvedores: Marjorie Luize Martins Costa, Paulo Andre de Oliveira Hirata, Diogo Santos Linna, Victor Merker Binda')
        print(" ")
        print('O programa "Átomo de Bohr" simula o comportamento de elétrons em átomos de Bohr, permitindo calcular diversas propriedades físicas como velocidade do elétron, energia do fóton, raio da órbita, energia cinética, potencial e total. O programa se baseia no modelo de átomo de Bohr, que descreve o átomo como um sistema de elétrons que orbitam um núcleo atômico. O modelo assume que os elétrons só podem se mover em órbitas circulares com raios específicos e quantizados. A energia de cada órbita é também quantizada, o que significa que os elétrons só podem ter certos valores de energia.')

        print(" ")
        print('Funcionalidades:')
        print(" ")
        print('- Cálculo de diversas propriedades físicas do átomo de Bohr')
        print('- Conversão de unidades')
        print('- Interface amigável e fácil de usar')
        print(" ")
        print('Limitações:')
        print(" ")
        print('- O modelo de Bohr é um modelo simplificado e não leva em consideração todos os aspectos da estrutura atômica.')
        print('- O programa pode apresentar resultados imprecisos para alguns átomos e para alguns cálculos.:')
        print(" ")

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
