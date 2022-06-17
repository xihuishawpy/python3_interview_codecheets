"""
inputArray = ["aba", "aa", "ad", "vcd", "aba"]
allLongestStrings(inputArray) = ["aba", "vcd", "aba"]

"""
def allLongestStrings(inputArray):
    mxLen = 0

    mxLen = len(max(inputArray, key=len))
    return [i for i in inputArray if len(i) == mxLen]

