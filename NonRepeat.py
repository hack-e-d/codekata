n=int(input())
a=input().split(" ")
b=[]
for temp in a:
    b.append(int(temp))
flag=0
flag1=0
for i in range(0,n):
    tew=int(b[i])
    for j in range(0,n):
        if(i!=j and b[i]==b[j]):
            flag=1
    if(flag==0):
        print(tew)
        flag1=1
    flag=0
if(not flag1):
    print("No non repeat")
