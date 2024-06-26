"""""
Math test:

Alice has a mathematics test for which she is underprepared. She has to do at least one
question correctly to pass the test. He decides to do a question which needs her to find the
smallest prime number which is larger than a given integer N. Your task is to find and return
an integer value representing the smallest prime number larger than N.

Input Format:
input1: An integer value N
Output Format:
Return an integer value representing the smallest prime number larger than N.
Sample Input
6
Sample Output
7 

"""

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2,(num//2)+1):
        if num%i==0:
            return False
    return True

def next(N):
    can=N+1
    while not is_prime(can):
        can+=1
    return can    


N = int(input('Enter the number: '))
output = next(N)
print(f"The smallest prime number larger than {N} is: {output}")
