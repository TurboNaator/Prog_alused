def on_alglopuline(rida):
    if len(rida) < 1:
        return 0
    if rida[0] > rida[-1]:
        return 1
    else:
        return 0

jarjend_ruudus = [[4, 3, 2], [-1, 0]]

alglopulisi = 0
for rida in jarjend_ruudus:
    alglopulisi += on_alglopuline(rida)

print("Alglõpulisi ridu on " + str(alglopulisi))
