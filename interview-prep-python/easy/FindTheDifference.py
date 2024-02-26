class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # better solution
        sum_s = 0
        sum_t = 0

        for char in s:
            sum_s += ord(char)
        
        for char in t:
            sum_t += ord(char)
        
        return chr(sum_t - sum_s)

        ''' another solution
        count_char1 = Counter(s)
        count_char2 = Counter(t)
        
        count_char1 = {}
        count_char2 = {}

        for char in s:
            if char not in count_char1:
                count_char1[char] = 1
            else:
                count_char1[char] += 1
        
        for char in t:
            if char not in count_char2:
                count_char2[char] = 1
            else:
                count_char2[char] += 1
        
        for char in count_char2:
            if char not in count_char1:
                return char
            if count_char1[char] != count_char2[char]:
                return char 
        '''
