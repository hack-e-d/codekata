a,b=input().split(" ")
a =int(a)
b =int(b)
aa=input().split(" ")
bb=input().split(" ")
flag=0
flag1=1
for i in range(0,b):
    for j in range(0,a):
        if(int(bb[i])==int(aa[j])):
            flag=1
            break
    if(flag==0):
        flag1=0
        break
    flag=0
if(flag1==1):
    print("YES")
else:
    print("NO")
