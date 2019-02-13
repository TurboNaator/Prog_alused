def kala_kaal(pikkus,fti):
    kaal = round((pikkus)**3 * (fti) / 100)
    return kaal

filename = input('Sisestage failinimi: ')
smallestLength = input('Sisestage püügi alammõõt: ')
fulton = input('Sisestage Fultoni tüsedusindeks: ')

#loeb faili
f = open(filename, encoding="UTF-8")
read = f.readlines()
input = []
#eemaldan realõpus reavahemärgi "\n"
for i in read:
    input.append(i.strip())
#sulgen faili
f.close()

#määran kala kaalu muutuja, et funktsiooni kord tsükli jooksul välja kutsuda
fishWeight = 0
#määran kala kaaldude järjendi et ülemõõdulised salvestada 
fishWeightList = []
for i in input:
    if int(i) < int(smallestLength):
        print('Kala lasti vette tagasi')
    else:
        fishWeight = kala_kaal(int(i),float(fulton))
        print('Püütud kala kaaluga', fishWeight, 'grammi')
        fishWeightList.append(fishWeight)
        
print('Kõige raskem püütud kala:', max(fishWeightList)/1000, 'kg')