a=input()
b=a.lower()
x=input()
y=x.lower()
l=[]
l1=[]
for i in b:
    if i not in y and i!=' ':
        l.append(i)
for i in y:
    if i not in b:
        l.append(i)
q=set(l)
q=list(q)
q.sort()
if len(q)>0:
    for i in q:
        print(i,end="")
else:
    print("-1")