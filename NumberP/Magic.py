num=int(input())
num1=num
sum=0
while(num1!=0):
    rem=num1%10
    sum+=rem
    num1=int(num1/10)
rev=0
num2=sum
while(num2!=0):
    rem1=num2%10
    rev=rev*10+rem1
    num2=int(num2/10)
if(rev*sum==num):
    print("Yes")
else:
    print("No")
    
