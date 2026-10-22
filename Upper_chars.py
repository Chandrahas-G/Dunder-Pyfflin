# to Print upper case chars
S = "This Is Caps"
res = ""

for char in S:
  if char.isupper():
    res+=char

print(res)              # TIC

# count of upper case chars
S = "This Is Caps"
count = 0

for char in S:
  if char.isupper():
    count+=1

print(count)
