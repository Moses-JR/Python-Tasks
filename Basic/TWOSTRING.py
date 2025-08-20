input1 = "Machine"
input2 = "Learning"
f1 = input1[:(len(input1)//3)]
f3 = input1[len(input1)-(len(input1)//3):]
t1 = input2[:(len(input2)//3)]
t3 = input2[len(input2)-(len(input2)//3):]
print(t1+f1+f3+t3)