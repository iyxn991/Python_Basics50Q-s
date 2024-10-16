num=7

is_prime=True
for i in range(2,num): # i will start at 2 , ending rnage is number which is 7 s loops will go till 6
    if num%i==0: # 7%2 = 0.14
        is_prime=False
        break
if is_prime:
    print("Prime NUMber")
else:
    print("Not a Prime NUber")   