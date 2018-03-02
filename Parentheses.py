i = ["(","{","["]
j = [')','}',"]"]

def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    stack = []
    for n in s:
        if n in j:
            if not stack:
                return False
            elif i.index(stack.pop()) != j.index(n):
                return False
        if n in i:
            stack.extend(n)
    return not stack

d = {
    ')' : '(',
    ']' : '[',
    '}' : '{'
}

def isValidType2(s):
    """
    :type s: str
    :rtype: bool
    """
    l = []
    for n in s:
        if n in d.keys():
            if d[n] not in l:
                return False
        elif n in d.values():
            l.append(n)
    return True


#print isValid("{{{[][]}}()}")

print isValidType2('{[]}')