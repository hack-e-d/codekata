n=int(input())
a=input().split(" ")
b=[]
flag=0
for i in range(0,n):
    for j in range(i+1,n):
        if(int(a[i])==int(a[j])):
            if a[i] not in b:
                b.append(int(a[i]))
                flag=1
b.sort()
if(flag==1):
    print(*b,end=" ")
if(flag==0):
    print("unique")