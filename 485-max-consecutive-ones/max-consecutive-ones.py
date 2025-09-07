class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        for i in nums:
            if i:
                cur += 1
                if cur > res:
                    res = cur
            else:
                cur = 0
        return res