class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = sum(nums[0:3]) # initialize the result to a random three_sum

        for i in range(len(nums)): 
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = nums[i] + nums[left] + nums[right] # three pointers

                if three_sum < target:
                    left += 1
                elif three_sum > target:
                    right -= 1
                else: # return if equal
                    return target
                
                ''' 
                If three_sum closer to target, result is new three_sum
                use absolute value because we want difference
                so if target is 0, 3 and -3 are equal 
                '''
                if abs(three_sum - target) < abs(result - target):
                    result = three_sum
        
        return result
        
