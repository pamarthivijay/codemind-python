n=input()
l=list(n)
l1=[]
l2=[]
for i in l:
    a=l.count(i)
    l1.append(a)
x=max(l1)
for i in l:
    if l.count(i)!=x:
        l2.append(i)
if len(l2)>0:
    print(l2[0])
else:
    print("-1")