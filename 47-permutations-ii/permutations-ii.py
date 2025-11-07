class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, sol = [], []

        def backtrack():
            if len(sol) == n:
                res.append(sol[:])
                return
            for i in range(n):
                if i in sol_indices:
                    continue
                sol_indices.add(i)
                sol.append(nums[i])
                backtrack()
                sol.pop()
                sol_indices.remove(i)
        sol_indices = set()
        backtrack()

        set1 = set(tuple(x) for x in res)
        ans = list(map(list, set1))
        return ans
