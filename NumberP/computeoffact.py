x=int(input())
n=int(input())
fact=1
for i in range(1,n+1):
    fact*=i
a=pow(x,n)/fact
print(a)
