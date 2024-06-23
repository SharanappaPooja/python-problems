"""""
Finding commas
Liam works as a data analyst for a company that stores massive amounts of numerical data. He has been
tasked with determining how many commas are used when writing numbers in the range of 1 to N
(inclusive) in a specific format
In this format, if numbers are more than four digits long, commas are used to separate the numbers into
groups of three, starting from the right for the representation of the number. Your task is to help Liam find
and return an integer value, representing the total number of commas used when writing each integer in the
range of 1 to N
Input Specification:
Input: An integer value N. representing the number range.
Output Specification:
Return an integer value, representing total number of commas used when writing each integer in the range
of 1 to N.
Sample Input:
5000
Sample Output:
4001 
"""

def count_commas_in_range(N):
    total_commas = 0
    for num in range(1, N + 1):
        num_str = str(num)
        length = len(num_str)
        
        if length > 3:
            num_commas = (length - 1) // 3
            total_commas += num_commas
    
    return total_commas

N = 5000
output = count_commas_in_range(N)
print(f"The total number of commas used for numbers from 1 to {N} is: {output}")
