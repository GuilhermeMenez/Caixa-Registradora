from functools import reduce

precos = []
inicio = 1


def soma(x, y):
    return x + y


def caixa_registradira():
    valor_final = reduce(soma, precos)
    print(valor_final)
    valor_recebido = int(input("digite o valor pago pelo cliente\n"))
    troco = valor_final - valor_recebido
    print(troco)
    receber_produtos()


def receber_produtos():
    preco_produto = int(input("digite o preço do produto\n"))
    encerrar = int(input(" digite 0 para encerrar, e 1 para continuar\n"))
    precos.append(preco_produto)
    if encerrar == 0:
        return 0


while inicio != 0:
    receber_produtos()
    if receber_produtos() == 0:
        inicio = 0
        caixa_registradira()
