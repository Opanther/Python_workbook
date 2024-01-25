# Question
#
# Given an array of characters chars, compress it using the following algorithm:
#
# Begin with an empty string s. For each group of consecutive repeating characters in chars:
#
# If the group's length is 1, append the character to s.
# Otherwise, append the character followed by the group's length.
# The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
#
# After you are done modifying the input array, return the new length of the array.
#
# You must write an algorithm that uses only constant extra space.

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        read, write = 0, 0
        while read < len(chars):
            curr = chars[read]
            count = 0

            # count the occurrences of the current character

            while read < len(chars) and chars[read] == curr:
                read += 1
                count += 1
            # write the current character to the write pointer
            chars[write] = curr
            write += 1
            # if count is more than 1, convert it to string and write each digit
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1

        # the write pointer is now at the new end of the array
        return write
