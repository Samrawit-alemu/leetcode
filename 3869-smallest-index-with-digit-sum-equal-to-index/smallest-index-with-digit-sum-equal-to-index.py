class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        summ = [sum(int(digit) for digit in str(num)) for num in nums ]
        for i in range(len(nums)):
            if i == summ[i]:
                return i
            
        return -1