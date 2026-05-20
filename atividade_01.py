import random # 'random' vem de aleatório
import os # 'import' é a biblioteca, traz coisas
from auxiliar.operacoes_fundamentais import soma, subtracao, multiplicacao, divisao

# def soma(x,y):
#     s = x + y
#     return s
# #ou fazer assim: 
# #   return x + y    


# def subtracao(x,y):
#     w = x - y
#     return w
# #ou fazer assim:
# #   return a -b


# def multiplicacao(x,y):
#     m = x * y
#     return m
# #   return x * y


# def divisao(x,y):
#     if y == 0:
#         return 'Operação Inválida'
#     o = x / y
#     return o
# #   return x / y


#Início da execução
os.system('cls') # "os" é a biblioteca e um dos métodos que tem é o 'cls', que é a limpeza do terminal

# num1 = float(input('\nDigite um número: '))
# num2 = float(input('\nDigite outro número: '))

num1 = random.randint(11,100) # vai fazer o random randint que é o inteiro 
num2 = random.randint(1,10)
print(f'Primeiro número: {num1}')
print(f'Segundo número: {num2}')

while True:
    print('\n #### MENU DE OPÇÕES PARA AS OPERAÇÕES #### ')
    print(40 * '=')

    print(' [1] - Soma \n [2] - Subtração\n [3] - Multiplicação\n [4] - Divisão')
    opcao = int(input('\nInforme a sua opção: '))

    match opcao:
        case 1: 
            resultado = soma(num1, num2) #quando escolhe um caso específicio já exclui os outros casos, então por isso pode definir o 'resultado' como uma coisa só
            operacao = 'Soma'
            break
        case 2:
            resultado = subtracao(num1, num2)
            operacao = 'Subtração'
            break
        case 3:
            resultado = multiplicacao(num1, num2)
            operacao = 'Multiplicação'
            break
        case 4:
            resultado = divisao(num1, num2)
            operacao = 'Divisão'
            break
        case _: # O underline captura QUALQUER outra opção (5, 6, 99, etc.)
            print('\n[ERRO] Opção inválida! Por favor, escolha uma opção de 1 a 4.')
            # Como não tem 'break' aqui, o "while" recomeça do início do menu

print(f'\nO resultado da sua operação entre os números: {num1} e {num2} fazendo a operação de {operacao} fica: {resultado:.2f}.')

