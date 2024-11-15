from typing import List

class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        n = len(nums)
        
        for i in range(n):  # Loop until n to include the last element
            for j in range(n):  # Ensure j is always greater than i
                a = abs(i - j)
                b = abs(nums[i] - nums[j])
                if a >= indexDifference and b >= valueDifference:
                    return [i, j]
        
        return [-1, -1]  # Return this only if no valid pair is found
       
    
        