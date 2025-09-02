num=float(input("1-son"))
mx=num
mn=num
for i in range(2,6):
    num=float(input(f"{i}-son"))
    if num>mx:
        mx=num
    if num<mn:
        mn=num
print(mn,mx)