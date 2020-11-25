matrix1 = [[7, 24, 12], [50, 16, 42], [42, 48, 40], [32, 16, 5], [50, 16, 42]]
matrix2 = [[7, 24, 7, 1, 2], [50, 16, 50, 3, 4], [42, 48, 42, 5, 6], [32, 16, 32, 7, 8], [50, 1, 50, 9, 10]]
# Basic print:
def printmx(mx):
    for row in mx:
        printrow(row)
        print()
    return
    print('--------')
def printrow(row):
    for value in row:
        print('{:4d}'.format(value),end='')
    return
# printmx(matrix1)
# printmx(matrix2)

# Get maximum value:
def maximum_value(mx,name):
    print(f'The maximum value in matrix {name} is:  {max(max(mx))}')
    return max(max(mx))
# maximum_value(matrix1,'matrix1')
# maximum_value(matrix2,'matrix2')

# Get maximum sum for rows:
def maximum_row(mx):
    print(f'The max sum per row is: {max([sum(i) for i in mx])}')
    pass
# maximum_row(matrix1)
# maximum_row(matrix2)
# Get index of maximum sum of row:
def maximum_row_index(mx):
    maximum = [i[0] for i in mx]
    print('Maximum row: ',maximum)
    # for i in range(len(mx)):
    return

# maximum_row_index(matrix1)
# maximum_row_index(matrix2)

def transpose_mx(mx):
    n = len(mx)
    m = len(mx[0])
    trans = [[0 for i in range(n)] for j in range(m)]
    for i in range(m):
        for j in range(n):
            trans[i][j] = mx[j][i]
    return trans
# printmx(matrix1)
printmx(transpose_mx(matrix1))