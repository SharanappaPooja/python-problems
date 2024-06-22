'''
Chocolate jar :

You are given an integer array of size N, representing jars of chocolates. Three students A, B, 
and C respectively, will pick chocolates one by one from each chocolate jar, till the jar is 
empty, and then repeat the same with the rest of the jars. Your task is to fine and return an 
integer value representing the total number of chocolates that student A will have, after all 
the chocolates have been picked from all the jars. 
Note: Once a jar is done A will start taking the chocolates from the new jar. 

Input Format :
input1: An integer array representing the quantity of chocolates in each jar. input2: An 
integer value N representing the number of jars. 

Output Format:
Return an integer value representing the total number of chocolates that student A will 
have, after all the chocolates are picked. 

Example:
Input:
10 20 30 3 
Output: 
21 
Explanation:
Jar 1: 10 chocolates -> A-4, B-3,C-3 
Jar 2: 20 chocolates -> A-7, B-7, C-6 Jar 3: 30 
chocolates -> A-10, B-10,C-10 so A gets a 
total of 4+7+10=21 chocolates.

'''
def chocolates_for_student_A(chocolates, N):
    if N == 0:
        return 0
    
    A_chocolates = 0
    A_index = 0
    A_mod = 3  
    
    for chocolates_in_jar in chocolates:
        if chocolates_in_jar == 0:
            continue
        
        A_pick = min(chocolates_in_jar, A_mod - A_index)
        A_chocolates += A_pick
        
        chocolates_in_jar -= A_pick
        B_pick = min(chocolates_in_jar, A_mod)
        chocolates_in_jar -= B_pick
        C_pick = min(chocolates_in_jar, A_mod)
        chocolates_in_jar -= C_pick
        
        A_index = (A_index + A_pick + B_pick + C_pick) % A_mod
    
    return A_chocolates


chocolates = [10, 20, 30, 3]
N = len(chocolates)
result = chocolates_for_student_A(chocolates, N)
print(result)  
