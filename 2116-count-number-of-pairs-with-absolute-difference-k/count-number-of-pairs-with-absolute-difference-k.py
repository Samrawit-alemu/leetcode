class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        ans = 0
        for i in nums:
            for j in nums:
                if abs(i-j) == k:
                    ans += 1
        return int(ans/2)