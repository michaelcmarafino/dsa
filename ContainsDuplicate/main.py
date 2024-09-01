from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ##myMap = {}
        ##for n in nums:
            ##if n in myMap:
                ##return True
            ##else:
                ##myMap[n] = True
        ##return False
        
        hashset = set()

        for n in nums: 
            if n in hashset:
                return True
            hashset.add(n)
        return False





    