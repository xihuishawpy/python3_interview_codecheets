"""
time: lgn
space: 1
"""
class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        target = k + nums[0] - 1
        while left_element := bisect.bisect(nums, target):
            nums = nums[left_element:]
            target += left_element
        return target