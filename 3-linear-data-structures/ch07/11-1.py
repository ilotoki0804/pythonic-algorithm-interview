from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []

        left_accumulated = 1
        for number in nums:
            result.append(left_accumulated)
            left_accumulated *= number

        right_accumulated = 1
        for i in range(0, len(nums))[::-1]:
            result[i] *= right_accumulated
            right_accumulated *= nums[i]

        return result
