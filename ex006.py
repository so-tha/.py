# Faça um programa que leia um numero inteiro e mostre na tela o seu sucessor e seu atencessor
num = int(input('Informe um numero: '))
op = int(input('Informe a opção: \n 1 - Antecessor \n 2 - Sucessor \n'))


def antsus(op):
    if op == 1:
        ant = num - 1
        print('O antecessor do numero é {}'.format(ant))
    elif op == 2:
        sus = num + 1
        print('O sucessor do numero é igual a {}'.format(sus))
    else:
        print('Comando Invalido!')


antsus(op)
