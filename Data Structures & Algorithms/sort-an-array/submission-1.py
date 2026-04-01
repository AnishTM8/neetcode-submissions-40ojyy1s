class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)

    def mergeSort(self, nums):

        if len(nums) == 1:
            return nums
        
        left = self.mergeSort(nums[:len(nums)//2])
        right = self.mergeSort(nums[len(nums)//2:])

        l, r = 0, 0
        sorted_array = []

        while l < len(left) and r < len(right):
            if left[l] > right[r]:
                sorted_array.append(right[r])
                r += 1
            else:
                sorted_array.append(left[l])
                l += 1
        
        while l < len(left):
            sorted_array.append(left[l])
            l += 1

        while r < len(right):
            sorted_array.append(right[r])
            r += 1
        
        return sorted_array

            