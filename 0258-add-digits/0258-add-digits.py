class Solution:
    def addDigits(self, num: int) -> int:

            while num >= 10:  # Continue until num has only one digit
                num = sum(int(digit) for digit in str(num))  # Sum the digits
            return num

