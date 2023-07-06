def sacar(valor):
    saldo = 500

    if saldo >= valor:
        print("valor sacado!")
        print("retire o seu dinheiro na boca do caixa.")

    if saldo <= valor:
        print("saldo insulficiente!")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")

sacar(1000)


def depositar(valor):
    saldo = 500
    saldo += valor

    if saldo is not valor:
        print("Deposito efetuado com sucesso!")

depositar(500)
