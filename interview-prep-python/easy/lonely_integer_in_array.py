'''
File: Lonely integer in an array
Author: DaviZCodes
Question (easy):
Given an array of integers, where all elements but one occur twice, find the unique element.

Example

The unique element is .

'''

def lonelyinteger(array):
    result = 0
    
    for number in array:
        result ^= number
    
    return result


#example input

def main():
    array = [1,3,4,4,3,1,6]
    print(lonelyinteger(array))
    
if __name__ == "__main__":
    main()

'''
the trick is to use ^ (caret) operator which will cancel out all the even number of same integers and the remaining "lonely integer"
will be the result since it is the only odd one out
'''
