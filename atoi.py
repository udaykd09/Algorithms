def atoi(str):
    ans = 0
    negative = False
    if str[0] == '-':
        negative = True
        str = str[1:]
    for s in str:
        x = ord(s) - ord('0')
        if 0 > x or x > 9:
            raise Exception("NotCorrect")
        ans = ans*10 + x
    return ans if not negative else -ans

print(atoi('-10'))