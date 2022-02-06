#Faça um programa que leia algo pelo teclado e mostre na tela o
#seu tipo primitivo e todas as informações possíveis sobre ele.

inf = (input('Informe algo: '))
print('O tipo primitivo desse valor é:', type(inf))
print('Só possui espaços: ',inf.isspace())
print('É um numero: ',inf.isnumeric())
print('é alfabetico: ',inf.isalpha())
