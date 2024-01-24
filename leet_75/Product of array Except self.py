# Question
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.

# Solution
class Solution(object):
    def productExceptSelf(self, nums):
        n = len(nums)
        left, right, answer = [1] * n, [1] * n, [1] * n

        # Fill the left array
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]

        # Fill the right array
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]

        # Calculate the answer
        for i in range(n):
            answer[i] = left[i] * right[i]

        return answer

