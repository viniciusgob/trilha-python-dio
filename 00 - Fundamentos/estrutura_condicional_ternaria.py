saldo = 2000
saque = int(input("Informe o valor para saque: "))

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")
