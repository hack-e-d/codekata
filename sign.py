#to find if positive ,negative or zero 
n=int(input())
try:
    if(n>0):
        print("Positive")
    elif(n<0):
        print("Negative")
    else:
        print("Zero")
except:
    print("Invalid Input")