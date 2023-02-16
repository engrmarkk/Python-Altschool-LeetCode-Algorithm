
"""
 This function generates a Pascal's Triangle of the given number of rows. It takes in an integer as an argument and returns a list of lists containing the numbers in the triangle.
 The first two rows are hard-coded as [1] and [1,1] and then the remaining rows are calculated using the numbers from the previous row.
 The result is returned as a list of lists.
"""

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        # Hard-coding the first two rows
        nums = [[1], [1,1]]

        # If numRows is 1 or 2, return the hard-coded list
        if numRows == 1:
            # return [[1]]
            return [[1]]
        # if numRows == 2:
        elif numRows == 2:
            # return [[1], [1,1]]
            return [[1], [1,1]]
        # If numRows is greater than 2, calculate the remaining rows
        else:
            # Loop through the remaining rows
            for i in range(1, numRows - 1):
                # Create a new list to store the numbers in the current row
                new = list()
                # Loop through the numbers in the previous row
                for j in range(len(nums[i]) - 1):
                    # Calculate the sum of the two numbers in the previous row and append it to the new list
                    n = nums[i]
                    m = n[j] + n[j + 1]
                    new.append(m)
                # Append 1 to the beginning and end of the new list
                new.insert(0, 1)
                new.append(1)
                nums.append(new)

        # Return the list of lists
        return nums

solution = Solution()
output = solution.generate(4)
print(output)
