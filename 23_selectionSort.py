def selectionSort(arr):
    for i in range(len(arr)):
        min_idx=i
        for j in range(i+1,len(arr)-1):
            if arr[j] < arr[min_idx]:
                min_idx=j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr 

        
arr=[23,34,45,67,12,13,11,1,34,87]
print("Sorted List Using Selection SOrt list : ",selectionSort(arr))        