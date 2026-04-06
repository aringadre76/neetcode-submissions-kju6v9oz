from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            try:
                stack.append(int(token))
                print(stack)
            except ValueError:
                rOP = stack.pop()
                lOP = stack.pop()

                match token:
                    case "+":
                        stack.append(lOP + rOP)
                    case "*":
                        stack.append(lOP * rOP)
                    case "-":
                        stack.append(lOP - rOP)
                    case "/":
                        stack.append(int(lOP / rOP))
                    case _:
                        print(f"Received invalid token: {token}")
                print(stack)

        print(stack)
        return stack.pop()
