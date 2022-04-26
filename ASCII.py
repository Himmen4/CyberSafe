with open("bin","r") as f:
    a = f.read()

res=""
i=0
while i<len(a)-8:
    b=a[i:i + 8]
    c=chr(int(b,2))
    res+=c
    i+=8
print(res)
