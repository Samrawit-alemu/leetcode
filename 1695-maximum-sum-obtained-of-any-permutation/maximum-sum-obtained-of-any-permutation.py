class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        freq = [0] * (n + 1)
        for l, r in requests:
            freq[l] += 1
            freq[r + 1] -= 1
        freq = list(accumulate(freq))[:-1]  
        nums.sort(reverse=True)
        freq.sort(reverse=True)
        return sum(a * b for a, b in zip(nums, freq)) % MOD