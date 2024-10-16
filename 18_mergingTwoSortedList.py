lst1=[1,3,5]
lst2=[2,4,6]
merged=[]
i,j=0,0
while i < len(lst1) and j < len(lst2):
    if lst1[i] < lst2[j]:
        merged.append(lst1[i])
        i=i+1
    else:
        merged.append(lst2[j])
        j=j+1

merged.extend(lst1[i:])
merged.extend(lst2[j:])
print("Merged List is :",merged)