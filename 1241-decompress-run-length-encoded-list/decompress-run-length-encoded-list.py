class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(0,len(nums),2):
            a = nums[i]
            while a > 0:
                ans.append(nums[i+1])
                a -= 1

        return ans