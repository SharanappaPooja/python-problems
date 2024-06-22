'''

Best Grade :

Andrew has a string N consisting of lowercase English letters representing respective grades of N students 
in his class. His grade is at Pth index. He can swap any two adjacent grades. 
Your task is to help Andrew find and return a string value, representing maximized grade by bringing 
lexicographically smallest character on the Pth index after doing at most K swaps 

Sample Input:
abcdefg 
3 
2 
Sample Output:
a

'''

def maximize_grade(N, P, K):
    P -= 1
    
    grades = list(N)
    n = len(grades)
    
    
    for i in range(P, min(P + K, n - 1)):
        min_index = i
        
        for j in range(i + 1, min(P + K + 1, n)):
            if grades[j] < grades[min_index]:
                min_index = j
        
        for j in range(min_index, i, -1):
            grades[j], grades[j - 1] = grades[j - 1], grades[j]
            K -= 1  #
            if K == 0:
                break
        if K == 0:
            break
    
    return ''.join(grades)


N = "abcdefg"
P = 3
K = 2
print(maximize_grade(N, P, K))  
