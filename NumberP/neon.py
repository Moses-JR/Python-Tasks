a=int(input())
b=a*a
sum=0
while b!=0:
    c=b%10
    sum+=c
    b=int(b/10)
if(sum==a):
    print("Neon Number")
else:
    print("Not neon")
