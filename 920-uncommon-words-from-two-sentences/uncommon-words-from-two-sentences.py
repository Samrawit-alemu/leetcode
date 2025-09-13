class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1_list = s1.split()
        s2_list = s2.split()
        s1_cnt = Counter(s1_list)
        s2_cnt = Counter(s2_list)
        uncommon = []
        for i in s1_cnt:
            # print(s1_cnt[i])
            if s1_cnt[i] == 1 and s2_cnt[i] == 0:
                uncommon.append(i)
        for j in s2_cnt:
            if s2_cnt[j] == 1 and s1_cnt[j] == 0:
                uncommon.append(j)
        return uncommon
        