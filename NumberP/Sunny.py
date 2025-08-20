a=int(input())
b=a+1
c=0
for i in range(1,int(a/2)):
    if i*i==b:
        c+=1
        break
if c==1:
    print("Sunny Number")
else:
    print("Not Sunny Number")
