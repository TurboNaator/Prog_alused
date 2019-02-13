def symbolite_sagedus(sõne):
    sagedused={}
    for symbol in sõne:
        if symbol not in sagedused:
            sagedused[symbol] = 0
        if symbol in sagedused:
            sagedused[symbol] += 1
    
    return sagadeused

