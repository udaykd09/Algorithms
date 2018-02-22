def reverseForm(matrix):
    n = len(matrix[0]) - 1
    ans = []
    wave = 1
    while n >= 0:
        m = 0
        while m < len(matrix):
            if not wave:
                ans.append(matrix[len(matrix)-1-m][n])
            else:
                ans.append(matrix[m][n])
            m += 1
        n -= 1
        wave = 0 if wave else 1
    return ans

def transpose(matrix):
    # for i swap ij ji where i < j < n
    n = len(matrix)
    for i in xrange(n):
        for j in xrange(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def sort(matrix):
    # 1. Sort rows
    # 2. Transpose
    # 3. Sort rows
    sort_rows(matrix)
    transpose(matrix)
    sort_rows(matrix)

def sort_rows(matrix):
    n = len(matrix)
    for i in xrange(n):
        matrix[i] = sorted(matrix[i])

def zigzag(matrix):
    # Using Sum of row+column
    m = len(matrix)
    n = len(matrix[0])
    ans = [[]for i in xrange(m+n-1)]
    for i in xrange(m):
        for j in xrange(n):
            sum = i+j
            if sum%2:
                ans[sum].insert(0, matrix[i][j])
            else:
                ans[sum].append(matrix[i][j])
    return ans


def bottom_top_diagonal(matrix):
    sol = []
    m = len(matrix)
    counter = 0
    while True:
        i = m - 1 - counter
        j = 0
        arr = []
        if i < 0:
            j = -i
            i = 0
        while i < m and j < len(matrix[0]):
            arr.append(matrix[i][j])
            i += 1
            j += 1
        if not arr:
            break
        sol.append(arr)
        counter += 1
    return sol

def rotate(matrix):
    if matrix is None or len(matrix) < 1:
        return
    else:
        if len(matrix) == 1:
            return matrix
        else:
            # solution matrix
            soln = [row[:] for row in matrix]
            # size of matrix
            m = len(matrix)

            for x in range(0, m):
                for j in range(0, m):
                    soln[j][m - 1 - x] = matrix[x][j]
            return soln

def rotate_2(matrix):
    # 1. Transpose
    # 2. Reverse Rows
    transpose(matrix)
    m = len(matrix)
    for i in xrange(m):
        matrix[i] = matrix[i][::-1]

matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

#transpose(matrix)
#print matrix
#sort_helper(matrix)
#print matrix
#print(reverseForm(matrix))
#print zigzag(matrix)
#rotate_2(matrix)
print bottom_top_diagonal(matrix)