a=input()
l=list(a)
v="0123456789"
l1=[]
for i in l:
    if i in v:
        l1.append(i)
l2=[eval(i) for i in l1]
print(sum(l2))