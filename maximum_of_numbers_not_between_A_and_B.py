n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
l1=[]
l2=[]
for i in l:
    if i>=a and i<=b:
        l1.append(i)
    else:
        l2.append(i)
if len(l2)>0:
    print(max(l2))
else:
    print("-1")