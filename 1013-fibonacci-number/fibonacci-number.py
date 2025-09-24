class Solution:
    def fib(self, n: int) -> int:
        memo = defaultdict()
        def fib_num(n):
            if n == 0 or n == 1:
                return n
            if n not in memo:
                memo[n] = fib_num(n-1) + fib_num(n-2)
            return memo[n]
        return fib_num(n)
