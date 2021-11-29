import requests

URL = "https://mapa.pid.cz/getData.php"

r = requests.get(URL)

print(r.status_code)
print(r.encoding)


data = r.json()

#print(type(data))
#print(data.keys())
#print(type(data["trips"]))
#print(type(data["trips"].keys()))
#print(type(data["trips"]["389/2"]))


