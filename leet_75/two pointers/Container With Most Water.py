# Question
# You are given an integer array height of length n.
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
#
# Return the maximum amount of water a container can store.

# Solution
def maxArea(height):
    max_water = 0
    left, right = 0, len(height) - 1

    while left < right:
        width = right - left
        container_height = min(height[left], height[right])
        max_water = max(max_water, width * container_height)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_water

# Example usage
height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))  # Output will be the maximum water container area
