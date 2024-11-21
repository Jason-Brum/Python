def delta(a, b, c):
    """
    Calcula o valor de delta utilizado no cálculo de raízes de polinômios de segundo grau.
 
    :param a: Valor do primeiro termo do polinômio.
    :param b: Valor do segundo termo do polinômio.
    :param c: Valor do termo independente do polinômio.
    :return: Retorna as raízes calculadas e um booleano, indicando se o cálculo foi bem-sucedido.
    """
    return b*b - 4*a*c