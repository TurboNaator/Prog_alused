def kooslubajad(järjend):
    tulemus = (0,1)
    makssuurus = 0
    for i in range(len(järjend)-1):
        for j in range(i +1, len(järjend)):
            if len((järjend[i]) & (järjend[j])) > makssuurus:
                makssuurus = len((järjend[i]) & (järjend[j]))
                tulemus = (i,j)
    return tulemus