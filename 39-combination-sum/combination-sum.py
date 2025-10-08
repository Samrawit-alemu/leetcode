class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return 

            if total > target or idx >= len(candidates):
                return 

            comb.append(candidates[idx])
            backtrack(idx, comb, total + candidates[idx])
            comb.pop()
            backtrack(idx+1, comb, total)

            return res
        
        return backtrack(0, [], 0)