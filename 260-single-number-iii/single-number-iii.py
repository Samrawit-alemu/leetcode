class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        cnt = defaultdict(int)
        ans = []
        for i in nums:
            cnt[i] += 1
        for k,v in cnt.items():
            if v == 1:
                ans.append(k)
        return ans