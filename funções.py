import pandas as pd
from datetime import datetime
import os

arquivo_excel = "gastos.xlsx"

def salvar_dados(dados):
    dados.to_excel(arquivo_excel, index=False)

def carregar_dados():
    if os.path.exists(arquivo_excel):
        return pd.read_excel(arquivo_excel)
    else:
        return pd.DataFrame(columns=["Data", "Categoria", "Valor"])

def adicionar_gasto():
    valor = input("Digite o valor: ")
    try:
        gasto = float(valor)
        if gasto < 0:
            print("O valor não pode ser negativo.")
            return
    except ValueError:
        print("Valor inválido.")
        return

    data = input("Digite a data deste gasto (dd/mm/aaaa): ")
    try:
        datetime.strptime(data, "%d/%m/%Y")
    except ValueError:
        print("Data inválida. Use o formato dd/mm/aaaa.")
        return

    categoria = input("Digite a categoria (ex: Transporte, Alimentação): ")

    df = carregar_dados()
    novo_gasto = {"Data": data, "Categoria": categoria, "Valor": float(valor)}
    df = pd.concat([df, pd.DataFrame([novo_gasto])], ignore_index=True)
    salvar_dados(df)
    print("Gasto adicionado com sucesso, na planilha!")

def listar_gastos():
    df = carregar_dados()
    if df.empty:
        print("Nenhum gasto encontrado.")
    else:
        print("Lista de gastos:")
        print(df.to_string(index=False))
