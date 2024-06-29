
#INSERTATION SORT

def insertion_sort(A):
    for i in range(1,len(A)):
        temp=A[i]
        j=i-1
        while j>=0 and temp<A[j]:
            A[j+1]=A[j]
            j-=1
        A[j+1]=temp
A=[7,3,9,1,0,6]
insertion_sort(A)
print(A)