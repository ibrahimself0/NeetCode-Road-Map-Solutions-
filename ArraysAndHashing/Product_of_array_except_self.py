class Solution(object):
    def productExceptSelf(self, nums):
        def multiply_elements(array):
            res = 1
            for j in array:
                res *= j
            return res


        x = multiply_elements(nums)
        answers = []
        for i in nums:
            if i != 0:
                answers.append(int(x / i))
            else:
                temp = nums[:]
                temp.remove(i)
                answers.append(multiply_elements(temp))
        return answers
