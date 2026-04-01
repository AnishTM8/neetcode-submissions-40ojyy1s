class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        prefix = {0:1}

        for num in nums:
            curSum += num
            diff = curSum - k

            if diff in prefix:
                res += prefix[diff]
            
            prefix[curSum] = 1 + prefix.get(curSum, 0)

        return res 