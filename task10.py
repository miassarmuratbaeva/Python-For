num=float(input())
mx=num
for i in range(2,8):
    num=float(input(f"{i}-son"))
    if num>mx:
        mx=num
print(mx)