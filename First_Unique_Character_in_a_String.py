a=input()
b=a.lower()
c=list(b)
l=[]
for i in range(len(c)):
    if c.count(c[i])==1:
        l.append(i)
        break
if len(l)>0:
    print(*l)
else:
    print("-1")