# This problem is a good test of your ability to navigate array manipulation and apply logical conditions. Here's how you can approach it:
# Question
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
#
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

# Solution

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                # Check if the left and right plots are empty or non-existent
                empty_left = (i == 0) or (flowerbed[i-1] == 0)
                empty_right = (i == len(flowerbed) - 1) or (flowerbed[i+1] == 0)

                if empty_left and empty_right:
                    flowerbed[i] = 1  # Plant a flower
                    n -= 1  # Decrement n
                    if n == 0:
                        return True
                    i += 1

        return n == 0

sol = Solution()
print(sol.canPlaceFlowers([1, 0, 0, 0, 1], 1))  # Add test cases that are failing