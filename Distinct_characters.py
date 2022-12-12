a=input()
b=a.lower()
l=[]
for i in b:
    if b.count(i)==1 and i!=" ":
        l.append(i)
l.sort()
for i in l:
    print(i,end='')