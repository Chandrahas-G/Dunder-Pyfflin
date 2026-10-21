a = [2,3,5,8,4,5]
b = []

for i in range(len(a)-1, -1, -1):
  #print(a[i], end=" ")          # prints only numbers
  b.append(a[i])
  
print(b)                        # Prints List
