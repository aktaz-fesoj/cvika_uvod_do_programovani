# Pro slovo vypsat kolik má jakých písmen

slovo_str = input("Zadejte slovo:")

slovo_seznam = list(slovo_str)
slovnik = {}
for i in range(len(slovo_seznam)):
    if slovo_seznam[i] in slovnik.keys():
        slovnik[slovo_seznam[i]] = slovnik[slovo_seznam[i]] + 1
    else:
        slovnik[slovo_seznam[i]] = 1
pocty = {}

print(slovnik)

#Counter(string)