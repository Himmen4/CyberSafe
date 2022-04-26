def main():
    with open("letters.txt","r") as f:
        text=f.read()
    binresuil=""
    result=""
    for i in range(len(text)):
        temp=""
        if text[i]=='a':
            temp="00"
        if text[i] == 'o':
            temp = "01"
        if text[i] == 'p':
            temp = "10"
        if text[i] == 'e':
            temp = "11"
        binresuil+=temp
    i=0
    while i <= len(binresuil)-16:
        result += chr(int(binresuil[i:i+16],2))
        i+=16
    print(result)

main()