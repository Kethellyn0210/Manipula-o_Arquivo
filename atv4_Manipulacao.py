try:
    with open("inexistente.txt", "r", encoding="utf-8") as arquivo:
        print(arquivo.read())
except FileNotFoundError:
    print("Arquivo não encontrado. Criando o arquivo agora...")
    with open("inexistente.txt", "w", encoding="utf-8") as arquivo:
        arquivo.write("Este arquivo foi criado pois não existia.\n")
