class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        indices = [i for i,j in enumerate(s) if j == c ]
        cnt = 0
        ans = []
    
        for i in range(len(s)):
            if s[i] == c:
                cnt += 1
                ans.append(0)

            elif cnt == 0:
                ans.append(abs(i-indices[0]))
            elif cnt > 0 and cnt < len(indices):
                if abs(i-indices[cnt-1]) < abs(i-indices[cnt]):
                    ans.append(abs(i-indices[cnt-1]))
                else:
                    ans.append(abs(i-indices[cnt]))
            elif cnt == len(indices):
                ans.append(abs(i-indices[cnt-1]))
            
        return ans

