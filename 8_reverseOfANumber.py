num=4567

rev=0
while num>0:
    remiander=num%10  
    #to get the last digit out of complete number -> 4567/10 = 7 as remainder
    rev=rev*10+remiander
     # rev = 0*10+7 = 7 after 1st iteration,
    num=num//10 
    #4567/10 = 456.7 roundup is 456
print("Reverse of the Number is :",rev)


 