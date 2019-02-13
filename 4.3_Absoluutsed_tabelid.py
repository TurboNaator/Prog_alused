from copy import deepcopy

def absolutiseeri_tabel(tabel):
    for i in range(len(tabel)):
        for j in range(len(tabel[i])):
            if tabel[i][j] < 0:
                tabel[i][j] *= -1

def absoluutne_tabel(tabel):
    uus_tabel = deepcopy(tabel)
    for i in range(len(uus_tabel)):
        for j in range(len(uus_tabel[i])):
            if uus_tabel[i][j] < 0:
                uus_tabel[i][j] *= -1
    return uus_tabel
