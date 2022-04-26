import zipfile

def nop():
    filezip="letters.zip"
    ditcionary="passwords.txt"

    password= None
    zip_file=zipfile.ZipFile(filezip, mode="r")
    with open(ditcionary, "r") as f:
        for line in f.readlines():
            password = line.strip("\n")
            try:
                zip_file.extractall(path="./output", pwd=bytes(password, "utf8"))
                password= 'Password found: %s' % password
                print (password)
                break
            except:
                pass

nop()