import string
import random

alpabet=string.ascii_let ters+string.digits+string.punctuation
password = " "
while input("Хотите продолжить?:\n") == "+":

    service= input("сервис:\n")
    login= input("логин:\n")
    dlina= int(input("длина:\n"))

    password= "".join([random.choice(alpabet) for i in range(dlina)])

    print(password)

    with open ("Passwords.txt","a")as f:

        info=service+" "+login+" "+password+"\n"

        f.write(info)