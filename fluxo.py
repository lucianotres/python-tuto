def main():
    x = int(input("Entre com um numero inteiro: "))
    if x < 0:
      print("Número negativo")
    elif x == 0:
      print("Zero")
    elif x == 1:
      print("Um")
    else:
      print("Mais")

    print("""
Agora vamos ao for
""")
    palavras = ["gato", "janela", "outra"]
    for p in palavras:
      print(p, len(p))

    print("range(5)")
    for n in range(5):
      print(n)

    print("range(5, 10)")
    for n in range(5, 10):
      print(n)

    print("range(0, 10, 3)")
    for n in range(0, 10, 3):
      print(n)

    print("usando o indice")
    for n in range(len(palavras)):
      print(n, palavras[n])
    

    print("loop infinito, aguarda um ctrl+c")
    while True:
      pass

if __name__ == '__main__':
  main()