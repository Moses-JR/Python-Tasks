a=int(input())
b=int(input())
asum=0
bsum=0
for i in range(1,a+1):
    if(a%i==0):
        asum+=i
for i in range(1,b+1):
    if(b%i==0):
        bsum+=i
if a/b==asum/bsum:
    print("friendly pair")
else:
    print("Not friendly pair")
        
        
