class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:

            # Step 1: Sort the array
            nums.sort()

            # Step 2: Find the target indices
            target_indices = [i for i in range(len(nums)) if nums[i] == target]

            return target_indices