a=int(input())
sum=0
while sum!=1 and sum!=4:
    sum=0
    while a!=0:
        b=a%10
        sum+=b*b
        a=int(a/10)
    a=sum
if sum==1:
    print("Happy Number")
else:
    print("Unhappy number")
