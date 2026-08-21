# couleurs = ['bleu', 'rouge', 'vert']
# print(type(couleurs))
# print(couleurs)
#
# print(couleurs[1])
# a=["toto","tata"]
# b=["tete","titi"]
# print(a,b)
# c=[a,b]
# print(c)
#
# truc = list() # aussi truc = []
# print(truc)
# machin = [0.0]*3
# print(machin)
#
# liste1 = list(range(5, 9))
# print(liste1)
# liste2=list(range(2,9,2))
# print(liste2)
# print(len(liste2))
#
# print(2 in liste1, 8 in liste2, 6 not in liste2)

#
# nombre = [100, 87, 17, 1522, 45, 23]
# nombre.append(0)
# print(nombre)
# nombre.reverse()
# print((nombre))
# nombre.remove(1522)
# print((nombre))
# nombre.extend([1,2,3])
# print(nombre)
# nombre.sort()
# print(nombre)

tuple=(1,2)

#tuple[1]=3 # impossible car un tuple c'est triste et immutable
print(tuple)

sequences = [tuple, [4,5]]
for sequence in sequences:
    for item in sequence:
        print(item, end= ' ')
    print()

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

for i in range(3): # on parcoure pour les 3 lignes
    for j in range(4): # on parcour pour les 4 colonnes
        print(matrix[i][j], end=' ') # à chaque parcour ligne * colonne => on afficher le contenu (end = sans sauter de ligne)
