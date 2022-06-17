def find_missing_number(nums):
  i = 0
  while i < len(nums):
    j = nums[i] 
    if j < len(nums) and nums[i] != nums[j]:
      nums[i], nums[j] = nums[j], nums[i]
    else:
      i += 1

  return next((i for i, n in enumerate(nums) if i != n), -1)
