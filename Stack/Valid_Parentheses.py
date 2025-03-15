class Solution(object):
    def isValid(self, s):
        opened = ('(', '{', '[')
        closed = (')', '}', ']')
        stack = []

        def getLast():
            return stack[len(stack) - 1]

        for i in s:
            if i in opened:
                stack.append(i)
            else:
                if stack.__len__() == 0:
                    return False
                else:
                    indexOpen = 0
                    indexClose = 0
                    x = 0
                    while x < 3:
                        if getLast() == opened[x]:
                            indexOpen = x
                            break
                        x += 1
                    x = 0
                    while x < 3:
                        if i == closed[x]:
                            indexClose = x
                            break
                        x += 1
                    print(opened[indexOpen] + closed[indexClose])
                    if indexClose == indexOpen:
                        stack.pop()
                    else:
                        return False
        if stack.__len__() == 0:
            return True
        else:
            return False



