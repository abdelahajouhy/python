capa_calor_eau = 4.186
volume_eau = float(input("entrez voluime d'eau en ml : "))
while volume_eau < 0:
    volume_eau = float(input("entrez voluime d'eau POSITIF en ml: "))

delta_T = float(input("entrez la témpérature (diff) en C°:"))
while delta_T < 0:
    delta_T = float(input("entrez la témpérature POSITIF en C°:"))

q = volume_eau * capa_calor_eau * delta_T
print(f"Cet échauffement requier une énérgie de ",q)
