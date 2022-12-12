a=input()
b=a.lower()
c=b.split()
x=input()
y=x.lower()
z=y.split()
q=0
for i in c:
    for j in z:
        if i==j:
            q+=1
print(q)