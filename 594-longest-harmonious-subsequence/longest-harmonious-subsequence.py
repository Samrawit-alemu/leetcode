class Solution:
    def findLHS(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        ans = 0
        for x in cnt:
            if x + 1 in cnt:
                ans = max(ans, cnt[x] + cnt[x + 1])
        return ans