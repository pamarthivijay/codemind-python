a,b=map(int,input().split())
l=list(map(int,input().split()))
x=len(l)
c=0
for i in range(x):
    y=0
    for j in range(i,x):
        y+=l[j]
        if y==b:
            c+=1
print(c)