class Solution:
    def partition(self, s: str) -> List[List[str]]:

        result = []
        
        def backtrack(start, path):
            # Base Case
            if start == len(s):
                result.append(list(path))
                return

            # Explore all possible substrings starting from 'start'
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                
                # Check if the current substring is a palindrome (using slicing)
                if substring == substring[::-1]:
                    # Action: Add substring to the current partition
                    path.append(substring)
                    
                    # Recurse: Move the start point to the end of this substring
                    backtrack(end, path)
                    
                    # Backtrack: Remove the substring to try the next possible cut
                    path.pop()

        backtrack(0, [])
        return result
