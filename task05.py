start=int(input())
stop=int(input())
if start<stop:
    for ch in range(start,stop+1):
         print(ch)
else:
    for ch in range(start,stop, -1):
        print(ch)