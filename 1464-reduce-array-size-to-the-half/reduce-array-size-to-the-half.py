class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        cnt = Counter(arr)
        freq = list(cnt.values())
        freq.sort()

        ans, removed, half = 0,0,len(arr)//2
        while removed < half:
            ans += 1
            removed += freq.pop()

        return ans

