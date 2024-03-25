class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels_types = set([j for j in jewels])

        for stone in stones:
            if stone in jewels_types:
                count +=1
        
        return count
        
