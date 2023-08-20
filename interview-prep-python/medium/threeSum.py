class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        for i, a in enumerate(nums):
            # i is the index, a is the value
            if i > 0 and a == nums[i - 1]:
                continue # don't reuse duplicate value
            
            left, right = i + 1, len(nums) - 1

            while left < right:
                three_sum = a + nums[left] + nums[right]

                if three_sum > 0:
                    right -= 1
                elif three_sum < 0:
                    left += 1
                else:
                    result.append([a, nums[left], nums[right]])
                    left += 1

                    while nums[left] == nums[left - 1] and left < right: 
                        #duplicate, then keep shifting
                        left += 1
        
        return result
