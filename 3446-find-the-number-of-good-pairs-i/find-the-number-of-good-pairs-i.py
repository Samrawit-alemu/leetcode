class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = 0
        for i in nums2:
            mult = i * k
            for j in nums1:
                if j % mult == 0:
                    ans += 1
        return ans
