#
# a>0
# b=!0
#
# somme
# diff
# produit
# a/b et b/a
# log10a
# a^b

a = int(input("saisir a"))
b = int(input("saisir b"))
print(a+b)
print(a-b)
print(a*b)

try:
  print(a/b)
except:
  print("b ne doit pas être null")
