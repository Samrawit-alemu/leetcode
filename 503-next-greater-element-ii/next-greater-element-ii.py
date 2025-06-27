class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stk = []
        next_greater = [-1] * len(nums)
        for j in range(2):
            for i in range(len(nums)):
                while stk and nums[stk[-1]] < nums[i] :
                    stk_top = stk.pop()
                    next_greater[stk_top] = nums[i]

                stk.append(i) 

        return next_greater
        