def failist_sonastik(file):
    sonastik = {}
    with open(file) as f:
        for row in f:
            (key, val) = row.split()
            sonastik[key] = val
    return sonastik

def tahised_nimedeks(riik, sona):
    nimekiri = []
    for values in riik: 
        nimekiri.append(sona.get(values,None))
    return nimekiri


filename = input('Sisesta andmebaasi faili nimi: ')
input_countries = input('Sisesta riikide tähised tühikute eraldatult: ')

riigid = []
riigid = input_countries.split()

for riik in tahised_nimedeks(riigid, failist_sonastik(filename)):
    if riik == None:
        print('Tundmatu maa')
    else:
        print(riik)
