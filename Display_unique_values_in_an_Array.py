n=int(input())
l=list(map(int,input().split()))
a=[]
for i in l:
    if l.count(i)==1 and i!=" ":
        a.append(i)
if len(a)>0:
    print(*a)
else:
    print("-1")