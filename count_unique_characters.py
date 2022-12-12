a=input()
b=a.lower()
l=[]
for i in b:
    if b.count(i)==1 and i!=" ":
        l.append(i)
print(len(l))