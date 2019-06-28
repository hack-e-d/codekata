n=int(input())
s=0
arr=input().split(" ")
arr.sort(reverse=True)
for i in range(0,n):
    s*=10
    s+=int(arr[i])
print(s)