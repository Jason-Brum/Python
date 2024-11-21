def fatorial(numero):
    """
    Calcula o fatorial de um número inteiro de forma recursiva.

    Parâmetros:
        numero (int): O número inteiro para o qual o fatorial será calculado. 
                      Deve ser maior ou igual a zero.

    Retorno:
        int: O fatorial do número, se o número for não-negativo.
        str: Mensagem de erro, se o número for negativo.

    Observações:
        - O fatorial de 0 é 1 (0! = 1).
        - O fatorial de um número negativo não é definido matematicamente.

    Exemplos:
        >>> fatorial(5)
        120

        >>> fatorial(0)
        1

        >>> fatorial(-1)
        'Fatorial não é definido para números negativos.'
    """
    if numero < 0:
        return "Fatorial não é definido para números negativos."
    elif numero == 0 or numero == 1:
        return 1
    else:
        return numero * fatorial(numero - 1)

# Exemplo de uso
numero = int(input("Digite um número para calcular seu fatorial: "))
resultado = fatorial(numero)
print(f"O fatorial de {numero} é: {resultado}")