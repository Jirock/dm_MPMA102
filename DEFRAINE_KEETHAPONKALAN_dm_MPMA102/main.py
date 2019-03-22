from decimal import Decimal


# Q3
def factorielle(n):
    """
    fonction récusirve
    :param n: entier naturel
    :return: factorielle de n
    """
    if n == 0:
        return n
    else:
        return n * factorielle(n - 1)


# Q4
def question4():
    N = 0
    S = 1 / ((2 * N + 3) * factorielle(N + 1))
    while S > 0.000001:
        N += 1
        S = 1 / ((2 * N + 3) * Decimal(factorielle(N + 1)))
    return N


print(question4())
