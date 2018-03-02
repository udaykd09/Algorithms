#Given a 2D array, where each row contains sorted values of 0s and 1s, find the row with max 1s

def rowWithMoreOnes(matrix):
    if not matrix:
        return None
    m = len(matrix)
    n = len(matrix[0])
    ans = -1
    for row in matrix:
        ans = max(ans, OnesInRow(row))
    return ans

def OnesInRow(row):
    if not row:
        return -1
    l = 0
    chng = 1
    r = len(row)-1
    if row[0] == 1:
        return len(row)
    if row[r] == 0:
        return 0
    while row[chng] == row[l] and l < r:
        m = l + (r - l) / 2
        print m
        if row[m] == row[r]:
            r = m
        if row[l] == row[m]:
            l = m
            chng = l + 1
    return len(row) - chng

print(OnesInRow([0,0,0,1,1,1,1]))