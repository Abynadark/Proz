def calculadora_interativa():
    while True:
        print("\nSelecione a operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        opcao = input("Digite o número da operação: ")

        if opcao == '0':
            print("Encerrando a calculadora. Até mais!")
            break

        if opcao not in ['1', '2', '3', '4']:
            print("Essa opção não existe.")
            continue

        while True:
            try:
                num1 = float(input("Digite o primeiro valor: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        while True:
            try:
                num2 = float(input("Digite o segundo valor: "))
                break
            except ValueError:
                print("Entrada inválida. Por favor, digite um número.")

        if opcao == '1':
            resultado = num1 + num2
            op_nome = "Soma"
        elif opcao == '2':
            resultado = num1 - num2
            op_nome = "Subtração"
        elif opcao == '3':
            resultado = num1 * num2
            op_nome = "Multiplicação"
        elif opcao == '4':
            if num2 == 0:
                print("Erro: Divisão por zero não é permitida.")
                continue
            resultado = num1 / num2
            op_nome = "Divisão"

        print(f"{op_nome} de {num1} e {num2} é: {resultado}")

calculadora_interativa()
