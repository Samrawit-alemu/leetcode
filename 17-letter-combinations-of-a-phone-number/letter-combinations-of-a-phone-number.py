class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'2':['a','b','c'] ,'3':['d','e','f'] ,'4':['g','h','i'] ,'5':['j','k','l'] ,'6':['m','n','o'] ,'7':['p','q','r','s'] ,'8':['t','u','v'] ,'9':['w','x','y','z']}
        # print(mapping[5])
        ans = [""]
        if digits == "":
                return []
        for i in digits:
            
            new_ans = []
            for prefix in ans:
                for char in mapping[i]:
                    new_ans.append(prefix+char)

            ans = new_ans
        return ans
