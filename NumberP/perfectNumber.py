a=int(input())
sum=0
for i in range(1,int(a/2)+1):
    if(a%i==0):
        sum+=i
if(sum==a):
    print("perfect number")
else:
    print("not")
        
    
