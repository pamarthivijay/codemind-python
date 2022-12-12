a=input()
b=a.lower()
c=b.split()
x=input()
y=x.lower()
z=y.split()
l=[]
for i in z:
    for j in c:
        if i==j:
            l.append(i)
print(*l)