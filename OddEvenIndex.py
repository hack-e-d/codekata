n=int(input())
a=input().split(" ")
b=[]
for x in range(0,n):
    if((x+1)%2==0):
        if(int(a[x])%2==0):
            b.append(int(a[x]))
    if((x+1)%2==1):
        if(int(a[x])%2==1):
            b.append(int(a[x]))
print(*b,sep=" ")