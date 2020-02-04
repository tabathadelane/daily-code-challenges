'''
Task: 
Read two integers and print two lines. The first line should contain integer division,  a//b . The second line should contain float division,  a/b .

You don't need to perform any rounding or formatting operations.

Input Format:
The first line contains the first integer, a. The second line contains the second integer, b.

Output Format:
Print the two lines as described above.

Task 1. get user input
Task 2. convert inputs to int
Task 3. test if conversion is successful
Task 4. divide and print, twice
'''

def divide_two_ways():
    # Task 2
    try:
        # Task 1 and 3
        a = int(input())
        b = int(input())
        # Task 4
        print(a//b)
        print(a/b)
        # python 3 allows float answers by diving two integers. If it didn't, I could convert one of the inputs to a float type to get a float answer on float division. 
    except ValueError:
        divide_two_ways()

divide_two_ways()