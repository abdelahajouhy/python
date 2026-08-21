mots = ['r', 'abc', 'aba', 'xyz', '1221']

for i in mots:
    if len(i) > 2 and i[0] == i[-1]:
        print(i)


