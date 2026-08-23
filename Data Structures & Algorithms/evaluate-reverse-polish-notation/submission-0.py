class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for tk in tokens:
            if tk not in "+-*/":                
                stack.append(int(tk))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                match tk:
                    case "+":
                        stack.append(op2 + op1)
                    case "-":
                        stack.append(op2 - op1)
                    case "*":
                        stack.append(op2 * op1)
                    case "/":
                        stack.append(int(op2 / op1))
        return stack[0]