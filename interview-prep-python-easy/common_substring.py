'''
File: common_substring.py
Author: DaviZCodes
Question:
Given two strings, determine if they share a common substring. A substring may be as small as one character.
e.g.
Given string "pot" and string2 = "cod", the common substring is "o"
'''

def common_substring(s1, s2):
    if set(s1) & set(s2):
        return "Yes, there is a common substring."
    return "No, there is no common substring"

#define main

def main():
    #should return yes
    string1 = "hands"
    string2 = "plead"
    print(common_substring(string1, string2))

    #should return no
    string3 = "begone"
    string4 = "cat"
    print(common_substring(string3, string4))

if __name__ == '__main__':
    main()

'''
This exercise introduces the set() method which basically creates a set of distinct elements of an iterable like
a list, tuple, or dictionary. The set is as {}. 
This is very useful when comparing two iterables in O(n) runtime
'''