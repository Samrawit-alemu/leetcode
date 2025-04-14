class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max1 = max(candies)
        return [(cur + extraCandies >= max1) for cur in candies]