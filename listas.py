from collections import deque

def main():
    frutas = ['laranja', 'maça', 'pera', 'banana', 'kiwi', 'maça', 'banana']
    print("frutas = ['laranja', 'maça', 'pera', 'banana', 'kiwi', 'maça', 'banana'] #declaração")

    print("Conta bananas:", frutas.count('banana'))

    print("Indice de banana a partir de 4:", frutas.index('banana', 4))

    frutas.reverse()
    print("Inverso: ", frutas)

    frutas.append('uva')
    print("Adicionou uva: ", frutas)

    frutas.sort();
    print("Ordenado: ", frutas)

    print("Usando pop (pilha): ", frutas.pop())

    print("""
Agora usando da forma correta com collections
""")

    fila = deque(['Eric', 'Jonh', 'Michael']) #cria a fila
    print("fila = deque(['Eric', 'Jonh', 'Michael']) #cria a fila")

    fila.append("Terry")    #Terry entra na fila
    fila.append("Graham")   #Graham entra na fila

    print("Anda fila: ", fila.popleft())
    print("Anda fila: ", fila.popleft())
    print("Situação da fila: ", fila) 

    print("""
Compressão de listas
""")
    aoQuadrado = []
    for x in range(10):
        aoQuadrado.append(x ** 2)

    print("aoQuadrado =", aoQuadrado)
    print("")

    #mesma coisa anterior usando func lambda
    aoQuadrado = list(map(lambda x: x**2, range(10)))

    #ou ainda pode ser assim em compressão
    aoQuadrado = [x**2 for x in range(10)]
    print("aoQuadrado = [x**2 for x in range(10)]")
    print("aoQuadrado =", aoQuadrado)

    #usando if na expressão
    aoQuadrado = [x**2 for x in range(10) if x >= 4]
    print("aoQuadrado = [x**2 for x in range(10) if x >= 4]")
    print("aoQuadrado =", aoQuadrado)

    seq = [n for n in range(1,37)]
    print("seq = [n for n in range(1,37)]")
    print("seq =", seq)

    print("[x for x in seq if x % 2 == 0]")
    print("filtrado par:", [x for x in seq if x % 2 == 0])

    print("[x for x in seq if x in aoQuadrado])")
    print("filtrado aoQuadrado:", [x for x in seq if x in aoQuadrado])


    print("""
Instrução del diretamente para apagar sem retornar
""")

    a = [-1, 1, 66.25, 333, 333, 1234.5]
    print("a = [-1, 1, 66.25, 333, 333, 1234.5]")

    del a[0]
    print("del a[0]")
    print("a: ", a)

    del a[2:4]
    print("del a[2:4]")
    print("a: ", a)

    del a[:]
    print("del a[:]")
    print("a: ", a)


    print("""
Conjunto ou set
""")

    cesta = { 'maça', 'laranja', 'maça', 'pera', 'laranja', 'banana' }
    print("cesta = { 'maça', 'laranja', 'maça', 'pera', 'laranja', 'banana' }")
    print(cesta, "#conjunto não mantem duplicados")

    print("simples teste: 'laranja' in cesta", 'laranja' in cesta)

    a = set('abracadabra')
    b = set('alacazam')
    print("a = set('abracadabra')")
    print("b = set('alacazam')")
    print("a: ", a)
    print("b: ", b)

    print("letras em a mas não em b (a-b):", a - b)
    print("letras em a, b ou ambos (a | b):", a | b)
    print("letras am ambos a e b (a & b):", a & b)
    print("letras em a ou b mas não em ambos (a ^ b):", a ^ b)

    print("""
Dicionarios ou dict
""")
    tel = {'jack': 4098, 'sape': 4139}
    print("tel = {'jack': 4098, 'sape': 4139}")
    print("tel:", tel)

    print("tel jack:", tel['jack'])

    del tel["sape"]
    print("del tel['sape']")

    tel["irv"] = 4127
    print("tel['irv'] = 4127")

    print("tel:", tel)
    print("tel list:", list(tel))

    tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
    print("tel = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)]) #usando dict()")
    print("tel:", tel)

    tel = dict(sape=4139, guido=4127, jack=4098)
    print("tel = dict(sape=4139, guido=4127, jack=4098) #ou assim tambem")
    print("tel:", tel)

    print("usando for com retorno de .items()")
    for n, v in tel.items():
        print(n, v)

    print("listando com enumarate(lista)")
    for i, n in enumerate(cesta):
        print(i, n)

    print("percorre duas ou mais listas ao mesmo tempo com zip(l1, l2, ..)")
    situacao = ['madura', 'velha', 'podre', 'só por Deus', 'não vai usar']
    for f, n in zip(cesta, situacao):
        print(f, n)

if __name__ == '__main__':
  main()