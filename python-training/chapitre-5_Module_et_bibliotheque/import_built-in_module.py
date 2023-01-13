# python possède 243 modules (biblio et librairie) enrichissant le langage. 

import os
#les modules os sont considérés comme des attributs pour python. 
# Accéder à un objet/fonction/méthode monobjet du module os, on doit écrire : os.monobjet
os.getcwd() # cwd = Current Work Directory ,cette fonction de os donne le nom du répo courant      

import math as m    # éviter d'écrire math.cos
print(m.cos(1))

# ici on va uniquement importer que la fonction getcwd. Python ne connait pas os, mais que la fonction getcwd du module os. 
from os import getcwd
getcwd()

from os import * # pour tout importer, à éviter (voir page 71)
from os import getcwd, chdir # conseillé 
