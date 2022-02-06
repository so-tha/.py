#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua media
aluno = str(input('Informe o nome do aluno: '))
nota1 = int(input('Informe a primeira nota: '))
nota2 = int(input('Informe a segunda nota: '))
media = (nota1 + nota2)/2

def med(media):
    if media < 60:
        print('Nota igual a {} = Abaixo da média'.format(media))
    elif media <= 70:
        print('Nota igual a {} = Na media'.format(media))
    elif media >= 80 :
        print('Nota igual a {} = Acima da media'.format(media))


med(media)