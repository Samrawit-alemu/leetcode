class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True  # Found a duplicate
            seen.add(num)
        return False  # No duplicates found