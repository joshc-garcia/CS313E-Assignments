"""
  File: spiral.py
  Description:

  Student Name: Joshua Garcia
  Student UT EID: jcg4725

  Partner Name:   Partner UT EID:

  Course Name: CS 313E
  Unique Number: 
  Date Created:
  Date Last Modified:

 Input: n is an odd integer between 1 and 100
 Output: returns a 2-D list representing a spiral
         if n is even add one to n

def create_spiral(n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
    
 Input: spiral is a 2-D list and n is an integer
 Output: returns an integer that is the sum of the
         numbers adjacent to n in the spiral
         if n is outside the range return 0
def sum_adjacent_numbers(spiral, n):
    print("REMOVE THIS PRINT AND ADD YOUR CODE")
"""

import math


def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral diameter"""
    if dim % 2 == 0:
        dim += 1

    spiral = [[0 for x in range(dim)] for y in range(dim)]
    grid = [num for num in range(1, dim ** 2 + 1)]

    print(spiral)

    top = 0
    left = 0
    bottom = len(spiral) - 1
    right = len(spiral) - 1
    
    while top <= bottom and left <= right:
        for i in range(left, right + 1):
            spiral[top][i] = grid.pop()
        top += 1
        for i in range(top, bottom + 1):
            spiral[i][right] = grid.pop()
        right -= 1

        if top <= bottom and left <= right:
            for i in range(right, left - 1, -1):
                spiral[bottom][i] = grid.pop()
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                spiral[i][left] = grid.pop()
            left += 1
    
    return spiral

    """Ignore this for now"""
    # max_value = max(grid)

    # current_row = math.ceil(dim / 2) - 1
    # current_column = math.ceil(dim / 2) - 1

    # count = 1
    # jump_index = 1
    # while count <= max_value:
    #     if (current_column > len(spiral)) or (current_row > len(spiral)):
    #         break

    #     spiral[current_row][current_column] = count

    # return spiral

print(create_spiral(3))

def sum_sub_grid(grid, val):
    """
    Input: grid = a 2-D list containing a spiral of numbers
           val is a number within the range of numbers in
           the grid
    Output:
    sum_sub_grid returns the sum of the numbers (including val)
    surrounding the parameter val in the grid
    if val is out of bounds, returns 0
    """
    # ADD YOUR CODE HERE  


    return # ADD YOUR CODE HERE  





# def main():
"""
#     A Main Function to read the data from input,
#     run the program and print to the standard output.
#     """

#     # read the dimension of the grid and value from input file
#     dim = int(input())

#     # test that dimension is odd
#     if dim % 2 == 0:
#         dim += 1

#     # create a 2-D list representing the spiral
#     mat = create_spiral(dim)

#     while True:
#         try:
#             sum_val = int(input())

#             # find sum of adjacent terms
#             adj_sum = sum_sub_grid(mat, sum_val)

#             # print the sum
#             print(adj_sum)
#         except EOFError:
#             break


# if __name__ == "__main__":
#     main()

