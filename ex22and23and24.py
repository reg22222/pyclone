#22
song = """by the rivers of babylon"""
alphabet=dict()

for c in song:
    if c.isalpha()==False:
        continue
    c=c.lower()
    if c not in alphabet:
        alphabet[c]=1
    else:
        alphabet[c]+=1
print(alphabet)

#23
key = list(alphabet.keys())
key.sort()
for c in key:
    num = alphabet.keys
    print(c,"=>",num)

#24
for code in range(ord('a'),ord('z')+1):
    c = chr(code)
    num = alphabet.get(c)
    print(c,"=>",num)