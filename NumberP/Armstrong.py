a=int(input())
c=a
sum=0
while(a!=0):
    rem=a%10
    b=rem*rem*rem
    sum+=b
    a=int(a/10)
if(sum==c):
    print("Armstrong")
else:
    print("not armstrong")
