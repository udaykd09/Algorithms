def bsearch(item, arr):
    n = len(arr)
    first = 0
    last = n-1
    found = False
    while first<=last and not found:
        mid = (first + last)//2
        if arr[mid] == item:
            found = True
        elif arr[mid] < item:
            first = mid + 1
        else:
            last = mid - 1
    return found, mid

print(bsearch(0, [1,4,5,6]))