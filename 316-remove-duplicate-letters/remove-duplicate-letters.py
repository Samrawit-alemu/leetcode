class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stk = []
        last_occur = {letter:i for i, letter in enumerate(s)}

        seen = set()

        for i, letter in enumerate(s):
            if letter not in seen:

                while stk and stk[-1] > letter and last_occur[stk[-1]] > i:
                    seen.remove(stk.pop())

                seen.add(letter)
                stk.append(letter)
        return "".join(stk)