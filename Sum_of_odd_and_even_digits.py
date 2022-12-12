n=int(input())
l=list(map(int,input().split()))
l1=[]
l2=[]
for i in range(len(l)):
    if i%2==0:
        l1.append(l[i])
    else:
        l2.append(l[i])
s=sum(l1)-sum(l2)
if s==0:
    print("YES")
else:
    print("NO")