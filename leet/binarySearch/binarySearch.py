"""
time: > 20 min
errors: misplaced :, new algo
time: O(logN)
space: O(1)
"""
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums) - 1
        left = 0
        l,r = 0, len(nums) - 1
        while l < r:
            mid = l + (r-l)//2

            c = False
            if target <= nums[right] and nums[mid] > nums[right]:
                c = False
            elif target <= nums[right] or nums[mid] >= nums[right]:
                c = target <= nums[mid]
            else:
                c = True
            if c:
                r = mid
            else:
                l = mid + 1

        return l if nums[l] == target else -1