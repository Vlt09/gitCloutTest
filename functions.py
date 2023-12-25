def add_numbers(a, b):
    '''
    Cette fonction prend deux nombres en entrée et retourne leur somme.

    Args:
        a (int): Premier nombre.
        b (int): Deuxième nombre.

    Returns:
        int: Somme des deux nombres.
    '''
    return a + b

def factorial(n):
    '''
    Cette fonction calcule la factorielle d'un nombre donné.

    Args:
        n (int): Nombre pour lequel calculer la factorielle.

    Returns:
        int: Factorielle de n.
    '''
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

def is_even(number):
    '''
    Cette fonction vérifie si un nombre est pair.

    Args:
        number (int): Nombre à vérifier.

    Returns:
        bool: True si le nombre est pair, False sinon.
    '''
    return number % 2 == 0
