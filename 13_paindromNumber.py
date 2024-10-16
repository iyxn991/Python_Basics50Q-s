num=1211
temp = num
rev=0
while temp>0:
    ld=temp%10
    rev=rev*10+ld
    temp=temp//10
if rev==num:
    print("number is palidnrom")
else:
    print(" number is not palindrom")

