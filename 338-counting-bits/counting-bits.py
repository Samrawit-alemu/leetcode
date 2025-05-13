class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n+1):
            cnt = 0

            for j in range(32):
                if i & (1<<j) != 0:
                    cnt +=1
            ans.append(cnt)


            # ans.append(bin(i).count("1"))
            # or
            # ans.append(i.bit_count())
        return ans

