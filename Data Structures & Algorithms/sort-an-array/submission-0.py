class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        return self.mergeSort(nums)
    
    def mergeSort(self, arr):

        if len(arr) == 1:
            return arr
        
        m = len(arr) // 2

        left = self.mergeSort(arr[:m])
        right = self.mergeSort(arr[m:])

        i = j = 0
        s_arr = []

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s_arr.append(left[i])
                i += 1
            else:
                s_arr.append(right[j])
                j += 1
        
        s_arr.extend(left[i:])
        s_arr.extend(right[j:])

        return s_arr