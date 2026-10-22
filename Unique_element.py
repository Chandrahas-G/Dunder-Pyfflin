a = [2, 5, 3, 2, 3]
res = []

for i in range(len(a)):
  count = 0
  for j in range(len(a)):
    if a[j] == a[i]:
      count+=1

  if count == 1:
    res.append(a[i])

print (res)
