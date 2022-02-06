# Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada
import math

num = int(input('Informe um numero: '))
op = int(input('Deseja saber: \n 1 - Dobro do numero \n 2 - Triplo do numero \n 3 - Raiz Quadrada \n'))


def dtr(op):
    if op == 1:
        resultado = num * 2
        print('Dobro do numero é igual a {}'.format(resultado))
    elif op == 2:
        resultado = num * 3
        print('O Triplo do numero é igual a {}'.format(resultado))
    elif op == 3:
        resultado = math.sqrt(num)
        print('A raiz quadrada do numero é igual a {}'.format(resultado))
    else:
        print('Comando Invalido')


dtr(op)
