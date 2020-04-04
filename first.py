import numpy as np
from numpy.linalg import LinAlgError


def subtract(a, b):
    b = np.subtract(b, a)
    return b


def divide(a, x):
    for r in range(len(a)):
        a[r] = a[r] / x
    return a


def multiply(a, x):
    li = []
    for y in range(len(a)):
        li.append(x * a[y])
    return li


def print_matrix(array):
    print(np.round_(array, decimals=3))
    print("--------------------------")


print("please enter the row and column of the matrix:")
m, n = input().split()
print('please enter the coefficient matrix:')
aug_matrix = np.zeros((int(m), int(n) + 1))
for i in range(int(m)):
    l = input().split()
    l.append('0')
    l = [int(x) for x in l]
    aug_matrix[i] = l
# print(cof)
print('please enter the vector:')
for i in range(int(m)):
    x = int(input())
    aug_matrix[i][int(n)] = x
print('the Augmented matrix is:')
print_matrix(aug_matrix)
pivot_positions = []
pivot_columns = []
free = 0
col = 0
for row in range(int(m)):
    # while col < int(n):
    if col < (int(n) + 1):
        count = np.count_nonzero(aug_matrix[:, col])
        # print(count)
        if count == 0:
            col += 1
            if col > int(n) + 1:
                break
        # for x in cof[:, col]:
        #     if x != 0:
        #         temp = 1
        #         break
        #     print("jjj ", count)
        #     print_matrix(aug_matrix[:, col])
            # print("column")
        # if temp == 0:
        #     col += 1
        arr = []
        for i in aug_matrix[row]:
            arr.append(i)
        # print(arr)
        if aug_matrix[row][col] == 0:
            for k in range(row, int(m)):
                if aug_matrix[k][col] != 0:
                    # aug_matrix[[i, k]] = aug_matrix[[k, row]]
                    # break
                    aug_matrix[row] = aug_matrix[k]
                    aug_matrix[k] = arr
                    # print(arr)
                    # print("swap")
            print_matrix(aug_matrix)
            # print(col)
        if aug_matrix[row][col] == 1:
            pivot_positions.append((row, col))
            free += 1
            pivot_columns.append(col + 1)
        # print(aug_matrix[row][col], "++++")
        if np.fabs(aug_matrix[row][col]) < 0.0001:
            aug_matrix[row][col] = 0
        if aug_matrix[row][col] != 1 and aug_matrix[row][col] != 0:
            divide(aug_matrix[row], aug_matrix[row][col])
            pivot_positions.append((row, col))
            free += 1
            pivot_columns.append(col + 1)
            print_matrix(aug_matrix)
            # print("divide + ", aug_matrix[row][col])
            print(col)

        for t in range(int(m)):
            if t != row:
                o = aug_matrix[row]
                o = multiply(o, aug_matrix[t][col])
                # print(*o)
                aug_matrix[t] = np.subtract(aug_matrix[t], o)
                print_matrix(aug_matrix)
                # print(col)
                # print("sub +", free)
    elif col >= (1 + int(n)):
        print_matrix(aug_matrix)
        break
    col += 1
print("the reduced echelon matrix is:")
aug_matrix = np.round_(aug_matrix)
print_matrix(aug_matrix)
# invC = np.linalg.inv(cof[: int(n) + 1])
# X = invC.dot(cof[:, n])
# print(X)
b = np.round_(aug_matrix[:, int(n)])
for x in range(len(b)):
    if b[x] == -0:
        b[x] = 0
a = aug_matrix[:, :int(n)]
# print("the coefficient matrix is:\n ", a)
# print("the vector is\n", b)
# print("pivot columns are: ", *pivot_columns)

# if int(m) >= int(n):
flag = False
# print("=-=-=-=-")
# print(np.count_nonzero(cof[2]))
# print(aug_matrix[2][int(n)])
for j in range(int(m)):
    if np.count_nonzero(aug_matrix[j]) == 1 and aug_matrix[j][int(n)] != 0:
        print("inconsistent")
        aug_matrix[j][int(n)] = 1
        pivot_columns.append(int(n) + 1)
        pivot_positions.append((int(m)-1, int(n)))
        free += 1
        flag = True
        break
print("the coefficient matrix is:\n ", a)
print("the vector is\n", b)
print("pivot columns are: ", *pivot_columns)
print("the pivot positions are:", *pivot_positions)
if not flag:
    # checking for the free variable with checking the pivot positions:
    # we have the pivot columns here:
    print("the leading variables are:")
    for x in pivot_columns:
        print('x' + str(x) + ", ", end='')
    print("")
    if free < int(n):
        solution = np.zeros((int(n), 1))
        for x in range(int(n)):
            if x < int(m):
                solution[x] = b[x]
        print("we have free variable(s) and the solution is:")
        print(solution, end='')
        for y in range(1, int(n)+1):
            if pivot_columns.count(y) == 0:
                temp = np.zeros((int(n), 1))
                for x in range(int(n)):
                    if x < int(m):
                        temp[x] = aug_matrix[x, y - 1] * -1
                        if temp[x] == -0:
                            temp[x] = 0
                    if x == y-1:
                        temp[x] = 1
                print(" + ", end='')
                print("x" + str(y) + "*", end='')
                print(temp)
    else:
        try:
            print("the solution is ", np.linalg.solve(a, b))
        except LinAlgError:
            print("inconsistent****")














