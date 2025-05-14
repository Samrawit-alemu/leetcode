class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = 2 ** len(nums)
        ans = []

        for num in range(0,n):
            temp = []

            for i in range(32):
                if num & (1<<i) != 0: # test if ith index is 0 or 1
                    temp.append(nums[i])
            ans .append(temp)
        return ans
