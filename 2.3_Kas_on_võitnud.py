def voitis_nurkademangu(bingo):  
    return bingo[0][0] == 'X' and bingo[0][-1] == 'X' and bingo[-1][0] == 'X' and bingo[-1][-1] == 'X'

    
def x_peadiagonaalil(bingo):
    a = 0
    for i in range(5):
        if bingo[i][i] == 'X':
            a += 1
    return a 

def x_korvaldiagonaalil(bingo):
    a =  0
    loendur = 5
    for i in range(5):
        loendur -= 1
        if bingo[i][loendur] == 'X':
            a += 1
    return a 

def voitis_diagonaalidemangu(bingo):
    return x_peadiagonaalil(bingo) == 5 and x_korvaldiagonaalil(bingo) == 5

def voitis_taismangu(bingo):
    a = 0
    for i in bingo:
        for j in i:
            if j == 'X':
                a += 1
    return a == 25
