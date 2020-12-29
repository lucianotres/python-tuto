def main():
    a, b = 0, 1            #definição multipla em uma linha apenas
    while a < 10:          #faz enquanto menor que 10
        print(a, end=',')  #mostra valor de a, troca o final de nova linha para ,
        a, b = b, a+b      #atribui a = b e b = a+b (neste exemplo a ja tem valor de b anteior para somar a b atual e retorna em b)

if __name__ == '__main__':
  main()