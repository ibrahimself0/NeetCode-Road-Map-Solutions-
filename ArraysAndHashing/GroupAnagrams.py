from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        res = defaultdict(list)
        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord("a")] += 1
            res[tuple(count)].append(word)

        return res.values()
