import random

def teste_de_escopo():
    def apenas_local():
        a = "valor local";
    def nao_local():
        nonlocal a
        a = "não local"
    def como_global():
        global a
        a = "agora global"

    a = "Testando a"
    apenas_local()
    print("Após função local:", a)
    nao_local()
    print("Após não local:", a)
    como_global()
    print("Após como global:", a)


class OriginalBase():
    def fazRandom(self):
        return random.randint(0, 999999)

class OriginalBase2():
    __privado = "não existe" #apenas uma convenção para 'esconder' 

    def nada(self):
        pass


class AClasse(OriginalBase, OriginalBase2):
    """Teste de uma classe simples"""
    j = 333

    def __init__(self, oValor):
        self.j = oValor;

    def ao_quadrado(self):
        return self.j ** 2


def testar_classe():
    obj = AClasse(333)
    print("obj = AClasse(333) #instancia a classe")
    
    print("obj.j:", obj.j)
    print("obj.ao_quadrado():", obj.ao_quadrado())
    print("Metodo herdado:", obj.fazRandom())




class Interacao:
    """Exemplo de classe que implementa um Iterator"""

    def __init__ (self, valor):
        self.valor = valor
        self.n = -1;
        self.tam = len(valor)

    def __iter__ (self):
        return self;
    
    def __next__ (self):
        self.n = self.n+1;
        if (self.n >= self.tam):
            raise StopIteration
        
        return self.valor[self.n]


def testar_classe_iterator():
    obj = Interacao(['teste', 'de', 'interacao'])

    for i in obj:
        print(i)


def main():
    while(True):
        ipt = input("""
1 - Testar escopo
2 - Testar classe básica
3 - Classe com Iterator
Qual opção (q para sair)?""")
        if ipt == "q":
            break
        elif ipt == "1":
            teste_de_escopo()
            print("Por fim, no aspecto global:", a)
        elif ipt == "2":
            testar_classe()
        elif ipt == "3":
            testar_classe_iterator()
        else:
            print("! Opção inválida, escolha novamente.")

if __name__ == '__main__':
  main()