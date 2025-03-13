class Solution(object):
    def isAnagram(self, s, t):

        letters1 = []
        for char in s:
            letters1.append(char)

        letters2 = []
        for char in t:
            letters2.append(char)

        for char in letters1:
            if char in letters2:
                letters2.remove(char)
            else:
                return False
        if len(letters2) == 0:
            return True
        return False
