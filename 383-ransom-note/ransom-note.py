class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        for i, j in ransomNote_freq.items():
            if magazine_freq[i] < j:
                return False

        return True