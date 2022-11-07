'''
File: Bubble Sort Algorithm (easy)
Author: DaviZCodes
Question:
Write a bubble sort algorithm for a given array of integers. The algorith sorts the array then
prints three lines:
line 1: number of swaps
line 2: first element of array after swap
line 3: last element of array after swap
'''

def countSwaps(a):
    count = 0
    for i in range(len(a)):
        for j in range(len(a) - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                count += 1

    swaps = "Array is sorted in " + str(count) + " swaps."

    firstEle = "First Element: " + str(a[0])

    lastEle = "Last Element: " + str(a[len(a) - 1])

    return swaps + "\n" + firstEle + "\n" + lastEle

def main():
    array_example = [32,3,6,8,10]
    print(countSwaps(array_example))

if __name__ == "__main__":
    main()