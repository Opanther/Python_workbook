# Question
#
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
#
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

# Solution

class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # check for edge cases
        if len(s) == 0 or k == 0 or len(s) < k:
            return 0

        # Initialize window
        vowels = set('aeiou')
        curr = 0

        # count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        # Initialize max_vowels with the count of the first window
        max_vowels = curr

        # Slide the window
        for i in range(k, len(s)):
            if s[i] in vowels:
                curr += 1
            if s[i - k] in vowels:
                curr -= 1

            max_vowels = max(max_vowels, curr)

        return max_vowels




