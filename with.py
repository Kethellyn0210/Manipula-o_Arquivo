nome = input("Digite o nome: ")
email = input("Digite o e-mail: ")

with open("cadastro.txt", "w") as arquivo:
    arquivo.write(nome + " | " + email + "\n")