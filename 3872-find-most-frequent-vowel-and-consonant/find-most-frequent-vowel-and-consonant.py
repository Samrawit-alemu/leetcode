class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        s_cnt = Counter(s)
        max_freq_vowel = 0
        max_freq_const = 0
        

        for i,j in s_cnt.items():
            if i in vowels:
                max_freq_vowel = max(max_freq_vowel, j)
            else:
                max_freq_const = max(max_freq_const, j)

        return max_freq_vowel + max_freq_const
        
