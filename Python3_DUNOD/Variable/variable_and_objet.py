type('Alain') # Le type de l'objet 'Alain' est str. Le type determine les opérations (i.e les méthodes) que l'on peut
# lui appliquer, et définit ainsi les valeurs possibles (données) pour les objets de ce type.

print('Alain'.upper()) # ici on applique la méthode upper à l'objet 'Alain'. 
prenom='alain' # Pour lier une variable à un objet on utilise l'affectation. Les variables référencent les objets 
                # prenom est la variable, objet est 'Alain' 
                # Lors d'une affectation, l'intérpréteur python exécute 3 opérations :
                    # 1- création de l'objet 'Alain' dans l'espace objet en mémoire
                    # 2- création de la variable prenom dans l'espace des variables
                    # 3- création d'une référence entre la variable et l'objet (donc entre prenom et 'Alain')
                    #    La référénce se déclare par l'opérateur = , que l'interpreteur Python comprend (cf photo)
print(prenom.lower()) #ici on manipule l'objet 'alain' à l'aide de sa REFERENCE prenom 

# si maintenant on affecte la variable prenom à l'objet 'Bob', il se passe quoi ?
print(type(prenom))
prenom='Bob'            # réaffectation (même type)
print(type(prenom))
prenom=8                #  réaffectation autre type => typage dynamique 
print(type(prenom))
# En python, le type d'une variable n'est pas lié à la variable qui référencie l'objet, mais plutot à l'objet lui même! plutot au type de l'objet 
# Lorsqu'un objet est crée,  il va garder son type pendant toute son existance, et une variable peut référencer des objets de types différents
# durant tout l'execution du programme, ce mécanisme s'apelle le typage dynamique, qui fait que Python est un langage à typage fort.

#variantes de l'affectation 
v=4
v+=2        # 6
c = d = 8
c,d         # (8,8) demande de 2 valeurs sous forme d'un tuple 
e,f=2,3     # affectation parallèle par décapsulation d'un tuple 
e,f         # (2,3)
a,b=2,3
a,b=a+b,a*2
a,b         # (5,4), dans une affectation le menbre de gauche pointe sur le membre de droite 

# Suppression d'une variable 
# dir permet de lister les variables qui référencient les objets, 
print(dir())
#['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__', 'a', 'b', 'c', 'd', 'prenom', 's', 'v']
del a,b,c,d,prenom,s,v # comme tt est dynamique en python, c possible de del une var au cours de l'execution, donc UN NOM QUI REFERENCIE UNE DONNéE!
print(dir())
# ['__annotations__', '__builtins__', '__doc__', '__loader__', '__name__', '__package__', '__spec__']
print(a) 
# Traceback (most recent call last):
#   File "<pyshell#52>", line 1, in <module>
#     print(a)
# NameError: name 'a' is not defined


