class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        ans = []
        for word in strs:
            sorted1 = ''.join(sorted(word))
            mp[sorted1].append(word)

        return list(mp.values())