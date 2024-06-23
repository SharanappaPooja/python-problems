"""""
 Space Counter
You have been given the task of making the content on a social media platform more userfriendly. Your task is to find and return an integer value representing the count of the
number of spaces in a given string S.
Input: A
string S
Output :
Return an integer value representing the count of the number of spaces in a given string S.
Example:
Input: Hello
World Hey
Output:
2
"""


def count_spaces(S):
    return S.count(' ')

# Example usage:
input_string = "Hello World Hey"
output = count_spaces(input_string)
print(f"The number of spaces in the input string is: {output}")
