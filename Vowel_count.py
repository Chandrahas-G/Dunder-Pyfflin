sentence = "Chandrahas is an Engineer"
vowel_count = 0
consontant_count = 0

for char in sentence.lower():
  if char in "aeiou":
    vowel_count+=1
  elif 'a' <= char <= 'z':
    consontant_count+=1

print (vowel_count, consontant_count)
