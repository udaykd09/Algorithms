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

print isValid("{{{[][]}}()}")