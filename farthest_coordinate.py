""""
Arduino:

Tom is an Arduino Programmer. He has designed a program to run his robocar on a
horizontal number line. Initially, the car is parked at: 0.
Given an array A of N integers which can be A. B. C... the robocar runs as follows as per the
designed program
First the robocar moves A units in specified direction(right in case the integer is positive and
left if the integer is negative).
Then robocar first moves A units and then B units in a specified direction.
In the next step, the robocar moves A units. B units, and then C units in a specified direction.
This process keeps on repeating as per the number of integers in the sequence..
Your task is to find and retum an integer value, representing the farthest coordinate reached
by the robocar from the beginning to the end of the process.

Sample Input:
1 -2 3 4
Sample Output:
6 
"""

def farthest_coordinate(A):
    current_position = 0
    max_position = 0
    
    for i in A:
            current_position += i
            if current_position > max_position:
                max_position = current_position
    return max_position

A = [1, -2, 3, 4]
output = farthest_coordinate(A)
print(f"The farthest coordinate reached by the robocar is: {output}")



