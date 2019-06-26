#to find if odd or even
n=int(input())
try:
    if(n>0):
        if(n%2==0):
            print("Even")
        else:
            print("Odd")
    else:
        print("Invalid")
except:
    print("Invalid Input")
