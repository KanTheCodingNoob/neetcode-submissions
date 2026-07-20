class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        hashset = {'+', '-', '*', '/'}
        stack = []
        for t in tokens:
            if t in hashset:
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(self.calc(num1, num2, t))
            else:
                stack.append(int(t))
                
        return stack[0]

    def calc(self, num1, num2, sym):
        if sym == '+':
            return num1 + num2
        elif sym == '-':
            return num1 - num2
        elif sym == '*':
            return num1 * num2
        elif sym == '/':
            return int(num1 / num2)