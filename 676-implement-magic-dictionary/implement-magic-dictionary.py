class MagicDictionary:

    def __init__(self):
        self.word = collections.defaultdict(list)

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            self.word[len(w)].append(w)

    def search(self, searchWord: str) -> bool:
        for w in self.word[len(searchWord)]:
            diff = 0
            
            for c1, c2 in zip(w, searchWord):
                if c1 != c2:
                    diff += 1
                if diff > 1:
                    break
            if diff == 1:
                return True
        return False
          
               



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)