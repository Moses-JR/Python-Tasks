num=int(input())
c=0
for i in range(0,num+1):
    if i*(i+1)==num:
        c+=1
        break
if c==1:
    print("Pronic")
else:
    print("Not")
