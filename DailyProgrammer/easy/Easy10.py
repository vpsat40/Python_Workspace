# Check if a string is a palindrome or not.
# Write a program to convert Celsius to Fahrenheit.
# Write fibonacci using for loop and using recursion

def factorial_rec(n):
    if n == 1:
        return n
    n = n * factorial_rec(n-1)

    return n

def fibonacci(num):
    a = 0
    b = 1
    sum = 0

    print(f'{a}, {b}, ')

    while (sum <= num):
        temp = a
        a = b
        b = temp + b
        print(f'{b}, ')
    


if __name__ == "__main__":

# Write a Python program to print "Hello, World!" on the screen.
    print("Hello World")

# Calculate the area of a rectangle given its length and width as input.
    # print("Enter Rectangle Length  - ")
    # a = int(input())

    # print("Enter Rectangle Breadth - ")
    # b = int(input())

    # # Calculate Area and Print it
    # area = a * b
    # print(f"Area of rectangle is - {area}")

# Write a program that takes two numbers as input and swaps their values.
    # print(f'A = {a} and B = {b}')
    # temp = a
    # a = b
    # b = temp
    # print(f'Swap with temp A = {a} and B = {b}')

    # a = a + b
    # b = a - b
    # a = a - b
    # print(f'Inpalce Swap A = {a} and B = {b}')

# Check if a given number is even or odd.
    print("Enter number - ")
    num = int(input())

    if num % 2 == 0:
        print(f"{num} is a even number")
    else:
        print(f"{num} is an odd number")

# Calculate the factorial of a given number.
    print("Factorial of {} is {}".format(num, factorial_rec(num)))

# Given a list of numbers, find the sum of all the elements in the list.
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    list_sum = 0

    for n in my_list:
        list_sum += n
    
    print(f'Sum of all elements in the list is {list_sum}')

# Find the maximum and minimum numbers in a list.
    print(f'Maximum number in the list is {max(my_list)}')
    print(f'Minimum number in the list is {min(my_list)}')

# Write a program to print the first n Fibonacci numbers.
    print(f'Printing fibonnaci numbers until {num} :')
    fibonacci(num)
