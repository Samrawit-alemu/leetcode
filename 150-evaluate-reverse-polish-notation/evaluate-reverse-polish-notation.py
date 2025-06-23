class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []

        for i in tokens:
            if i !='+' and i !='-' and i !='*' and i !='/':
                stk.append(i)
            else:
                b = stk.pop()
                a = stk.pop()
                if i == '+':
                    c = int(a) + int(b)
                    stk.append(c)
                elif i == '-':
                     c = int(a) - int(b)
                     stk.append(c)
                elif i == '*':
                     c = int(a) * int(b)
                     stk.append(c)
                elif i == '/':
                    c = int(a) / int(b)
                    stk.append(c)
                
            
                

        return int(stk[-1])
        
        