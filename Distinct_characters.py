a=input()
b=a.lower()
l=[]
for i in b:
    if i!=" ":
        l.append(i)
x=set(l)
y=list(x)
y.sort()
for i in y:
    print(i,end='')