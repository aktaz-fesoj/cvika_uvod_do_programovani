#open()
#read()
#write()
#close() # - Důležité, nemusí být vše zapsáno bez close

#with open() as f:   # Důrazně doporučeno používat tuto konstrukci


#Cesty relativní
#Cesty absolutní

#### DŮLEŽITÁ JSOU DVĚ ZPĚTNÁ LOMÍTKA V CESTĚ A ENCODING

#.append - přidání do seznamu
#.pop - odebrání ze seznamu

l =["a", 2, None, True, "Ahoj"]
print(l)
print(l[2:4])
l.append("Posledni")
print(l)
print(l.pop())
print(l)
del l[3]
print(l)
l[1] = l[1] + 4

print(l)