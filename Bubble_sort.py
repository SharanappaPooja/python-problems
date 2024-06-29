def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(0,len(arr)-1-i):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]

arr=[5,10,7,23,15]
bubble_sort(arr)
print(arr)