class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        dif = (sum(aliceSizes) - sum(bobSizes)) / 2
        a = set(aliceSizes)
        for i in set(bobSizes):
            if dif + i in a:
                return [dif + i, i] 