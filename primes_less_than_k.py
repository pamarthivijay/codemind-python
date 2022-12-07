n=int(input())
l=list(map(int,input().split()))
a=int(input())
d=[]
for i in l:
    c=0
    for j in range(2,i+1):
        if i%j==0 and i<=a:
            c+=1
    if c==1:
        d.append(i)
print(len(d))