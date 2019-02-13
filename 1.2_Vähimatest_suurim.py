def vahimatest_suurim(maatriks):
    a = []
    for i in range(len(maatriks)):
        a.append(min(maatriks[i]))
    return max(a)

        