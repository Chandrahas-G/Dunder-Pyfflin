# Using Counter and extra res string
from collections import Counter
text = "Automation"
count = Counter(text)
res = ""

for char in text:
  if count[char] > 1:
    res = res + "2"
  else:
    res += char

print(res)

# with Inner Loop and without Counter & Empty String
text = "Automation"

for char in text:
  count = 0
  for i in range(len(text)):
    if char == text[i]:
      count+=1

  if count > 1:
    text = text.replace(char,"2")

print(text)
