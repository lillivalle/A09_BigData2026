#Criar uma função e retornar o dobro, triplo e quadrado

# o "def" é a palavra-chave utilizada para definir funções, 
#enquanto o "for" é um loop de interação/repetição

def dobro(n): #aqui só recebe o parâmetro
    d = n * 2
    return d


def triplo(n):
    t = n * 3
    return t


def quadrado(n):
    q = n **2
    return q


num1 = int(input('\nDigite um número: '))

resultado_dobro = dobro(num1)
resultado_triplo = triplo(num1)
resultado_quadrado = quadrado(num1)

print(f'O resultado do dobro de {num1} é: {resultado_dobro}')
print(f'O resultado do triplo de {num1} é: {resultado_triplo}')
print(f'O resultado do quadrado de {num1} é: {resultado_quadrado}')