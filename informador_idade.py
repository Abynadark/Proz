def cadastro_usuario():
    nome = input("Digite seu nome completo: ")

    while True:
        try:
            ano_nasc = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))

            if 1922 <= ano_nasc <= 2021:
                idade = 2022 - ano_nasc
                print(f"\nOlá, {nome}! Em 2022 você tem ou terá {idade} anos.")
                break
            else:
                print("Ano inválido! Digite um ano entre 1922 e 2021.")

        except ValueError:
            print("Entrada inválida! Digite apenas números.")

cadastro_usuario()
