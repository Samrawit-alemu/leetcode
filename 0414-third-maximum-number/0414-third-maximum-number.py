class Solution:
    def thirdMax(self, nums: List[int]) -> int:
   
            # Step 1: Use a set to get unique elements
            unique_nums = set(nums)

            # Step 2: Convert the set back to a list and sort it
            sorted_unique = sorted(unique_nums, reverse=True)

            # Step 3: Check the length of sorted unique numbers
            if len(sorted_unique) < 3:
                return sorted_unique[0]  # Return the maximum if less than 3 distinct
            else:
                return sorted_unique[2]  # Return the third maximum
