from collections import Counter


class Solution(object):
    def topKFrequent(self, nums, k):
        freq_map = Counter(nums)
        sorted_elements = sorted(freq_map.keys(), key=lambda x: freq_map[x], reverse=True)
        return sorted_elements[:k]