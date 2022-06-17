class Solution:
    def findMin(self, nums: List[int]) -> int:
        if not nums:
            return
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[-1] > nums[mid]:
                right = mid
            else:
                left = mid + 1
        return nums[left]