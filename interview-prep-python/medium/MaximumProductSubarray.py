class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = max(nums)
        currMin, currMax = 1, 1

        for num in nums:
            temp = currMax
            currMax = max(num * currMax, num * currMin, num)
            currMin = min(num* temp, num * currMin, num)

            result = max(result, currMax, currMin)
        
        return result
