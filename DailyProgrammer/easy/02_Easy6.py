# **Intermediate Exercises:**

# 1. Write a function to check if a given number is a perfect square.
# 2. Implement a program to find the common elements between two lists.
# 3. Write a function to reverse a sentence while preserving the order of words.
# 4. Create a program to find the longest substring without repeating characters in a given string.
# 5. Implement a function to check if a given string is a valid palindrome, ignoring non-alphanumeric characters.
# 6. Write a program to generate the Fibonacci sequence up to a given number.
# 7. Create a function that converts a given integer to Roman numerals.

from random import shuffle

def isSquare(num):
    sq = int(num ** 0.5)
    # print(sq)

    if sq * sq == num:
        print(f'{num} is PERFECT square')
    else:
        print(f'{num} NOT perfect square')


if __name__ == "__main__":
    numList = range(2, 50)
    nList1 = list(range(0, 50, 2))
    nList2 = list(range(0, 75, 3))

    shuffle(nList1)
    shuffle(nList2)

    for num in range(2, 50):
        isSquare(num)
    
    print(nList1)
    print(nList2)
    commonList = [num for num in nList1 if num in nList2]
    print(commonList)
