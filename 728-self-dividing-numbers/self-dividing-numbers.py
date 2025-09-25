class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        # Helper function to check if a number is self-dividing
        def self_dividing(n: int) -> bool:
            for d in str(n):
                if d == "0" or n % int(d) > 0:
                    return False
            return True

        """
        def self_dividing(n: int) -> bool:
            x = n
            while x > 0:
                d = x % 10
                if d == 0 or (n % d) > 0:
                    return False
                x //= 10
            return True
        """

        # List to store self-dividing numbers
        ans = []

        # Iterate over the range and find self-dividing numbers
        for n in range(left, right + 1):
            if self_dividing(n):
                ans.append(n)

        # Alternatively: return list(filter(self_dividing, range(left, right + 1)))
        return ans