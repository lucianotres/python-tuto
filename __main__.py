import fluxo
import fibonacci_series as fib
import operacoes_basicas as ope
import listas
import arquivo
import excecoes
import classes

def main():
    n = -1
    while n < 0 or n > 6:
        n = int(input("""
0 - Operadores básicos
1 - Fibonacci series
2 - Fluxo
3 - Listas
4 - Arquivo
5 - Tratamento de exceções
6 - Class (Objetos)
O que quer executar? """))

    if n == 0:
        ope.main()
    elif n == 1:
        fib.main()
    elif n == 2:
        fluxo.main()
    elif n == 3:
        listas.main()
    elif n == 4:
        arquivo.main()
    elif n == 5:
        excecoes.main()
    elif n == 6:
        classes.main()
    
main()