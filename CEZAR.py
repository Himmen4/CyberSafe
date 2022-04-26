import itertools

word=input("фраза для шифровки:\n")
key=int(input("на сколько зашифровать:\n"))



res=""
utf_word=list(map(ord,word))
for i in utf_word:
    j=i+key
    if j<0:
        j+=1000
    elif j>1000:
        j-=1000
    j=chr(j)
    res+=j

print(res)