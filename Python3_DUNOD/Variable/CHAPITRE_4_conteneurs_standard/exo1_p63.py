liste1 = ["a", "b", "c","c","c","c"]
liste2 = ["e", "f", "g","g","c"]

for i in liste1:
    if i in liste2:
        print("element en commun ! :", i)
        break
else:
    print("ko")


# Plus rapide : utiliser les set, car les sets des collections non ordonnées d'éléments uniques.
print(set(liste1))
print(set(liste2))
commun= set(liste1) & set(liste2)
if set(liste1) & set(liste2):
    print("point commun: ", commun)
else:
    print("pas delement commun")
