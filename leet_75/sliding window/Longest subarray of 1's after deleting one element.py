# Question

# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.

# Solution

class Solution(object):
    def longestSubarray(self, nums):
        i, j, max_length, zero_count = 0, 0, 0, 0

        for j in range(len(nums)):
            if nums[j] == 0:
                zero_count += 1

            # If there are more than one 0 in the window, shrink the window
            while zero_count > 1:
                if nums[i] == 0:
                    zero_count -= 1
                i += 1

            # Update max_length, subtract 1 for deletion
            max_length = max(max_length, j - i)

        return max_length
