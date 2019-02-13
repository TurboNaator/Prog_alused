def paarissumma(n):
    if n == 0:
        return 0
    if n % 2 != 0:
        return paarissumma(n-1)
    else:
        return n + paarissumma(n-2)