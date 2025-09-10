class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        concatenate1 = ''
        concatenate2 = ''

        for i in word1:
            concatenate1 += i
        # print(concatenate1)
        for i in word2:
            concatenate2 += i
        # print(concatenate2)

        if concatenate1 == concatenate2:
            return True
        return False

        
