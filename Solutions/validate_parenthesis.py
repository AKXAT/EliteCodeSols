"""Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
"""


class Solution:
    """Solution class."""

    ALL_BRACKETS = {"(": ")", "{": "}", "[": "]"}

    def isValid(self, s: str) -> bool:
        """Actual method to check if the parenthesis is valid or not."""
        current_openned = list()
        for each in s:
            if each in self.ALL_BRACKETS:
                current_openned.append(each)
            else:
                if (
                    len(current_openned) == 0
                    or each != self.ALL_BRACKETS[current_openned[-1]]
                ):
                    return False
                current_openned.pop(-1)
        return True if len(current_openned) == 0 else False


if __name__ == "__main__":
    sol = Solution()
    print(sol.isValid(s="]}"))
