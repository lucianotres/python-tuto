def main():
  '''Operações básicas com numeros e strings'''
  
  print("")
  print("Operação com números")
  print("")

  print("a = 2 + 2")
  a = 2 + 2
  print(a)
  
  print("a = 5 / 2 #sempre retorna floating number")
  a = 5 / 2
  print(a)

  print("a = 5 // 2 #divisao inteira")
  a = 5 // 2
  print(a)

  print("a = 5 // 2 #resto divisao")
  a = 5 % 2
  print(a)

  print("a = 2 ** 4 #potencia")
  a = 2 ** 4
  print(a)

  print("")
  print("Operação com texto")
  print("")

  print("a = 'texto' #string pode ser assim")
  print('a = "texto" #ou ainda assim')
  a = "texto"
  print(a)

  print("a = \"tex\\\"to\" #suporte escaped characters normalmente com \\")
  a = "tex\"to"
  print(a)

  print("""a = \"\"\"texto de
mais de uma linha\"\"\" #basta colocar em aspas triplas""")
  a = """texto de
mais de uma linha"""
  print(a)

  print("a = \"re\" * 3 #repde a string n vezes");
  a = "re" * 3
  print(a)

  print("a = \"re\" \"nata\" #strings em sequencia são concatenadas")
  a = "re" "nata"
  print(a)

  print("a = \"palavra\"")
  a = "palavra"
  print("a[0] #primeiro caracter")
  print(a[0])  
  print("a[-1] #ultimo caracter")
  print(a[-1])
  print("a[-2] #penultimo caracter")
  print(a[-2])
  print("a[3:5] #a partir do quarto caracter ate quinto caracter (zero indexed)")
  print(a[3:5])
  print("a[:2] #primeiros dois caracteres")
  print(a[:2])
  print("a[2:] #pula dois caracteres")
  print(a[2:])
  print("a[-2:] #ultimos dois caracteres")
  print(a[-2:])
  print("len(a) #tamanho da string")
  print(len(a))


  print("")
  print("Listas")
  print("Semelhante as strings, logo")
  print("letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g'] #declara uma lista")
  letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
  print(letras)

  print("letras[0] #primeiro")
  print(letras[0])
  print("letras[-1] #ultimo")
  print(letras[-1])
  print("letras[:] #copia direta")
  print(letras[:])
  print("letras[-3:] #tres ultimos")
  print(letras[-3:])
  print("letras = letras + ['h', 'i'] #concatena listas")
  letras = letras + ['h', 'i']
  print(letras)
  print("letras.append('j') #adiciona ao fim da lista")
  letras.append('j')
  print(letras)
  print("letras[2:5] = ['C', 'D', 'E'] #substitui o trecho")
  letras[2:5] = ['C', 'D', 'E']
  print(letras)
  print("letras[2:5] = [] #remove o trecho")
  letras[2:5] = []
  print(letras)
  print("letras[:] = [] #limpa a lista inteira")
  letras[:] = []
  print(letras)

if __name__ == '__main__':
  main()