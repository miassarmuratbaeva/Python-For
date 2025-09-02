start=int(input())
stop=int(input())
yigindisi=0
if start<stop:
    for ch in range(start,stop+1):
         yigindisi+=ch
else:
    for ch in range(start,stop, -1):
        yigindisi+=ch
print(yigindisi)