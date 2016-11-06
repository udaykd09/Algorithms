def is_alternate(n1, n2):
    if n1 == 0 or n2 == 0:
        return True
    if n1 > 0:
        return n2<0
    elif n1 < 0:
        return n2>0

def max_alternating_slice(arr):
    mmax = 1
    max_arr = []
    n = 1
    while n<len(arr):
        isit = is_alternate(arr[n - 1], arr[n])
        if isit:
            mmax += 1
            if n == len(arr) - 1:
                max_arr.append(mmax)
        else:
            max_arr.append(mmax)
            mmax = 1
        n += 1
    return max(max_arr)

print(max_alternating_slice([1,1,-1,1,1,1,1]))