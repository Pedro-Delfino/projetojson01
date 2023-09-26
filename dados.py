import json

nome_arquivo = "produtos.json"

def carregar_dados():
    try:
        with open(nome_arquivo, "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_dados(dados):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)

produtos = carregar_dados()

while True:
    print("Menu de Opções:")
    print("1. Inserir produto")
    print("2. Consultar produto")
    print("3. Consultar todos os produtos")
    print("4. Alterar preço")
    print("5. Aplicar acréscimo/desconto")
    print("6. Excluir produto")
    print("7. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        codigo = input("Código: ")
        if codigo not in produtos:
            produtos[codigo] = {
                "nome": input("Nome: "),
                "preco": float(input("Preço: ")),
                "quantidade": int(input("Quantidade: ")),
                "disponivel": True
            }
            salvar_dados(produtos)
        else:
            print("Código já existe!")

    elif escolha == "2":
        codigo = input("Código: ")
        produto = produtos.get(codigo)
        if produto:
            print(f"Nome: {produto['nome']}, Preço: {produto['preco']}, Quantidade: {produto['quantidade']}, Disponível: {produto['disponivel']}")
        else:
            print("Produto não encontrado!")

    elif escolha == "3":
        for codigo, produto in produtos.items():
            print(f"Código: {codigo}, Nome: {produto['nome']}, Preço: {produto['preco']}")
        else:
            print("Nao tem produtos cadastrados!")

    elif escolha == "4":
        codigo = input("Código: ")
        produto = produtos.get(codigo)
        if produto:
            produto["preco"] = float(input("Novo preço: "))
            salvar_dados(produtos)
        else:
            print("Produto não encontrado!")

    elif escolha == "5":
        percentual = float(input("Percentual de acréscimo/desconto: "))
        for produto in produtos.values():
            produto["preco"] *= 1 + percentual / 100
        salvar_dados(produtos)

    elif escolha == "6":
        codigo = input("Código do produto a ser excluído: ")
        if codigo in produtos:
            del produtos[codigo]
            salvar_dados(produtos)
        else:
            print("Produto não encontrado!")

    elif escolha == "7":
        salvar_dados(produtos)
        break
