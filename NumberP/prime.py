a=int(input())
c=0
for i in range(2,int((a/2)+1)):
    if(a%i==0):
        c+=1
if(c==0):
    print("Prime")
else:
    print("not prime")
