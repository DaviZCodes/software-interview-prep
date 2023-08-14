class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_result = nums[0] 

        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                min_result = min(min_result, nums[left])
            
            mid = (left + right)//2
            min_result = min(min_result, nums[mid])

            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return min_result
