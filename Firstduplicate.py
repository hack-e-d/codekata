n=int(input())
a=input().split(" ")
b=0
flag=0
for i in range(0,n):
    for j in range(i+1,n):
        if(int(a[i])==int(a[j])):
            b=int(a[i])
            flag=1
            break
if(flag==1):
    print(b)
if(flag==0):
    print("unique")