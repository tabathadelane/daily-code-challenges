'''
Task: Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of 2 to 5, print Not Weird
If  is even and in the inclusive range of 6 to 20, print Weird
If  is even and greater than 20, print Not Weird

Input Format:
A single line containing a positive integer 1 > n> 100

Output Format:
Print "Weird" if the number is weird; otherwise, print "Not Weird".
'''

'''
Task 1. I need to determine if the number is odd or even
Task 2. I need to test if even numbers are is in a range given
Task 3. I need to return a print statement
Task 4. I need to ask for user input after testing with hard coded numbers. 
Task 5. The user input must be between 1 and 100

'''

def is_weird(num):
    #  Task 3: I will set the print statement strings to variables because I will be using them more than once. 
    w = "Weird"
    nw = "Not Weird"
    # Task 1: I will test for even and odd. I will do this using the mudulus and the number 2 to test if the remainder is zero. 
    r = num % 2

    if r == 0:
        ''' 
        These numbers are even. Only even number were given ranges to test
         Task 2: I will group conditions with the same result. This gives me the option to test for either Not Weird: "greater than 20 or between 2 and 5" or Weird: "less than 5 or between 6 and 20". I will test for Not Weird simply because these were explicitly asked for in the instructions.
         ''' 
        if num > 20 or 2 <= num <= 5:
            return print(nw)
        else:
            return print(w)
    else:
        # odd and weird are synonyms.
        return print(w)

        


def test_input():
    x = input("Enter a number to test if it is weird: ")  
    try:
        # I want make sure the user followed instructions. 
        x = int(x)
        if 1 <= x <= 100:
            # if the input was a positve number between 1 and 100, I will test if it is weird. 
            return is_weird(x)
        else: 
            x = input("Please enter a positive number 1-100: ")
            return test_input()
    except ValueError:
        # I will keep asking them until they listen
        x = input("Please enter a positive number 1-100: ")
        return test_input()
      
    
    


test_input()