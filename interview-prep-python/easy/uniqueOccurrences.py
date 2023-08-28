class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = {}

        for num in arr:
            if num in occur:
                occur[num] += 1
            else:
                occur[num] = 1
        
        return len(occur.values()) == len(set(occur.values()))
        
