a=input()
b=a.lower()
c=b.split()
x=input()
y=x.lower()
z=y.split()
q=[]
for i in c:
    if i in z and c.count(i)==1 and z.count(i)==1:
        q.append(i)
print(len(q))