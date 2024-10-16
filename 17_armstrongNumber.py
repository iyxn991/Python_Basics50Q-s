num=151
temp =num
total=0
while temp>0:
    last_dgit=temp%10
    total=total+last_dgit**3
    temp=temp//10
if total==num:
    print("Numbe is Armstrong")
else:
    print("Number is nOt Armstrong")    