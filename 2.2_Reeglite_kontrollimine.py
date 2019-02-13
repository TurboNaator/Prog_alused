def on_bingo_tabel(loto):
    a = 0
    for i in range(len(loto)):
        if 1 <= loto[i][0] <= 15:
            a += 1
        if 16 <= loto[i][1] <= 30:
            a += 1
        if 31 <= loto[i][2] <= 45:
            a += 1
        if 46 <= loto[i][3] <= 60:
            a += 1
        if 61 <= loto[i][4] <= 75:
            a += 1
    if a == 25:
        return True
    else:
        return False