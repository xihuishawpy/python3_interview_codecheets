"""

"""

class Solution:
    """
    Time/Space: n
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        rtn = []
        mp = {}

        for i, n in enumerate(nums):
            if n in mp:
                rtn.extend((i, mp[n]))
            mp[target - n] = i

        return rtn
        

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        myList = []
        seenNums = {}

        if len(nums) == 1:
            return False

        for i, n in enumerate(nums):
            if target-n in seenNums:
                myList.extend((i, seenNums[target-n]))
            seenNums[n] = i

        return myList