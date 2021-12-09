import json                 # v praxi 4 fce: load, loads, dump, dumps

joo = json.loads('{"key":11}')

print(joo["key"])
joo["key2"] = None

print(joo)

print(json.dumps(joo))      #Převedo do json reprezentace

with open("vystup_json.json", "w") as f:
    json.dump(joo, f)

#NAINSTALOVAL JSEM REQUESTS - pip install requests

#r = requests.get("www")
#r.status_code
#r.headers["content types"]

#r.text

#r.json