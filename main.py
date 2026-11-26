produtos = ["Carne Moída", "Pão", "Macarrão"]

print(produtos)

produtos.append("Shampoo")
produtos.append("Sabonete")

print(produtos)

quantidade_produtos = len(produtos)

print("Lista de produtos:", produtos)

print("A quantidade total de produtos é:", quantidade_produtos)

print("Lista de produtos:")
for produto in produtos:
    print(produto)