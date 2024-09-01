from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ##total = 0
        ##missing_total = 0
        ##for n in nums:
            ##missing_total += n
        
        ##for i in range(0, len(nums) + 1):
            ##total += i
        
        ##return total - missing_total


        #return sum(range(len(nums) +1)) - sum(nums)

        #neetcode       
        res = len(nums)

        for i in range(len(nums)): 
            res += (i - nums[i])
        return res