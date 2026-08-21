liste1=['a','b','b']
liste2=['b','c','c']

diff= set(liste1) ^ set(liste2) # https://chatgpt.com/c/680aac49-fddc-800c-a2b4-55ba0cbecf7a
print(diff)


a=["1","2"]
b=["2","4"]

print(set(a))
print(set(b))

c= set(a) ^ set(b)
print("c=",c)
