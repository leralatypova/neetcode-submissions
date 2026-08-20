class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = {
            '+' : lambda a, b: a+b,
            '*' : lambda a, b: a*b,
            '-' : lambda a, b: a-b,
            '/' : lambda a, b: int(a/b)
        }
        stack = []
        for i in tokens:
            if i not in '+-*/':
                stack.append(int(i))
            else:
                a = stack.pop()
                b = stack.pop()
                stack.append(op[i](b, a))
        return stack[-1]

              
