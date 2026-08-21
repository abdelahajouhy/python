# somme
entier = False
while not entier:
    n = int(input("saisi n"))
    if n >0:
        entier = True
        s = (n*(n+1))/2
        print(s)
    else:
        entier = False


