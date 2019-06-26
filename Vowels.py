#Code to find if consonant or vowels
a=input()
flag=1
vow=['a','e','i','o','u']
for v in vow:
    if(a==v):
        print("Vowel")
        flag=0
        break
if(flag):
    if(a>='a' and a<='z'):
        print("Consonant")
    else:
        print("invalid")