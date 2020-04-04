import numpy as np


def subtract(a, b):
    b = np.subtract(b, a)
    return b


def divide(a, x):
    for y in range(len(a)):
        a[y] = a[y] / x
    return a


def multiply(a, x):
    li = []
    for y in range(len(a)):
        li.append(x * a[y])
    return li


def print_matrix(array):
    print(array)
    print("--------------------------")


def null_space(aug_matrix, m, n) :
    pivot_positions = []
    pivot_columns = []
    free = 0
    col = 0
    for row in range(int(m)):
        # while col < int(n):
        if col <= int(n):
            count = np.count_nonzero(aug_matrix[:, col])
            # print(count)
            if count == 0:
                col += 1
                if col > int(n):
                    break

                print_matrix(aug_matrix[:, col])
                print("column")

            arr = []
            for i in aug_matrix[row]:
                arr.append(i)

            if aug_matrix[row][col] == 0:
                for k in range(row, int(m)):
                    if aug_matrix[k][col] != 0:

                        aug_matrix[row] = aug_matrix[k]
                        aug_matrix[k] = arr

            if aug_matrix[row][col] == 1:
                pivot_positions.append((row, col))
                free += 1
                pivot_columns.append(col + 1)

            if np.fabs(aug_matrix[row][col]) < 0.0001:
                aug_matrix[row][col] = 0
            if aug_matrix[row][col] != 1 and aug_matrix[row][col] != 0:
                divide(aug_matrix[row], aug_matrix[row][col])
                pivot_positions.append((row, col))
                free += 1
                pivot_columns.append(col + 1)

            for t in range(int(m)):
                if t != row:
                    o = aug_matrix[row]
                    o = multiply(o, aug_matrix[t][col])
                    aug_matrix[t] = np.subtract(aug_matrix[t], o)
                    # print_matrix(aug_matrix)
                    # # print(col)
                    # print("sub +", free)
        elif col > int(n):
            break
        col += 1
    # print("the reduced echelon matrix is:")
    aug_matrix = np.round_(aug_matrix)
    # print_matrix(aug_matrix)

    b = np.round_(aug_matrix[:, int(n)])
    for x in range(len(b)):
        if b[x] == -0:
            b[x] = 0

    for j in range(int(m)):
        if np.count_nonzero(aug_matrix[j]) == 1 and aug_matrix[j][int(n)] != 0:
            print("inconsistent")
            flag = True
            break
    if free < int(n):
        solution = np.zeros((int(n), 1))
        for x in range(int(n)):
            if x < int(m):
                solution[x] = b[x]

        print("the null space of the matrix is:")
        for y in range(1, int(n) + 1):
            if pivot_columns.count(y) == 0:
                temp = np.zeros((int(n), 1))
                for x in range(int(n)):
                    if x < int(m):
                        temp[x] = aug_matrix[x, y - 1] * -1
                        if temp[x] == -0:
                            temp[x] = 0
                    if x == y - 1:
                        temp[x] = 1
                    #
                print(temp)
                print("------")

    else:
        print("the null space is 0")


print("please enter the row and column:")
m, n = input().split()
print("please enter the matrix:")
matrix = np.zeros((int(m), int(n) + 1))
for i in range(int(m)):
    l = input().split()
    l.append('0')
    l = [int(x) for x in l]
    matrix[i] = l
print("the rank of the matrix is ")
rank = np.linalg.matrix_rank(matrix[:, :int(n)])
print(rank)
null_space(matrix, int(m), int(n))
print("and the dimension of null space is :", int(n) - rank)


