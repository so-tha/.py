# Calculadora basica
primeiro = int(input('Informe um numero: '))
segundo = int(input('Informe um segundo numero: '))
operacao = input('Informe a operação: ')

def op(operacao):
    if (operacao == '+'):
        resul = primeiro + segundo
        print(resul)
    elif (operacao == '-'):
        resul = primeiro - segundo
        print(resul)
    elif (operacao == '*'):
        resul = primeiro * segundo
        print(resul)
    elif (operacao == '/'):
        resul = primeiro / segundo
        print(resul)
    else:
        print('Comando Invalido')

op(operacao)