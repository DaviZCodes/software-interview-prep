class Solution:
    def repeatedCharacter(self, s: str) -> str:
        letters = set()

        for char in s:
            if char in letters:
                return char
            letters.add(char)
        
