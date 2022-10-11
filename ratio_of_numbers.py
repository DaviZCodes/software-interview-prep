'''
File name
Author: Davi Zheng

Question from HackerRank:

Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero.
Print the decimal value of each fraction on a new line with  places after the decimal.

Note: This challenge introduces precision problems.
The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.
'''


def ratio_of_numbers(input_array):

    # create a dictionary with positive, zero, and negative counts
    dictionary_counts = {"positive_count" : 0, "negative_count" : 0, "zero_count" : 0}

    # loop through the array
    for element in input_array:
        if element == 0:
            dictionary_counts["zero_count"] += 1
        elif element > 0:
            dictionary_counts["positive_count"] += 1
        else:
            dictionary_counts["negative_count"] += 1

    # use round for precision six decimal places
    print(round(dictionary_counts["positive_count"]/len(input_array), 6))
    print(round(dictionary_counts["negative_count"] / len(input_array), 6))
    print(round(dictionary_counts["zero_count"] / len(input_array), 6))

    return ""

if __name__ == '__main__':
    print(ratio_of_numbers([1, 1, 0, -1, -1]))
    print(ratio_of_numbers([-4, 3, -9, 0, 4, 1]))



