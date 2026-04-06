class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for t in tokens:
            try:
                stack.append(int(t))
            except ValueError:
                rOP = stack.pop()
                lOP = stack.pop()
                if t == "+":
                    stack.append(lOP + rOP)
                elif t == "-":
                    stack.append(lOP - rOP)
                elif t == "*":
                    stack.append(lOP * rOP)
                elif t == "/":
   
                    stack.append(int(lOP / rOP))

        return stack[0]
