#Pedir um número ao usuário, exibir um menu de opções e calcular apenas a operação escolhida (dobro, triplo, quadrado ou metade) usando funções e a estrutura match/case

# o "def" é a palavra-chave utilizada para definir funções, 
# enquanto o "for" é um loop de interação/repetição
# "Match/case" Avalia a opção escolhida pelo usuário e chama apenas a função correspondente, salvando o retorno na variável 'resultado'

from auxiliar.operacoes import dobro, triplo, quadrado, metade
import random # 'random' vem de aleatório
import os
# def dobro(n): #aqui só recebe o parâmetro
#     d = n * 2
#     return d


# def triplo(n):
#     t = n * 3
#     return t


# def quadrado(n):
#     q = n **2
#     return q


# def metade(n):
#     m = n / 2
#     return m

#Início da execução
os.system('cls')
#num1 = int(input('\nDigite um número: '))
num1 = random.randint(1,50)
print(f'O número aleatório sorteado é: {num1}')


print('\n #### MENU DE OPÇÕES ####')
print(30 * '=')

print('[1] - Dobro\n[2] - Triplo\n[3] - Quadrado\n[4] - Metade')
opcao = int(input('\nInforme a sua opção: '))

match opcao:
    case 1: 
        resultado = dobro(num1) #quando escolhe um caso específicio já exclui os outros casos, então por isso pode definir o 'resultado' como uma coisa só
    case 2:
        resultado = triplo(num1)
    case 3:
        resultado = quadrado(num1)
    case 4:
        resultado = metade(num1)

print(f'\n O resultado da operação deu: {resultado:.2f}')

# resultado_dobro = dobro(num1)   #para comentar tudo seleciona e colocar ctrl + ;
# resultado_triplo = triplo(num1)
# resultado_quadrado = quadrado(num1)

# print(f'O resultado do dobro de {num1} é: {resultado_dobro}')
# print(f'O resultado do triplo de {num1} é: {resultado_triplo}')
# print(f'O resultado do quadrado de {num1} é: {resultado_quadrado}')