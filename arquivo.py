
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


if __name__ == '__main__':
  main()