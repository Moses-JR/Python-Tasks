a=int(input())
c=a
sum=0
while(a!=0):
    b=a%10
    a=int(a/10)
    sum+=b
if(c%sum==0):
    print("Harshade number")
else:
    print("Not")
