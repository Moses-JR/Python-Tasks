a=int(input())
sum=0
mul=1
while a!=0:
    b=a%10
    sum+=b
    mul*=b
    a=int(a/10)
if(sum==mul):
    print("Spy number")
else:
    print("Not spy")
