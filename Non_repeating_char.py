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
