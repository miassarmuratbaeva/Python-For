num=int(input())
step=2
yigindi=0
for i in range(1,num+1,step):
    yigindi+=i
print(yigindi)
for i in range(2,num+1,step):
    yigindi+=1
print(yigindi)