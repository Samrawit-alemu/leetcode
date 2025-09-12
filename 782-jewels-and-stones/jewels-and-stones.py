class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        stones_cnt = Counter(stones)
        ans = 0
        # print(stones_cnt)
        for i in jewels:
            if i in stones_cnt:
                ans += stones_cnt[i]
        return ans