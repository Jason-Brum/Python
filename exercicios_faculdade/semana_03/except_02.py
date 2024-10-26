try:
    num = int(input("Digite um número: "))
except ValueError:
    print("Valor inválido")
except:
    print("Outro tipo de erro ocorreu!")
