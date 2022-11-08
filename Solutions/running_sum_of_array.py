"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

Example 1:

Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
"""

from typing import List


class Solution:
    """Final Solution."""

    def runningSum(self, nums: List[int]) -> List[int]:
        """Run sum method."""
        for x in range(1, len(nums)):
            nums[x] += nums[x - 1]
        return nums
