a=input()
b=a.lower()
l=set()
for i in b:
    if i!=" ":
        l.add(i)
print(len(l))