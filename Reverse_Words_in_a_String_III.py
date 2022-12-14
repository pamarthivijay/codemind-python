n=input()
a=n.split()
l1=[]
for i in a:
    x=i[::-1]
    l1.append(x)
print(*l1)