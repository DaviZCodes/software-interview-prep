class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #reverse because we only want to add on last one
        digits = digits[::-1]
        
        #carry to keep track of when to stop
        #index to keep track of current index in list
        carry, index = 1, 0

        while carry == 1: 
            # we only stop if there is no more carry, that is our condition
            if index < len(digits):
                if digits[index] == 9:
                    #if it is 9, we want to replace with 0, then we append 1,
                    #e.g 9 + 1 would be 10 (notice we first add 0, then append 1                    and reverse it so it is 0,1 reversing would be 1,0 which is 10)
                    digits[index] = 0
                else:
                    #if there is no 9 involved, we just simply add like 6 + 1 = 7
                    digits[index] += 1
                    carry = 0
            else: #if index is greater, then we just need to append 1
                digits.append(1)
                carry = 0
            index += 1

        return digits[::-1] #unreverse the list
    
