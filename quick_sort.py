
#QUICKSORT

def quick(arr,left,right):
    if left<right:
        partition=partition(arr,left,right)
        quick(arr,left,partition-1)
        quick(arr,partition+1,right)

def partition(arr,left,right):
    i=left
    j=right-1
    pivot=arr[right]

    while i<j:
        while i<right and arr[i]<pivot:
            i+=1
        while j>left and arr[j]>=pivot:
            j-=1
        if i<j:
            arr[i],arr[j]=arr[j],arr[i]

    if arr[i]>pivot:
        arr[i],arr[right]=arr[right],arr[i]

    return i
arr=[5,3,7,2,9,0,6]
quick(arr,0,len(arr)-1)
print(arr)
