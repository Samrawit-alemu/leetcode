class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1_set = set(nums1)
        nums2_set = set(nums2)
        ans = []
        a = []
        b = []
        for i in nums1_set:
            
            if i not in nums2_set:
                a.append(i)

        for j in nums2_set:
           
            if j not in nums1_set:
                b.append(j)

            
        ans.append(a)
        ans.append(b)

        return ans

            
            
