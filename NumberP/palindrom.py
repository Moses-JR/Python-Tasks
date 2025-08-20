a=int(input())
d=a
b=0
while(a!=0):
    c=a%10
    a=int(a/10)
    b=b*10+c
if(d==b):
    print("Palindrom")
else:
        print("not palindrom")
