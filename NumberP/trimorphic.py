num=int(input())
val=num*num*num
c=0
while num!=0:
    if num%10!=val%10:
        c+=1
        break
    val=int(val/10)
    num=int(num/10)
if c==0:
    print("Trimorphic")
else:
    print("Not")
