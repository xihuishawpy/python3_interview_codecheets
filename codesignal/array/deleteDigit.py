"""
For n = 152, the output should be
deleteDigit(n) = 52;
For n = 1001, the output should be
deleteDigit(n) = 101.
"""
def deleteDigit(n):
    rtn = 0
    numList = [ int(c) for c in str(n)]

    for i in range(len(numList)):
        newList = numList[:i] + numList[i+1:]
        rtn = max(rtn, int(''.join(map(str, newList))))

    return rtn 