sentence = "My My Name is Chandrahas is an Engineer is"
words = sentence.lower().split()
res = {}                                                        # Dictionary

for word in words:
  if word in res:
    res[word]+=1
  else:
    res[word] = 1
print (res)

for key in res:                                    # Using keys
  if res[key] > 1:
    print (key)

for key in res.keys():                            
  if res[key] > 1:
    print (key)

for k, v in res.items():                          # Using items (key, vales pair)
  if v > 1:
    print (k)
