def mergeSort(arr, helper, left, right):
    if left < right:
        mid = (left + right) / 2
        mergeSort(arr, helper, left, mid)
        mergeSort(arr, helper, mid + 1, right)
        merge(arr, helper, left, mid, right)


def merge(arr, helper, left, mid, right):
    for n in xrange(left,right+1):
        helper[n] = arr[n]

    hLeft = left
    hRight = mid + 1
    current = left

    while hLeft <= mid and hRight <= right:
        if helper[hLeft] < helper[hRight]:
            arr[current] = helper[hLeft]
            hLeft += 1
        else:
            arr[current] = helper[hRight]
            hRight += 1
        current += 1

    remaining = mid - hLeft
    for n in xrange(remaining+1):
        arr[current+n] = helper[hLeft+n]


arr = [5,3,6,9,4,2,-1]
mergeSort(arr,[0]*len(arr), 0, len(arr)-1)
print(arr)