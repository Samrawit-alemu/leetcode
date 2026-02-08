class Solution(object):
    def optimalDivision(self, nums):
        if len(nums) == 1:
            return str(nums[0])
        if len(nums) == 2:
            return "{}/{}".format(nums[0], nums[1])
        return "{}/({})".format(nums[0], "/".join(map(str, nums[1:])))