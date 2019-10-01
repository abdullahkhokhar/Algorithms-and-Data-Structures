"""
Given a string, find the length of the longest substring without repeating characters.

EXAMPLE:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # can not have repeating character
        # want to find the longest substring

        current_longest = ""
        final_longest = ""
        values_seen = []

        for i in range(len(s)):
            while (i != len(s)) and (s[i] not in values_seen):
                # add to the seen list
                values_seen.append(s[i])
                # append to the string
                current_longest = current_longest + s[i]
                i += 1
            if len(current_longest) > len(final_longest):
                final_longest = current_longest
            current_longest = ""
            values_seen = []

        return len(final_longest)
