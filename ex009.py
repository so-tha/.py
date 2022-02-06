#Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros
valor = int(input('Informe o valor: '))
op = int(input('>>>>>>>>>>>>>>>>>>>> Conversor <<<<<<<<<<<<<<<<<<< \n 1 - Converter para centimetros \n 2 - Converter para milimetros \n'))

def conversor(op):
    if(op == 1):
        cent = valor * 100
        print('{} metros = {} cm'.format(valor,cent))
    elif(op == 2):
        mili = valor * 1000
        print('{} metros = {} milimentros'.format(valor,mili))
    else:
        print('Comando Invalido')

conversor(op)