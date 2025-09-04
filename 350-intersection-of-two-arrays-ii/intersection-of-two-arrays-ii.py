class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1_cnt = Counter(nums1)
        nums2_cnt = Counter(nums2)
        ans = []
        for num in nums1_cnt:
            if num in nums2_cnt:
                count = min(nums1_cnt[num], nums2_cnt[num])
                ans.extend([num] * count)

        return ans


