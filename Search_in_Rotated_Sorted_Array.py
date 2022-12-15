n=int(input())
l=list(map(int,input().split()))
a=int(input())
l1=[]
for i in range(len(l)):
    if l[i]==a:
        l1.append(i)
if len(l1)>0:
    print(*l1)
else:
    print("-1")