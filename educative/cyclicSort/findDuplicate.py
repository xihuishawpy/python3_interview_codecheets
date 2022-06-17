"""
9 min

Error
int i
j = len(nums[i])
"""
def find_duplicate(nums):
  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[j], nums[i] = nums[i], nums[j]
    elif i == j:
      i += 1
    else:
      return nums[i]
  return -1
