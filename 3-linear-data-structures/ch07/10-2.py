from typing import List


class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        return sum(
            number
            for i, number in enumerate(nums)
            if i % 2 == 0
        )
