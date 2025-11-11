class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # n = len(nums) - 1
        cnt = Counter(nums)
        for i,j in cnt.items():
            if j >= 2:
                return i