a,b=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
l3=[]
res=[]
for i in l1:
    for j in l2:
        if i==j:
            l3.append(i)
resu=set(l3)
print(len(resu))