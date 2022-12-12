l=input()
a=l.lower()
b=a.split()
x=[]
for i in b:
    q=i[::-1]
    if i==q:
        x.append(i)
print(len(x))