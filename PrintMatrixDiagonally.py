def print_diagonally(matrix):
    a = len(matrix)
    counter = 0
    final_array = []
    while True:
        array = []
        i = (a-1)-counter
        j = 0
        if i < 0:
            print i, counter
            j = -i
            i = 0
        while i < a and j < len(matrix[i]):
            array.append(matrix[i][j])
            i += 1
            j += 1
        if len(array) == 0:
            break

        final_array += array
        counter += 1

    return final_array

a = [
    ['a','b','c'],
    ['d','e','f','g'],
    ['h','i','j','k'],
    ['l','m','n']
    ]

print(print_diagonally(a))
