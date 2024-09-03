from typing import List

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []
        for n in (nums):
            i = abs(n) - 1
            nums[i] = -1 * abs(nums[i])

        for i, n in enumerate(nums):
            if n > 0:
                result.append(i + 1)

        return result

