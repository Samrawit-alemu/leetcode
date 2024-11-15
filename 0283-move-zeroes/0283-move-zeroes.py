            
from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Pointer for the position to place the next non-zero element
        non_zero_index = 0
        
        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[non_zero_index] = nums[i]
                non_zero_index += 1
        
        # Fill the remaining part of the array with zeros
        for i in range(non_zero_index, len(nums)):
            nums[i] = 0

