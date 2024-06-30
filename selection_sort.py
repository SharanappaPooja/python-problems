
#SELECTION SORT
def selection_sort(B):
    for i in range(0,len(B)-1):
        min_index=i
        for j in range(i+1,len(B)):
            if B[j]<B[min_index]:
                min_index=j
            if B[j]!=i:
                B[i],B[min_index]=B[min_index],B[i]

B=[2,8,5,4,9,7]
selection_sort(B)               
print(B)