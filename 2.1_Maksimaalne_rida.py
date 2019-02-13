
nimi = input('Sisestage failinimi: ')
fail = open(nimi, encoding="UTF-8")


ridade_summad = []
for rida in fail:
    rea_summa = 0
    osad = rida.split()
    for arv in osad:
        rea_summa += int(arv)
    ridade_summad.append(rea_summa)

maks_rida = 1
maks_rea_summa = ridade_summad[0]

for i in range(1, len(ridade_summad)):
    if ridade_summad[i] > maks_rea_summa:
        maks_rida = i + 1
        maks_rea_summa = ridade_summad[i]

print('Suurim summa on failis ' + str(maks_rida) + '. real ja see on ' + str(maks_rea_summa) + '.')

fail.close()