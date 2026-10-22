def linear_search(nums, a):
  for i in range(len(nums)):
    if nums[i] == a:
      print (f"{a} is at index: {i}")

def binary_search(left, right, nums, a):
  if left <= right:
    mid = (left + right) // 2
    if a == nums[mid]:
      print (f"target {a} at index: {mid}")
    elif a > nums[mid]:
      left = mid + 1
      binary_search(left, right, nums, a)
    elif a < nums[mid]:
      right = mid - 1
      binary_search(left, right, nums, a)
  else:
    print (f"{a} is not present in list")
    
  
nums = [2, 3, 4, 8, 10, 12, 12, 14]
a = 12

linear_search(nums, a)
binary_search(0, len(nums)-1, nums, a)
