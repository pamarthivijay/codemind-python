from itertools import permutations

a,b=map(int,input().split())
l=[]
c=b-1
for i in range(1,a+1):
    l.append(i)
for i in range(len(l)):
    x=list(permutations(l))
y=x[c]
for i in y:
    print(i,end='')