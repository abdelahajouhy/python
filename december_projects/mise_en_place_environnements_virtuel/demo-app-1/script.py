# from <CLASS> IMPORT <METHOD> : ici j'importe la méthode. 
#   Plus  besoin d'appeller la méthode comme ça : <CLASS>.<METHOD>(), mais plutot directement la méthode <METHOD>()
#  si on importe toutes les méthodes d'une classe, c'est dangereux pour une app car risque de conflit entre les deux méthodes des différentes
#  classes, mais pour faire du debogging en cmd line python, c'est pas mal.  

#import os
#print(os.getcwd())

from os import getcwd
import numpy as np

print (getcwd())


print(np.ceil(1.2)) # 1
print(np.ceil(1.933)) # 2  
print(np.floor(1.2)) 

