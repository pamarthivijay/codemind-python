a=int(input())
l=list(map(int,input().split()))
x=[]
y=[]
b=len(l)//2
for i in range(b):
    x.append(l[i])
for j in range(b,len(l)):
    y.append(l[j])
print(sum(x))
print(sum(y))