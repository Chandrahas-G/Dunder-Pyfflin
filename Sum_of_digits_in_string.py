import re

text = "C2h4a5n6d6r8a"
digits = re.sub(r"\D", "",text)
sum = 0
print(digits)                        # 245668

for digit in digits:
  num = int(digit)
  sum += num

print (sum)
