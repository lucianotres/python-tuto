import json


def main():
    """Irá testar algumas operações com escrita e leitura arquivos."""

    nome = input("Nome do arquivo teste:")
    with open(nome, 'w') as f:
        for n in range(1, 11):
            f.write("linha {}\n".format(n))

    print("Arquivo salvo!")
    print("Lendo arquivo direto..")

    with open(nome) as f:
        print(f.read())

    print("Lendo linhas uma a uma..")
    with open(nome) as f:
        for l in f:
            print(l, end="")


    print("""
Agora vamos escrever um Json e ler o mesmo na sequência
""")

    lista = [1, 'lista', 'simples']
    print("lista = [1, 'lista', 'simples']")

    with open('teste.json', 'w') as f:
        json.dump(lista, f)

    print("json.dump(lista, f) #onde f é um arquivo aberto para escrita")
    print("outra = json.load(f) #le do arquivo para objeto")

    with open('teste.json') as f:
        outra = json.load(f)
        print(outra)

if __name__ == '__main__':
  main()