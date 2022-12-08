n=int(input())
l=list(map(int,input().split()))
a=len(l)//2
l1=[]
l2=[]
for i in range(a):
    l1.append(l[i])
for j in range(a,len(l)):
    l2.append(l[j])
l2.reverse()
l3=l2+l1
print(*l3)