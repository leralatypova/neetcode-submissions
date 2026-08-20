class Solution:
    def isValid(self, s: str) -> bool:
        d = {'}' : '{', ')' : '(', ']' : '['}
        stk = []
        for c in s:
            if c=='[' or c=='(' or c=='{':
                stk.append(c)
            else:
                if not stk:
                    return False
                if stk[-1]!=d[c]:
                    return False
                stk.pop()
        return not stk




