class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def dfs():
            tk = tokens.pop()
            if tk not in "+-*/":
                return int(tk)
            
            right = dfs()
            left = dfs()

            if tk == '+':
                return left + right
            elif tk == '-':
                return left - right
            elif tk == '*':
                return left * right
            elif tk == '/':
                return int(left / right)
            
        return dfs()