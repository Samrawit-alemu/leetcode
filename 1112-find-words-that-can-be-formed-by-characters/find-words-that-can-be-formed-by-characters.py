class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        chars_cnt = Counter(chars)
        for i in words:
            word_cnt = Counter(i)
            is_good_word = True
            for j,k in word_cnt.items():
                if chars_cnt[j] < k:
                    is_good_word = False
                    break

            if is_good_word:
                ans += len(i)
        return ans
                
