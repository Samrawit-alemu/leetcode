class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)/2
        freq= Counter(nums)

        for i,j in freq.items():
            if j == n:
                return i
             