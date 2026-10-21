# First Non-Repeating char only
from collections import Counter
s = "chandrahas"
count = Counter(s)

for char in s:
  if count[char] == 1:
    print(char)

# All Non-Repeating characters
text = "chandrahas"

for i in range(len(text)):
  count = 0
  for j in range(len(text)):
    if text[i] == text[j]:
      count+=1
  if count == 1:
    print(text[i])
    break                  # add 'break' to print only First Non-repeating character only

# Last one Non-Repeating character only
text = "chandrahas"

for i in range(len(text)-1, -1, -1):
  count = 0
  for j in range(len(text)):
    if text[i] == text[j]:
      count+=1
  if count == 1:
    print(text[i])
    break                # add 'break' to print only Last Non-repeating character only

# using Counter from collections
from collections import Counter
def non_repeat(s):
  count = Counter(s)

  for char in reversed(s):
    if count[char] == 1:
      return char

print(non_repeat("chandrahas"))
