# With Dictionary
a = [2, 5, 3, 6, 2, 3]
freq = {}

for num in a:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

print(freq)                # {2: 2, 5: 1, 3: 2, 6: 1}

for num in a:
    if freq[num] == 1:
        print(num)


# using loops & empty list
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
