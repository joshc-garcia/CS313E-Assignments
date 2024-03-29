"""
  File: spiral.py
  Description: Program that creates a spiral in a 2D array. Calculates
  the sum of the values that surround a specified number.
  Student Name: Joshua Garcia
  Student UT EID: jcg4725
  Partner Name: Odette Saenz
  Partner UT EID: oss286
  Course Name: CS 313E
  Unique Number: 50775
  Date Created: 1/22/2024
  Date Last Modified: 1/23/2024
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
def create_spiral(dim):
    """Creates a Spiral given a dimension for the spiral diameter"""
    # Initializes spiral that will be appended with values from grid.
    spiral = [[0 for x in range(dim)] for y in range(dim)]
    grid = list(range(1, dim ** 2 + 1))
    #Boundary conditions for the spiral
    top = 0
    left = 0
    bottom = dim - 1
    right = dim - 1
    # Loop that prints out spiral from outside to in, going in a
    # counterclockwise direction. Inspiration was retrieved from URL:
    # https://www.prepbytes.com/blog/python/spiral-traversal-of-a-matrix-in-
    # python/
    # len(spiral + 1) // 2 calculates the "rings" of the spiral
    for _ in range((len(spiral) + 1) // 2):
        # Prints the top row from right to left
        for i in range(right, left - 1, -1):
            spiral[top][i] = grid.pop()
        top += 1
        # Prints left column from top to bottom.
        for i in range(top, bottom + 1):
            spiral[i][left] = grid.pop()
        left += 1
        if top <= bottom and left <= right:
            # Prints bottom column from left to right
            for i in range(left, right + 1):
                spiral[bottom][i] = grid.pop()
            bottom -= 1
            # Prints right column from bottom to top.
            for i in range(bottom, top - 1, -1):
                spiral[i][right] = grid.pop()
            right -= 1
    return spiral
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
    #calculates rows and columns for grid
    row = len(grid)
    if row == 0:
        return 0
    col = len(grid[0])
    if col == 0:
        return 0
    # Dictionary with directions adjacent to the number
    directions = {
        "up": (-1, 0),
        "down": (1, 0),
        "left": (0, -1),
        "right": (0, 1),
        "upperLeft": (-1, -1),
        "upperRight": (-1, 1),
        "lowerLeft": (1, -1),
        "lowerRight": (1, 1)
    }
        # Iterate through each row and column of the grid to find the value.
        # If the value exists, find the value of all adjacent numbers
        # add them to the running total if they are within bounds
    #Finds position of starting, given value
    start_position = None
    for i in range(row):
        for j in range(col):
            if grid[i][j] == val:
                start_position = (i,j)
                break #exit loop when index starting position (index of col) is found
        if start_position:
            break #exit loop when index starting position (index of row) is found
    #If value is not found, retun 0 (out of bounds)
    if not start_position:
        return 0
    #Calculates the total sum of adjacent numbers to starting value
    total = 0
    for slope_x, slope_y in directions.values():
        x_coordinate, y_coordinate = start_position[0]+ slope_x, start_position[1] + slope_y
        if 0 <= x_coordinate < row and 0 <= y_coordinate < col:
            total += grid[x_coordinate][y_coordinate]
    #add starting value to total
    return total
def main():
    """
    #     A Main Function to read the data from input,
    #     run the program and print to the standard output.
    #     """
    # read the dimension of the grid and value from input file
    dim = int(input())
    # test that dimension is odd
    if dim % 2 == 0:
        dim += 1
    # create a 2-D list representing the spiral
    mat = create_spiral(dim)
    while True:
        try:
            sum_val = int(input())
            # find sum of adjacent terms
            adj_sum = sum_sub_grid(mat, sum_val)
             # print the sum
            print(adj_sum)
        except EOFError:
            break
if __name__ == "__main__":
    main()
