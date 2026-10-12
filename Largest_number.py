nums = (4123, 234, 3153)

l_num = nums[0]

for i in range(len(nums)):
  if nums[i] > l_num:
    l_num = nums[i]

print(l_num)
