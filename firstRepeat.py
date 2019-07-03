n=int(input())
a=input().split(" ")
b=[]
for temp in a:
    b.append(int(temp))
flag=0
for y in range(0,n):
    for i in range(0,n):
        tew=int(b[i])
        for j in range(i+1,y+2):
            if(i!=j and b[i]==b[j]):
                flag=1
                print(tew)
                break
        if(flag==1):
            break
    if(flag==1):
        break

