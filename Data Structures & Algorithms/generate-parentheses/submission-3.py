class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []
        stack = []

        def backtrack(lP, rP):
            if lP == n and rP == n:
                res.append("".join(stack))
                return
            
            if lP < n:
                stack.append("(")
                backtrack(lP+1, rP)
                stack.pop()
            
            if rP < lP:
                stack.append(")")
                backtrack(lP, rP+1)
                stack.pop()
        
        backtrack(0, 0)
        return res
