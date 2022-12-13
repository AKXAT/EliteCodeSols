"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""
from typing import List


class Solution:
    """The Solution to check the logest common Prefix."""

    def longestCommonPrefix(self, strs: List[str]) -> str:
        """Check what is the logest prefix for the given list of strings."""
        strs.sort(key=len)
        mylist = list(zip(*strs))
        result = str()
        for each in mylist:
            if len(set(each)) == 1:
                result += each[0]
            elif len(set(each)) > 1:
                break
        return result
