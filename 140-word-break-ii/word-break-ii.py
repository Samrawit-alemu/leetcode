class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(start):
            if start == len(s):
                return [""]  # End of string — valid sentence

            if start in memo:
                return memo[start]

            sentences = []
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]
                if word in word_set:
                    # Get all possible sentences from the remaining substring
                    for sub in dfs(end):
                        if sub:
                            sentences.append(word + " " + sub)
                        else:
                            sentences.append(word)
            memo[start] = sentences
            return sentences

        return dfs(0)
