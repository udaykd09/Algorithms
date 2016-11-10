def print_sub_sets(arr):
    n = len(arr)
    powerset = pow(2, n)
    for c in range(powerset):
        for cc in range(n):
            if c & (1<<cc):
                print arr[cc],
        print ""

print_sub_sets([1,2,3])
