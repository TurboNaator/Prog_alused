def kontroll(sisu):
    if kastid_korras(sisu) == True and ridade_kontroll(sisu) == True and veerud_korras(sisu) == True:
        return 'OK'
    else:
        return 'VIGA'
    
def kastid_korras(sisu):
    
    for rea_nurk in range(0, 9, 3):
        for veeru_nurk in range(0, 9, 3):
            
            kast = []
            for i in range(3):
                for j in range(3):
                    kast.append(int(sisu[rea_nurk + i][veeru_nurk + j]))
            
            if sorted(kast) != list(range(1, 10)):
                return False
    return True

def ridade_kontroll(sisu):
    for i in range(9):
        if sorted(sisu[i]) != list(range(1, 10)):
            return False
    return True


def veerud_korras(sisu):
    sum0 = 0
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    sum7 = 0
    sum8 = 0
    for i in range(9):
        sum0 += sisu[i][0]
        sum1 += sisu[i][1]
        sum2 += sisu[i][2]
        sum3 += sisu[i][3]
        sum4 += sisu[i][4]
        sum5 += sisu[i][5]
        sum6 += sisu[i][6]
        sum7 += sisu[i][7]
        sum8 += sisu[i][8]
    if sum0 == 45 and sum1 == 45 and sum2 == 45 and sum3 == 45 and sum4 == 45 and sum5 == 45 and sum6 == 45 and sum7 == 45 and sum8 == 45:
        return True
    else:
        return False


filename = input('Sisestage failinimi: ')

fail = open(filename, encoding="UTF-8")
maatriks = []

for rida in fail:
    maatriks.append(rida.split())

fail.close()

for i in range(9):
    for j in range(9):
        maatriks[i][j] = int(maatriks[i][j])

print(kontroll(maatriks))



