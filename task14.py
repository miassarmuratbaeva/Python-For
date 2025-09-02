age=int(input("1-talaba yoshi:"))
yigindi=0
for i in range(2,6):
    age=int(input(f"{i}-talaba yoshi:"))
    yigindi+=age
middle=yigindi/5
print(middle)