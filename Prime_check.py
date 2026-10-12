num = int(input("Enter a Number: "))
flag = False

if num > 1:
  for i in range(2, num):
    if num % i == 0:
      flag = True

if num <=1 or flag:
  print(f"{num} is Not a Prime Number")
else:
  print(f"{num} is a Prime Number")


## Without flags, used 'return' to function instead
def prime_check(num):

  if num < 2:
    print ("Not Prime")
    return
    
  for i in range(2, num):
    if num % i == 0:
      print("Not Prime")
      return
    
  print("Prime")

prime_check(67)
