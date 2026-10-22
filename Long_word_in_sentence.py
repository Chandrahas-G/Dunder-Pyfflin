# python built-in
text = "Salaar Devaratha Raisaar"
words = text.split()

s_word = min(words, key = len)
l_word = max(words, key = len)

print (s_word, l_word)


# for loop & if conditions
text = "Salaar Devaratha Raisaar"
words = text.split()
s_word = words[0]
l_word = ""

for word in words:
  if len(word) < len(s_word):
    s_word = word

  if len(word) > len(l_word):
    l_word = word
  
print(s_word,l_word)
  
