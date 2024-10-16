lst=[20,30,45,67,56]
# lent=len(lst)

# maximum = lst[0]
# secondMax=lst[0]

# for i in range(1,lent):
#     if lst[i]>maximum:
#         maximum=lst[i]
# print("largest element is ", maximum)

# for i in range(1,lent):
#     if lst[i]>secondMax and secondMax<maximum:
#         secondMax = lst[i]          
# print("second largest element is : ",secondMax)

lst.sort().max()