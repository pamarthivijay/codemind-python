a=input()
b=a.lower()
x=input()
y=x.lower()
l=[]
for i in b:
    if i in y and i!=' ':
        l.append(i)
q=set(l)
q=list(q)
q.sort()
if len(q)>0:
    for i in q:
        print(i,end="")
else:
    print("-1")