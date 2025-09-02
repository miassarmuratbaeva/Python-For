start=int(input())
stop=16
step=int(input())
if start<stop:
    for ch in range(start,stop,+step ):
         print(ch)
elif start>stop:
    for ch in range(start,stop -2, -1):
        print(ch)