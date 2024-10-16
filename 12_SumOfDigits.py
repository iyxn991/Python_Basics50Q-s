num=1234

total=0
while num>0:
    total = total+num%10 # 0=0+1234%10 = 4, 4=4+3=7, 7=7+2=9 .. ..
    num//=10
print("Sum of Digits is : ",total)
