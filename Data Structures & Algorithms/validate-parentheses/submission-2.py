class Solution:
    def isValid(self, s: str) -> bool:
        left = ['(', '{', '[']
        right = [')', '}', ']']
        pair1='()'
        pair2 = '{}'
        pair3 = '[]'

        stack = []
        for char in s:
            if char in left:
                stack.append(char)
            elif char in right:
                if len(stack) != 0:
                    pair = stack.pop() + char
                    print(pair)
                    if not (pair == pair1 or pair == pair2 or pair == pair3):
                        return False
                else:
                    return False
                

        if len(stack) != 0:
            return False
        
        return True