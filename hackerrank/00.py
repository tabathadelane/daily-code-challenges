
a = ["a", "b", "c", "d", "e", "f",]
d= = 2

'''
Input:
a = ["a", "b", "c", "d", "e", "f",]
i = 0,   1,   2,   3,   4,   5,
I would first identify the indexes and compare how that number relates to the number of rotations

d = 2

Output
b = ["c", "d", "e", "f", "a", "b",]
i =   2,   3,   4,   5,   0,   1,   
I would then visualize what the list should look like after the rotation and compare indexes to the first list
I can now see that the new list should begin at i = 2 which == to d
I can determine that I sould need to split this list and move everything before d to the end of the list

The final step is to print the list as a string of letters with a single space between, so I can join them together in the currect order with a whitespace between
'''


def rotLeft(a,d):
  output1 = a[d:]
  output2 = a[:d]
  string = " ".join(output1 + output2)
  return string
print(rotLeft(a,d))