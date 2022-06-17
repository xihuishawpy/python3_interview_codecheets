def find_missing_numbers(nums):

  i = 0
  while i < len(nums):
    j = nums[i] - 1
    if nums[i] != nums[j]:
      nums[j], nums[i] = nums[i], nums[j]
    else:
      i += 1

  return [x+1 for x, n in enumerate(nums) if x+1 != n]


def main():
  print(find_missing_numbers([4, 3, 5, 2, 1]))


main()

