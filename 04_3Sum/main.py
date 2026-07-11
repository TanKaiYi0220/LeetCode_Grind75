class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        out = []

        length = len(nums)
        nums = sorted(nums)

        for i in range(length):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            
            l = i + 1
            r = length - 1
            while l < r:
                s = nums[l] + nums[r]

                if s == target:
                    out.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1

                    # move until not duplicated
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1 

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
                elif s < target:
                    l += 1
                else:
                    r -= 1

        return out
