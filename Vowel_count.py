sentence = "Chandrahas is an Engineer"

count = 0

for char in sentence.lower():
    if char in "aeiou":
        count += 1

print(count)
