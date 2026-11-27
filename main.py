produtos = ["Mouse", "Teclado", "Monitor", "Headset", "WebCam"]

print("Lista atual:", produtos)

produto_remover = input("Digite o nome do produto que deseja remover: ")
if produto_remover in produtos:
    produtos.remove(produto_remover)
    print(f"O produto '{produto_remover}' foi removido com sucesso!")
else:
    print(f"O produto '{produto_remover}' não foi encontrado na lista.")

    print("\n--- Lista Atualizada ---")
    print(produtos)