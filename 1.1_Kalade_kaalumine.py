def kala_kaal (pikkus, fti):
    return round((pikkus)**3 * (fti) / 100)

failinimi = input("Sisestage failinimi: ")
alamõõt = input("Sisestage püügi alamõõt: ")
fulton = input("Sisestage Fultoni tüsedusindeks: ")

kala_pikkus = []
f = open(failinimi, encoding="UTF-8")
for rida in f:
    kala_pikkus += rida

tegelik_kaal=0
    
for i in kala_pikkus:
    if int(i) < int(alamõõt):
        print("Kala lasti vette tagasi")
    else:
        tegelik_kaal = kala_kaal(int(i), float(fulton))
        print("Püütud kala kaaluga " + str(round(tegelik_kaal)) + " grammi")
 