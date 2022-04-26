file=open("Profile.photo.bmp","rb")
file.seek(-29,2)
text=file.read(29)
open("file","wb").write(text)