def bubbleSort(lst):
    n=len(lst)

    for i in range(0,n):
        for j in range(0,n-i-1):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
    
    return lst


lst=[34,45,54,12,11,34,23]

print("Sorted List Is :",bubbleSort(lst))