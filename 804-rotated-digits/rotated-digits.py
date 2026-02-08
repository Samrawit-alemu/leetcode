class Solution:
    def rotatedDigits(self, n: int) -> int:
        num = list(map(int, str(n)))
        @cache
        def dp(pointer: int, strict: bool, good: bool) -> int:
            if pointer == len(num): return int(good)

            res = 0
            bound = num[pointer] if strict else 10
            for i in [0, 1, 8]:
                if i < bound: res += dp(pointer + 1, False, good)
                elif i == bound: res += dp(pointer + 1, True, good)
            
            for i in [2, 5, 6, 9]:
                if i < bound: res += dp(pointer + 1, False, True)
                elif i == bound: res += dp(pointer + 1, True, True)
 
            return res

        return dp(0, True, False)