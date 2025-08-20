n=9
a=[1,2,3,4,5,6,7,9]
nsum=0
asum=0
c=len(a)
for i in range(1,n):
    nsum+=i
for j in range(0,c):
    asum+=j
b=nsum-asum
print(b)
