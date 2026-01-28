class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1
      
        for k,v in cnt.items():
            if v == 1:
                return k
