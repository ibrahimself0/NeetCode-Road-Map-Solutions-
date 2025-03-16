class Solution(object):
    def evalRPN(self, tokens):
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(int(stack.pop()) + int(stack.pop()))
            elif i == "-":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(num2 - num1)
            elif i == "*":
                stack.append(int(stack.pop()) * int(stack.pop()))
            elif i == "/":
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(int(num2 / num1))
            else:
                stack.append(int(i))
        return int(stack.pop())


s = Solution()
print(s.evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))
