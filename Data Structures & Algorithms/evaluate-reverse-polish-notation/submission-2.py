class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]

        for tk in tokens:
            if tk ==  "+":
                stack.append(stack.pop() + stack.pop())
            elif tk ==  "-":
                a,b =stack.pop(), stack.pop()
                stack.append(b-a)
            elif tk ==  "*":
                stack.append(stack.pop() * stack.pop())
            elif tk ==  "/":
                a,b =stack.pop(), stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(tk))
        return stack[0]