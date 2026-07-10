from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for idx, n in enumerate(nums):
            dn = target - n
            if dn in num_map:
                return [num_map[dn], idx]
            num_map[n] = idx
