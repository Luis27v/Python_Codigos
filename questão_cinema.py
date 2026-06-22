while True:
    assentos_disponiveis = 30
    assentos_ocupados = 0
    print("Bem-vindo ao cinema!")
    print(1, " - reservar assento")
    print(2, " - cancelar reserva")
    print(3, " - mostrar assentos disponíveis")
    print(4, " - encerrar sistema")
    opcao = int(input("Digite a opção desejada: "))
    for i in range(1, 31):
         print("Assento", i, " - ", "Disponível" if i <= assentos_disponiveis else "Ocupado")
    if assentos_ocupados == 30:
        print("Desculpe, não há mais assentos disponíveis.")
        continue
    if opcao == 1:
        if assentos_disponiveis > 0:
            assentos_ocupados += 1
            assentos_disponiveis -= 1
            print("Assento reservado com sucesso!")
        else:
            print("Desculpe, não há mais assentos disponíveis.")
    elif opcao == 2:
        if assentos_ocupados > 0:
            assentos_ocupados -= 1
            assentos_disponiveis += 1
            print("Reserva cancelada com sucesso!")
        else:
            print("Não há reservas para cancelar.")
    elif opcao == 3:
        print("Assentos disponíveis:", assentos_disponiveis)
    elif opcao == 4:
        print("Sistema encerrado.")
        break
    else:
        print("Opção inválida. Por favor, digite um número entre 1 e 4.")
        
    
