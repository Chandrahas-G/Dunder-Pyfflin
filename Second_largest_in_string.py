import re

text = "str102553rts"
nums = re.findall(r"\d",text)
print(nums)                          # ['1', '0', '2', '5', '5', '3']

l_num = float('-inf')
sl_num = float('-inf')

for digit in nums:
  num = int(digit)
  if num > l_num:
    sl_num = l_num
    l_num = num

  elif num > sl_num and num != l_num:
    sl_num = num

print (l_num, sl_num)
