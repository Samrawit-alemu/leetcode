class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        sort_score = sorted(score, reverse = True)
        n = len(score)
        ans = ["" for _ in range(n)]

        for i in range(n):
            if i == 0:
                ans[score.index(sort_score[i])] = "Gold Medal"
            elif i== 1:
                ans[score.index(sort_score[i])] = "Silver Medal"
            elif i == 2:
                ans[score.index(sort_score[i])] = "Bronze Medal"

            else:
                ans[score.index(sort_score[i])] = str(i+1)
        
        return ans
