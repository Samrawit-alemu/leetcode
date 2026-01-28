class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        

        if len(nums) < 3:
            return 0

        d = [nums[i + 1] - nums[i] for i in range(len(nums) - 1)]
        r = 0

        for _, g in groupby(d):
            k = len(list(g))
            r += k * (k - 1) // 2

        return r