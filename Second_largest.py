nums = [2, 3, 14, 8, 10, 12, 12, 14]
nums = sorted(set(nums))

print("Largest:", nums[-1])
print("Second largest:", nums[-2])

# using loop and if conditions
nums = [22, 3, 14, 8, 10, 12, 12, 14]
l_num = float('-inf')
sl_num = float('-inf')

for i in range(len(nums)):
  if nums[i] > l_num:
    sl_num = l_num
    l_num = nums[i]

  elif nums[i] > sl_num and nums[i] != l_num:
    sl_num = nums[i]

print(l_num, sl_num)
