# Résumé et syntaxe :

# Les dictionnaires stockent des paires clé-valeur.

# Syntaxe de base :

# Création : mon_dict = {"clé": "valeur"}

# Ajouter ou modifier : mon_dict["clé"] = "nouvelle_valeur"

# Accéder : mon_dict["clé"]

# Mnémotechnique :
# "Dictionnaire = Défini par des Données clés".
# C’est un peu comme un annuaire où chaque clé donne accès à une valeur.

# Exercice :
# Crée un dictionnaire avec une clé "nom" et une valeur "Alice". Ajoute une nouvelle clé "âge" avec la valeur 25.
# réponse: 
dico= {"nom":"Alice"}
print(dico)
dico["age"]=25
dico["nom"]="Alicia"
print(dico)

sac = {3:"pommes",1:"pain",8:"yahourts"}
w=sac.items
print(w)
k=sac.keys()
print(k)
del sac[8]
print(k)
sac["bug"]=9
print(k)
print(sac)
print("0" in k, 1 in k)

d = {0: 1, 1: 10, 2: 20}
# for i in d.items():
#     print(i)
s=0
for k, v in d.items():
    print(k,v)
    s+=v
d['nouveau']=s
print(d)