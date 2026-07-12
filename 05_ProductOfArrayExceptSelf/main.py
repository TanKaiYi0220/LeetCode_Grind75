class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # init [1, 1, 1, 1]
        # [2, 3, 4, 5]
        # prefix
        #                = 1
        # a1             = 2
        # a1 * a2        = 6
        # a1 * a2 * a3   = 24

        # suffix
        #                = 1
        # a4             = 5
        # a4 * a3        = 20
        # a4 * a3 * a2   = 60

        length = len(nums)
        out = [1 for _ in range(length)]

        prefix = 1
        for i in range(length):
            out[i] = prefix # not excluding self
            prefix *= nums[i] # multiply self for next element

        suffix = 1
        for i in range(length - 1, -1, -1):
            out[i] *= suffix # not excluding self
            suffix *= nums[i]
    
        return out