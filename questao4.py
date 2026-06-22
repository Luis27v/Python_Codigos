saldo_inicial = 500.00

while True:
    print("Saldo atual: R$", saldo_inicial)
    print("Escolha uma opção:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar saldo")
    print("4 - Encerrar")

    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor_deposito = float(input("Digite o valor a ser depositado: "))
        saldo_inicial += valor_deposito
        print("Depósito realizado com sucesso!")
    elif opcao == "2":
        valor_saque = float(input("Digite o valor a ser sacado: "))
        if valor_saque <= saldo_inicial:
            saldo_inicial -= valor_saque
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente para realizar o saque.")
    elif opcao == "3":
        print("Saldo atual: R$", saldo_inicial)
    elif opcao == "4":
        print("Encerrando o programa...")
        

        