n=int(input())
flag=0
b=[]
a=input().split(" ")
for i in range(0,n):
    if(int(a[i])==i):
        b.append(int(a[i]))
        flag=1
if(flag==0):
    print(-1)
else:
    print(*b,end=" ")