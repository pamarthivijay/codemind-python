import itertools

s=input()
l=list(itertools.permutations(s))
for i in l:
   print("".join(i))