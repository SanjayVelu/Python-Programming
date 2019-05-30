a=int(input())
if((a%4)==0 and (a%100)==0 or (a%400)==0):
    print("it is a leap year")
else:
    print("it is a not a leap year")
