
matrixD = [
    [1,2,3],
    [4,5,6]
]
matrixE = [
    [7,8],
    [9,10],
    [11,12]
]
matrixF = [
    [3,4,2]
]
matrixA = [
    [3,4,5]
    ]
matrixG = [
    [13,9,7,15],
    [8,7,4,6],
    [6,4,0,3]
]


def print2dMatrix(matrix):
    for i in matrix:
        print(i)


def matrixPrintWithSpaces(matrix):
    for i in range(0, len(matrix)):
        item_in_matrix = ""
        for j in range(0, len(matrix[i])):
            item_in_matrix = str(item_in_matrix) + " " + str(matrix[i][j])
        print(item_in_matrix)


def addMatrices(m1, m2):
    m3 = m1
    if len(m1) == len(m2):
        for row in range(0, len(m1)):
            print(str(m1[row]) + " + " + str(m2[row]))
            for num in range(0, len(m1)):
                m3[row][num] = m1[row][num] + m2[row][num]
            if row == len(m1) - 1:
                print("= ")
        for row in m3:
            print(row)
        return m3
    else:
        print("Please use a valid matrix")
        


def multiplyMatrices(m1,m2):
    m3=[]
    if len(m1[0]) != len(m2):
        print("Calc not possible")
    else:
        for i in range(0, len(m1)):
            m3.append([])
            for j in range(0, len(m2[0])):
                m3[i].append(0)
                for k in range(0, len(m1[0])):
                    m3[i][j] += m1[i][k] * m2[k][j]
        print(m3)
        return m3
