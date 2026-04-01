class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l, r = 0, len(nums) - 1

        k = 0

        while k <= r:
            if nums[k] == 0:
                nums[k], nums[l] = nums[l], nums[k]
                l += 1
            elif nums[k] == 2:
                nums[k], nums[r] = nums[r], nums[k]
                r -= 1
                k -= 1
            k += 1
        