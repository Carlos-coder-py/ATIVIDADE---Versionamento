from funções import adicionar_gasto, listar_gastos

def exibir_menu():
    print("1 - Adicionar gasto")
    print("2 - Listar gastos")
    print("3 - Sair")

while True:
    exibir_menu()
    opcao = input("Escolha uma das opções:")

    if opcao == "1":
        adicionar_gasto()
    elif opcao == "2":
        listar_gastos()
    elif opcao == "3":
        print("Saindo...")
        break
    else:
        print("Opção inválida. Tente novamente.")