"""
time: 6 min
error: mistyped targetSum != target
a + b = c
a = c - b
"""
def twoNumberSum(array, targetSum):
    rtnList = []
    ht = {}

    for n in array:
        if n in ht:
            rtnList.extend((n, targetSum - n))
        ht[targetSum-n] = True

    return rtnList