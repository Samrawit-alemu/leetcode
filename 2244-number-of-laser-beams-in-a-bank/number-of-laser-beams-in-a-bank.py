class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        num_1 = []
        res = 0
        for i in bank:
            cnt = i.count('1')
            num_1.append(cnt)
        filtered = [x for x in num_1 if x>0]

        for j in range(1, len(filtered)):
            res += filtered[j-1] * filtered[j]
        return res
        
