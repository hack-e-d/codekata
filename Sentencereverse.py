str = input().split(" ")
strrev=""
for s in str:
    srev=""
    for i in s:
        srev=i+srev
    strrev=strrev+srev+" "
print(strrev)