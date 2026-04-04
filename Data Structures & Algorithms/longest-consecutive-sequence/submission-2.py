class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0

        num_set = set(nums)

        for num in nums:
            if (num - 1) not in num_set:
                count = 1
                while (num + count) in num_set:
                    count += 1
                res = max(count, res)

        return res