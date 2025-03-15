from collections import Counter


class Solution(object):
    def longestConsecutive(self, nums):
        dict0 = Counter(nums)
        sorted_nums = sorted(dict0.keys())
        i = 0
        answers = []
        for j in range(len(sorted_nums) - 1):
            res = sorted_nums[j + 1] - sorted_nums[j]
            if res != 1:
                answers.append(i)
                i = 0
                continue
            else:
                i += 1
        else:
            answers.append(i)
        if sorted_nums.__len__() != 0:
            return max(answers) + 1
        else:
            return 0
