# Using Dict
text = "testing"
dict = {}

for char in text:
  if char in dict:
    dict[char]=dict[char]+1
  else:
    dict.update({char:1})

print(dict)

# Another way using Dict
str1 = "Jai Mahishmathi"
str1.lower()

char_count = {}            # Using Dictionary

for i in range(len(str1)):
    c = str1[i]

    if c != ' ':
        if c in char_count:
            char_count[c] = char_count[c] + 1
        else:
            char_count[c] = 1        # can also be written as char_count.update({c:1})

print(char_count)
