class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hm = {0:-1}
        ps = rtn = 0

        for i, n in enumerate(nums):
            ps += -1 if n == 0 else 1
            if ps in hm:
                rtn = max(rtn, i-hm[ps])
            else:
                hm[ps] = i

        return rtn
