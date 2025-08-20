import math
num=int(input())
num2=num
sum=0
c=0
num1=0
while num!=0:
    c+=1
    num=int(num/10)
num=num2
while num!=0:
    b=num%10
    num1+=math.pow(b,c)
    c-=1
    num=int(num/10)
if num2==num:
    print("Disarium")
else:
    print("Not")
