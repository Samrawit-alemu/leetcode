class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        candy_set = set(candyType)
        to_eat = len(candyType)/2
        ans = 0
        if len(candy_set) > to_eat:
            ans = to_eat
        elif len(candy_set) < to_eat:
            ans = len(candy_set)
        else:
            ans = to_eat

        return int(ans)