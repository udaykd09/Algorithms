import math

class Solution(object):

    def basicTwoAc(self, num):
        numArr = list(map(int, str(num).strip()))
        myMin = num
        i = 1
        while i < len(numArr):
            newArr = numArr[:i] + numArr[i+1:]
            newInt = int("".join(str(x) for x in newArr))
            print(myMin, i, newInt)
            myMin = newInt if myMin > newInt else myMin
            i += 1
        return myMin

    def twoAc(self, num):
        numArr = list(map(int, str(num).strip()))
        myMin = num
        i = 1
        arrLen = len(numArr)
        while i < arrLen:
            if numArr[i-1] <= numArr[i]:
                i += 1
                continue
            else:
                newArr = numArr[:i] + numArr[i+1:]
                newInt = int("".join(str(x) for x in newArr))
                print(myMin, i, newInt, newArr)
                myMin = newInt if myMin > newInt else myMin
                i += 1

        if myMin == num:
            pivot = arrLen-1 if numArr[arrLen-1] < numArr[arrLen-2] else arrLen - 2
            newArr = numArr[:pivot] + numArr[pivot+1:]
            myMin = int("".join(str(x) for x in newArr))

        return myMin

    def solution(self, num):
        num_arr = list(map(int, str(num).strip()))
        my_max = 0
        i = 1
        while i < len(num_arr):
            new_arr = num_arr[:i-1] + [int(math.ceil((num_arr[i] + num_arr[i-1])/float(2)))] + num_arr[i+1:]
            new_int = int("".join(str(x) for x in new_arr))
            print(my_max, i, new_int)
            my_max = new_int if my_max < new_int else my_max
            i += 1
        return my_max


mySol = Solution()
#print(mySol.twoAc(177763))
print(mySol.solution(9876543210))