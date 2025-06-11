frutas = input("Digite o nome da fruta: ")

with open("frutas.txt", "w") as arquivo:
    arquivo.write(frutas +"\n")