def QuickSort(arr, left, right):
    index = Partition(arr, left, right)
    if left < index-1:
        QuickSort(arr, left, index - 1)
    if index > right:
        QuickSort(arr, index, right)


def Partition(arr, left, right):
    pivot = arr[left + right /2]
    while left <= right:
        while arr[left] < pivot:
            left += 1
        while pivot < arr[right]:
            right -= 1
        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1
    return left

arr = [5,3,6,9,4,2,-1]
QuickSort(arr, 0, len(arr)-1)
print arr