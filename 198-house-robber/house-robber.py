class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def dp(i):
            # base case
            if i == 0 :
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i not in memo:
                rob = nums[i] + dp(i-2)
                dont_rob = dp(i-1)
                memo[i] = max(rob, dont_rob)
            return memo[i]

        return dp(len(nums)-1)
        
        