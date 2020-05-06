# Joseph Wilson-Hall

def printMatrix(matrix):
    r = int(input("Enter number of rows: "))
    c = int(input("Enter number of columns: "))
    matrix = []  # Creates blank list 'Matrix'
    for i in range(0, r):  # Creates blank list for certain ammount of rows within the list
        matrix.append([])  # Appends 'r' number of blank lists to the matrix
    for i in range(0, r):  # 'i' = number of rowws
        for j in range(0, c):  # 'j' = number of columns
            matrix[i].append(j)  # In each row append 'c' number of elements, as c is number of columns
            matrix[i][j] = 0  # Creates 2d matrix of size r by c
    for i in range(0, r):
        for j in range(0, c):
            print('Enter number in row: ', i + 1, 'column: ', j + 1)
            matrix[i][j] = int(input())
    print(matrix)


matrixA = [[3, 8], [4, 6]]
matrixA2 = [[4, 0], [1, -9]]
matrixB = [[3, 8, 24], [4, 6, 17]]
matrixC = [[3, 8, 24], [4, 6, 17], [11, 14, 41]]


def matrixPrint(matrix, name_of_matrix):
    print(name_of_matrix)
    for i in range(0, len(matrix)):
        item_in_matrix = ""
        for j in range(0, len(matrix[i])):
            item_in_matrix = str(item_in_matrix) + " " + str(matrix[i][j])
        print(item_in_matrix)


def add(m1, m2):
    m3 = m1
    if len(m1) == len(m2):
        for row in range(0, len(m1)):
            print(str(m1[row]) + " + " + str(m2[row]))
            for num in range(0, len(m1)):
                m3[row][num] = m1[row][num] + m2[row][num]
            # matrixAnswer =
            if row == len(m1) - 1:
                print("= ")
        for row in m3:
            print(row)
        return m3
    else:
        print("Please use a valid matrix")


def add(m1, m2):
    m3 = m1
    if len(m1[0]) == len(m2[0]):
        for row in range(0, len(m1)):
            for num in range(0, len(m1)):
                m3[row][num] = m1[row][num] + m2[row][num]
        return m3
    else:
        print("Please use a valid matrix")


print(add(matrixA, matrixB))
