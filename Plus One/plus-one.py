"""
 This function takes a list of digits as an input and adds 1 to it.
 It then converts the list of digits to a string, adds 1 to it and then converts the result back to a list of digits.
 It returns the resulting list of digits.
"""
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # declare an empty list to store the digits
        num = []
        # loop through the list of digits and append each digit to the list
        for digit in digits:
            # convert the digit to a string and append it to the list
            num.append(str(digit))
        # convert the list of digits to a string
        result = int(''.join(num))
        # add 1 to the result
        result = result + 1
        # convert the result to a string
        result_to_str = str(result)
        # clear the list
        num.clear()

        # loop through the result and append each digit to the list
        for i in result_to_str:
            # convert the digit to an integer and append it to the list
            num.append(i)
        # return the list of digits
        return num

        

solution = Solution()
output = solution.plusOne([9])
print(output)