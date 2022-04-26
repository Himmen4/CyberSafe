import requests
url= "https://cybersecurity.codabra.org/Codabrin.zip"
file=requests.get(url)
open("codabrin.zip","wb").write(file.content)