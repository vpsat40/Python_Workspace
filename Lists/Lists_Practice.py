# Exercise 8: Matrix Transpose Write a function that takes a 2D list (matrix) as input and returns a new 2D list representing the transpose of the original matrix.
# Exercise 10: List Flattening Write a function that takes a nested list as input and returns a new list containing all the elements from the nested lists in a single, flat list.

# Exercise 1: List Sum 
# Write a function that takes a list of 
# integers as input and returns the sum of all the elements in the list.

def listSum(n_lst):
    if type(n_lst) != list:
        return None
    
    lst_Sum = 0
    for num in n_lst:
        lst_Sum += num
    return lst_Sum

def sortList(n_list):
    if type(n_list) == list:
        n_list.sort()
        return n_list
    else:
        return None

def uniqueElements(input_list):
    unique_list = []

    for num in input_list:
        if num not in unique_list:
            unique_list.append(num)
    
    return unique_list

def commonElements(iList1, iList2):
    commonList = []
    for num in iList1:
        if num in iList2 and num not in commonList:
            commonList.append(num)

    return commonList

def evenIndices(strings):
    newStrings = []
    newWord = ''

    for eachWord in strings:
        newWord = eachWord[::2]
        newStrings.append(newWord)
        print(newWord)

    return newStrings

if __name__ == '__main__':
    lst = [10, 2, 13, 46, 35, 86, 27, 88]
    my_list = [28, 3, 19, 79, 10, 5, 19, 87, 23, 12, 20, 13, 30, 9, 20, 19, 23, 10, 20, 12, 3, 5, 20, 22, 13, 11, 20, 17, 4, 2, 20, 14, 18, 2, 19, 76]
    sub_list1 = my_list[0:18]
    sub_list2 = my_list[18:]


    print(f'Sum of all elements in list is {listSum(lst)}')

# Exercise 2: 
# 
# List Sorting Write a function that takes a list of numbers as input and 
# returns a new list with the elements sorted in ascending order.
    print(f'Sorted list of elements is {sortList(lst)}')

# Exercise 3: Unique Elements 
# 
# Write a function that takes a list as input and returns a new list containing only the 
# unique elements from the original list, preserving their order of appearance.
    print(f'Unique elements {uniqueElements(my_list)} ? ')

# Exercise 4: List Reversal 
# Write a function that takes a list as input and returns a new list with the elements reversed.
    reverse_list = my_list[::-1]
    print(f'Reversed list is {reverse_list}')

# Exercise 5: List Comprehensions 
# Write a function that takes a list of numbers as input and returns a new list 
# containing only the even numbers using list comprehensions.
    even_list = [num for num in range(1, 11) if num%2 == 0 ]
    print(f'List of evens with list comprehension - {even_list}')


# Exercise 6: List Intersection 
# Write a function that takes two lists as input and returns a new list 
# containing the common elements present in both lists, without duplicates.
    print(f'List 1 - {sub_list1}')
    print(f'List 2 - {sub_list2}')
    print(f'\nCommon Elements are {commonElements(sub_list2, sub_list1)}')


# Exercise 7: List Manipulation 
# Write a function that takes a list of strings as input and modifies the list 
# by appending the word "good" before each string. For example, 
# if the input list is ["morning", "afternoon", "evening"], 
# the output list should be ["good morning", "good afternoon", "good evening"].

    str_list = ["morning", "afternoon", "evening"]

    for idx, each_word in enumerate(str_list):
        str_list[idx] = "good " + each_word
        print(str_list[idx])
    
    print(f'Output is {str_list}')

# Exercise 9: List Slicing 
# Write a function that takes a list as input and 
# returns a new list containing only the elements at even indices.
    print(f'List of elements at even indices is {evenIndices(str_list)}')