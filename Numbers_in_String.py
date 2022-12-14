a=input()
l=list(a)
l1=[]
x="0123456789"
for i in l:
    if i in x:
        k=int(i)
        l1.append(k)
print(sum(l1))