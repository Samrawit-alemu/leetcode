class Solution:
    def findLucky(self, arr: List[int]) -> int:
        arr_cnt = Counter(arr)
        ans = [-1]
        for i, j in arr_cnt.items():
            if i == j:
                ans.append(i)
        return max(ans)
        # return -1