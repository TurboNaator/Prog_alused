from random import shuffle

def juhuslik_bingo():
    matrix = [ [ None for i in range(5) ] for j in range(5) ]
    column1 = [i for i in range(1,16)]
    column2 = [i for i in range(16,31)]
    column3 = [i for i in range(31,46)]
    column4 = [i for i in range(46,61)]
    column5 = [i for i in range(61,76)]

    shuffle(column1)
    shuffle(column2)
    shuffle(column3)
    shuffle(column4)
    shuffle(column5)

    for i in range(5):
        matrix[i][0] = (column1[i])
        matrix[i][1] = (column2[i])
        matrix[i][2] = (column3[i])
        matrix[i][3] = (column4[i])
        matrix[i][4] = (column5[i])

    return(matrix)
