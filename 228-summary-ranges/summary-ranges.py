class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        if not nums:
            return result
        a = nums[0]
        for i in range(1, len(nums)):
            if nums[i] != nums[i-1] + 1:
                if a == nums[i-1]:
                    result.append(str(a))
                else:
                    result.append(f"{a}->{nums[i-1]}")
                a = nums[i]
        if a == nums[-1]:
            result.append(str(a))
        else:
            result.append(f"{a}->{nums[-1]}")

        return result
                
        
