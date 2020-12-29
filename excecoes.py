import sys

def outra():
    raise IOError

def main():
    while True:
        try:
            x = int(input("Digite um número: "))
            print("Agora foi, você digitou:", x)
            break;
        except ValueError:
            print("Eita! Errou ai né?! Digite um número válido na próxima..")


    print("""
Vamos para outro teste, agora com mais de um tipo de exception
""")
    try:
        f = open('teste.txt')
        s = f.readline()
        i = int(s.strip())
    except OSError as err:
        print("Erro do tipo OSError:", err)
    except ValueError:
        print("Texto não pode ser convertido para int!")
    except:
        print("Erro inesperado:", sys.exc_info()[0])
        raise
    else:
        f.close()
        print("Tudo de boas!")

    print("""
Cadeia de erros
""")
    try:
        try:
            outra()
        except IOError as exc:
            raise RuntimeError("Falou ao sei la!") from exc
    except Exception as e:
        print(e)
    finally:
        print("Encerrou por aqui")

if __name__ == '__main__':
  main()