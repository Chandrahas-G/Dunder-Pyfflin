# Slicing 
text = "Hello World"
print(" ".join(text.split()[::-1]))

# loop
text = "Hello World"
text = text.split()

for i in range(len(text)-1, -1, -1):
  print (text[i],end=' ')
