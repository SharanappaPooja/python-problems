'''
Advance sub array problem:

You are competing in a basketball contest. In this contest the score for each successful shot 
depends on both the distance from the basket and the player's position. The ball is shot N 
times, successfully. You are given an array A containing the distance of a player from basket 
for N shots. The index of array represents the position of the player. Score is calculated by 
multiplying the position with the distance from the basket. 
Your task is to find and return an integer value, representing the maximum possible score 
you can achieve by choosing a contiguous subarray of size K from the given array. 

Note:
* A subarray is a contiguous part of array. 
* Assume 1 based indexing. 
* The array contains both negative and positive values. 
* Assume the player is standing on a cartesian plane. 

Input Format
- input1:An integer value N representing the number of shots made by the player 
- input2 : An integer K representing the size of subarray 
- input3 : An array of integers 

Sample Input
5 
2 
1 2 3 4 5 

Sample Output
14 

'''
#method 1
def max_score(N, K, A):
    if K > N:
        return 0
    
    current_sum = sum((i + 1) * A[i] for i in range(K))
    max_sum = current_sum
   
    for i in range(K, N):
        current_sum += (i + 1) * A[i] - (i - K + 1) * A[i - K]
        if current_sum > max_sum:
            max_sum = current_sum
    
    return max_sum


N = 5
K = 2
A = [1, 2, 3, 4, 5]
print(max_score(N, K, A))  

#method 2
def array():
    lst=[]
    for i in range(0,n):
        x=i*l[i]
        lst.append(x)
    print(lst)

    cur=0
    for i in lst:
        for j in (i+1,lst):
            if (i+j)>cur:
                cur=lst[i]+lst[j]
    print(cur)


l=[]
n=int(input("Enter the number of  shots: "))
k=int(input("enter the subarray size: "))
for i in range(n):
    a=int(input("Enter the position of player: "))
    l.append(a)
print(l)
array()
