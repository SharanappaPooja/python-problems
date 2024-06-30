
#MERGESORTING

def merge(array):
    if len(array)>1:
        left_arr=array[0:len(array)//2]
        right_arr=array[len(array)//2:]

        merge(left_arr)
        merge(right_arr)

        i=0
        j=0
        k=0

        while i<len(left_arr) and j<len(right_arr):
            if left_arr[i]<right_arr[j]: 
                array[k]=left_arr[i]
                i +=1
            else:
                array[k]=right_arr[j]
                j +=1
            k +=1
        
        while i <len(left_arr):
            array[k]=left_arr[i]
            i+=1
            k+=1
        
        while j<len(right_arr):
            array[k]=right_arr[j]
            j+=1
            k+=1

array=[5,3,7,1,8,2,0]
merge(array)
print(array)