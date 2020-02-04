'''
Task: Read two integers from STDIN and print three lines where:

    The first line contains the sum of the two numbers.
    The second line contains the difference of the two numbers (first - second).
    The third line contains the product of the two numbers.

Input Format:
The first line contains the first integer, "a". The second line contains the second integer, "b".

Constraints:
1 <= a <= 10^10
1 <= b <= 10^10

Task 1. Test if user input can be successfully converted to an int type
Task 2. Test if the integer meets the above constraints
Task 3. Return the statements if everything is true. 
'''

def print_three_lines():
    # The only way to test if the input string can be an int without breaking the code is to run a try and except to catch a ValueError which will run the program again if you want. 
    try:
        a = int(input())
        b = int(input())
        # i am adding the input and int converstion on the same line for tidiness. 
        if 1 <= a <= 10**10 and 1 <= b <= 10**10  :
            # these were the only constraints given. if success, move on to simple and seperate print statements
            print(a + b)
            print(a - b)
            print(a * b)
    except ValueError:
        print_three_lines()
        
print_three_lines()