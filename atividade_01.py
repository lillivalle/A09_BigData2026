def soma(x,y):
    s = x + y
    return s


def subtracao(x,y):
    w = x - y
    return w


def multiplicacao(x,y):
    m = x * y
    return m


def divisao(x,y):
    o = x / y
    return o


#Início da execução
num1 = int(input('\nDigite um número: '))
num2 = int(input('\nDigite outro número: '))

print('\n #### MENU DE OPÇÕES PARA AS OPERAÇÕES #### ')
print(30 * '=')

print(' [1] - Soma \n [2] - Subtração\n [3] - Multiplicação\n [4] - Divisão')
opcao = int(input('\nInforme a sua opção: '))

match opcao:
    case 1: 
        resultado = soma(num1, num2) #quando escolhe um caso específicio já exclui os outros casos, então por isso pode definir o 'resultado' como uma coisa só
    case 2:
        resultado = subtracao(num1, num2)
    case 3:
        resultado = multiplicacao(num1, num2)
    case 4:
        resultado = divisao(num1, num2)

print(f'\nO resultado da sua operação é {resultado}.')

