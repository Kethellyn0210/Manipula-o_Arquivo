def cadastrar_usuario(nome, email):
    with open("usuarios.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nome},{email}\n")
    print("Usuário cadastrado com sucesso!")
