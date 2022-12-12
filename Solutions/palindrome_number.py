"""Given an integer x, return true if x is a palindrome, and false otherwise.

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
"""


class Solution:
    """Solution class to check if the number is a palindrome or not."""

    def isPalindrome(self, x: int) -> bool:
        """Actual Program."""
        return str(x) == str(x)[::-1]
