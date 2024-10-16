def insertionsort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1
        while j >= 0 and key < arr[j]:
           arr[j+1] = arr[j]
           j-=1
        arr[j+1]=key   
    return arr               

lst=[67,45,4,23,24,12,-12,79,-90]
print("insertin Algo Sorted List :",insertionsort(lst))