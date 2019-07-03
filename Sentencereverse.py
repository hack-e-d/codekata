str = input().split(" ")
strrev=""
q=0
for s in str:
    srev=""
    for i in s:
        srev=i+srev
    if(q==0):
        strrev=srev
        q=q+1
    else:
        strrev=strrev+" "+srev
print(strrev)