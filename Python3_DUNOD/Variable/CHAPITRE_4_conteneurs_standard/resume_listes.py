######################### 1
a=["A","B"]
b=["B","C"]
# diff_symetrique a,b = A,C
# commun = set(a) & set(b)
# print(commun)
#
# for i in a:
#     if i in b:
#         print("commun", i)
#         break
# else:
#     print("pas de commun")

######################### 2

# mots = ['abc', 'aba', 'xyz', '1221']
#
# for i in mots:
#     if len(i) > 2 and i[0] == i[-1:]:
#         print(i)

######################### 3

set_a = set(a)
set_b = set(b)

diff= set_a ^ set_b
print(diff)
