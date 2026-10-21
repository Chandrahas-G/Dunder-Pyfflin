text = "Chandrahas"
a = "an"

for char in a:
  text = text.replace(char,"")

print(text)

# Using index of          string.find(character)
text = "Chandrahas"
a = "an"
res = ""

for char in text:
  if a.find(char) == -1:
    res = res+char

print(res)
