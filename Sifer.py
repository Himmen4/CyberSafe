import string

shifr=open("Shifr.txt","r").read()
shifr=shifr.lower()
chars=string.ascii_lowercase
a1=list(chars)
a2=list(chars)
word=input("кодовое слово:\n")
res=""

for j,i in enumerate(word):
    a2.remove(i)
    a2.insert(j,i)
    print(str(a2))
for i in shifr:
    if i not in a2:
        res+=i
        continue
    res+= a1[a2.index(i)]

with open("decipher.txt","w") as f:
    f.write(res)