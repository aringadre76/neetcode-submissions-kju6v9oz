class Solution:
    def isValid(self, s: str) -> bool:
        valid = {')': '(', ']': '[', '}': '{'}

        stack = []

        for char in s:
            if char in valid.values(): # left
                stack.append(char)
            elif char in valid.keys(): # right
                if len(stack) == 0: return False
                matched = stack.pop() # matching left
                print(valid[char],  matched)
                
                if valid[char] != matched: 
                    return False
        if len(stack) != 0: return False
        return True