class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        maxx = max(cnt.values())
        #
        return sum(freq for freq in cnt.values() if freq == maxx)