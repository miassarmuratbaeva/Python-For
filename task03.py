start=int(input())
stop=16
if start<stop:
    for ch in range(start,stop):
         print(ch)
elif start>stop:
    for ch in range(start,stop -2, -1):
        print(ch)