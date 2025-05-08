class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        def atmost(x):
            if x < 0 : return 0

            curr = 0
            l = res = 0
            for r in range(len(nums)):
                curr += nums[r]

                while curr > x:
                    curr -= nums[l]
                    l += 1

                res += (r - l + 1)
            return res
        return atmost(goal) - atmost(goal-1) 