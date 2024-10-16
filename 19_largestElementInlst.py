lst=[23,45,67,7,8,11111,90]
lent=len(lst)
max=lst[0]
for i in range(1,lent):
  if lst[i]>max:
    max=lst[i]

print("largest element n the list is :",max)