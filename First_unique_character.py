a=input()
b=a.lower()
l=[]
for i in b:
    if b.count(i)==1 and i!=" ":
        l.append(i)
if len(l)>0:
    print(l[0])
else:
    print("-1")