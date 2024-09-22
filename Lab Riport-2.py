# 1. String Reverse: Write a Python function to reverse a given string and return the reversed string.
def reverse_string(s):
    return s[::-1]

# Test Case
s = "hello world"
reversed_string = reverse_string(s)
print(reversed_string) # Output: dlrow olleh

# 2. Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.
def convert_to_string(numbers):
    return [str(number) for number in numbers]

# Test Case
numbers = [1, 2, 3, 4, 5]
string_numbers = convert_to_string(numbers)
print(string_numbers) # Output: ['1', '2', '3', '4', '5']

# 3. Temperature Converter: Write a Python program that converts a temperature in Celsius to Fahrenheit. Take the Celsius temperature as input from the user.
def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

# Test Case
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = celsius_to_fahrenheit(celsius)
print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.") # Output: Enter temperature in Celsius: 25
                                                                             # 25.0 degrees Celsius is equal to 77.0 degrees Fahrenheit.

# 4. String Palindrome: Write a Python function to check if a given string is a palindrome or not.
def is_palindrome(s):
    return s == s[::-1]

# Test Case
s = "madam"
if is_palindrome(s):
    print(f"{s} is a palindrome.")
else:
    print(f"{s} is not a palindrome.") # Output: madam is a palindrome.

# 5. String Reversal with Slicing: Write a Python function to reverse a given string using slicing.
def reverse_string_slicing(s):
    return s[::-1]

# Test Case
s = "hello world"
reversed_string = reverse_string_slicing(s)
print(reversed_string) # Output: dlrow olleh

# 6. Grades Classification: Write a Python program that takes a student's percentage as input and prints their corresponding grade according to the following criteria: - 90% or above: A+ - 80-89%: A 70-79%: B-60-69%: C Below 60%: Fail.
def get_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    else:
        return "Fail"

# Test Case
percentage = float(input("Enter student's percentage: "))
grade = get_grade(percentage)
print(f"The grade for {percentage}% is {grade}") # Output: Enter student's percentage: 85
                                                # The grade for 85.0% is A

# 7. Table of a Number: Write a Python program using a for loop to print the multiplication table of a given number N.
def print_multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Test Case
n = int(input("Enter a number: "))
print_multiplication_table(n) # Output: Enter a number: 5
                            # 5 x 1 = 5
                            # 5 x 2 = 10
                            # 5 x 3 = 15
                            # 5 x 4 = 20
                            # 5 x 5 = 25
                            # 5 x 6 = 30
                            # 5 x 7 = 35
                            # 5 x 8 = 40
                            # 5 x 9 = 45
                            # 5 x 10 = 50

# 8. Count Digits in a Number: Write a Python program using a while loop to count the number of digits in a given integer N.
def count_digits(n):
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

# Test Case
n = int(input("Enter a number: "))
digit_count = count_digits(n)
print(f"The number of digits in {n} is {digit_count}") # Output: Enter a number: 12345
                                                    # The number of digits in 12345 is 5

# 9. Fibonacci Sequence: Write a Python program using a for loop to generate the Fibonacci sequence up to a given limit N.
def fibonacci_sequence(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

# Test Case
n = int(input("Enter the limit for Fibonacci sequence: "))
fibonacci_sequence(n) # Output: Enter the limit for Fibonacci sequence: 10
                        # 0 1 1 2 3 5 8 13 21 34 

# 10. Sum of Even Numbers: Write a Python program using a while loop to calculate the sum of all even numbers between 1 and N, where N is taken as input from the user.
def sum_of_even_numbers(n):
    sum = 0
    i = 2
    while i <= n:
        sum += i
        i += 2
    return sum

# Test Case
n = int(input("Enter the upper limit: "))
sum = sum_of_even_numbers(n)
print(f"The sum of even numbers between 1 and {n} is {sum}") # Output: Enter the upper limit: 10
                                                            # The sum of even numbers between 1 and 10 is 30

# 11. Print Patterns: Write a Python program using nested for loops to print various patterns, such as a right-angled triangle, an inverted right-angled triangle, and so on.
def print_right_angled_triangle(rows):
    for i in range(1, rows + 1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

def print_inverted_right_angled_triangle(rows):
    for i in range(rows, 0, -1):
        for j in range(1, i + 1):
            print("*", end="")
        print()

# Test Case
rows = int(input("Enter the number of rows: "))
print("Right-Angled Triangle:")
print_right_angled_triangle(rows)
print("\nInverted Right-Angled Triangle:")
print_inverted_right_angled_triangle(rows) # Output: Enter the number of rows: 5
                                        # Right-Angled Triangle:
                                        # *
                                        # **
                                        # ***
                                        # ****
                                        # *****
                                        # 
                                        # Inverted Right-Angled Triangle:
                                        # *****
                                        # ****
                                        # ***
                                        # **
                                        # *

# 12. Prime Number Checker: Write a Python program using a while loop to check if a given number N is prime or not.
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test Case
n = int(input("Enter a number: "))
if is_prime(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.") # Output: Enter a number: 17
                                        # 17 is a prime number.

# 13. List Manipulation: Given a list of integers, write a Python program using a for loop to find the sum, average, maximum, and minimum values in the list.
def list_manipulation(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return sum, average, maximum, minimum

# Test Case
numbers = [1, 2, 3, 4, 5]
sum, average, maximum, minimum = list_manipulation(numbers)
print(f"Sum: {sum}, Average: {average}, Maximum: {maximum}, Minimum: {minimum}") # Output: Sum: 15, Average: 3.0, Maximum: 5, Minimum: 1

# 14. Reverse String: Write a Python program using a while loop to reverse a given string.
def reverse_string_while(s):
    reversed_string = ""
    i = len(s) - 1
    while i >= 0:
        reversed_string += s[i]
        i -= 1
    return reversed_string

# Test Case
s = "hello world"
reversed_string = reverse_string_while(s)
print(reversed_string) # Output: dlrow olleh

# 15. List Sum: Write a Python program to find the sum of all elements in a given list of integers.
def list_sum(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# Test Case
numbers = [1, 2, 3, 4, 5]
sum = list_sum(numbers)
print(f"The sum of the list is {sum}") # Output: The sum of the list is 15

# 16. List Average: Write a Python program to calculate the average of all elements in a given list of integers.
def list_average(numbers):
    sum = 0
    for number in numbers:
        sum += number
    average = sum / len(numbers)
    return average

# Test Case
numbers = [1, 2, 3, 4, 5]
average = list_average(numbers)
print(f"The average of the list is {average}") # Output: The average of the list is 3.0

# 17. List Max and Min: Write a Python program to find the maximum and minimum values in a given list of integers.
def list_max_min(numbers):
    maximum = max(numbers)
    minimum = min(numbers)
    return maximum, minimum

# Test Case
numbers = [1, 2, 3, 4, 5]
maximum, minimum = list_max_min(numbers)
print(f"Maximum: {maximum}, Minimum: {minimum}") # Output: Maximum: 5, Minimum: 1

# 18. List Sorting: Write a Python program to sort a list of integers in ascending order.
def list_sorting(numbers):
    numbers.sort()
    return numbers

# Test Case
numbers = [5, 2, 4, 1, 3]
sorted_numbers = list_sorting(numbers)
print(f"Sorted list: {sorted_numbers}") # Output: Sorted list: [1, 2, 3, 4, 5]

# 19. List Filtering: Given a list of integers, write a Python program to create a new list that contains only the even numbers from the original list.
def list_filtering(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Test Case
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = list_filtering(numbers)
print(f"Even numbers: {even_numbers}") # Output: Even numbers: [2, 4, 6]

# 20. List Reversal: Write a Python program to reverse a given list without using any built-in functions.
def list_reversal(numbers):
    reversed_numbers = []
    i = len(numbers) - 1
    while i >= 0:
        reversed_numbers.append(numbers[i])
        i -= 1
    return reversed_numbers

# Test Case
numbers = [1, 2, 3, 4, 5]
reversed_numbers = list_reversal(numbers)
print(f"Reversed list: {reversed_numbers}") # Output: Reversed list: [5, 4, 3, 2, 1]

# 21. List Manipulation: Given two lists of integers, write a Python program to create a new list that contains elements common to both lists.
def list_manipulation_common(list1, list2):
    common_elements = []
    for element in list1:
        if element in list2:
            common_elements.append(element)
    return common_elements

# Test Case
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = list_manipulation_common(list1, list2)
print(f"Common elements: {common_elements}") # Output: Common elements: [3, 4, 5]

# 22. List Element Count: Write a Python program to count the occurrences of a specific element in a given list.
def list_element_count(numbers, element):
    count = 0
    for number in numbers:
        if number == element:
            count += 1
    return count

# Test Case
numbers = [1, 2, 3, 2, 4, 2, 5]
element = 2
count = list_element_count(numbers, element)
print(f"The element {element} occurs {count} times in the list.") # Output: The element 2 occurs 3 times in the list.

# 23. List Duplicates Removal: Write a Python program to remove duplicates from a given list while preserving the order of the elements.
def list_duplicates_removal(numbers):
    unique_numbers = []
    for number in numbers:
        if number not in unique_numbers:
            unique_numbers.append(number)
    return unique_numbers

# Test Case
numbers = [1, 2, 3, 2, 4, 2, 5]
unique_numbers = list_duplicates_removal(numbers)
print(f"List without duplicates: {unique_numbers}") # Output: List without duplicates: [1, 2, 3, 4, 5]

# 24. List Comprehension: Given a list of integers, write a Python program to create a new list that contains the squares of the elements using list comprehension.
def list_comprehension(numbers):
    squares = [number**2 for number in numbers]
    return squares

# Test Case
numbers = [1, 2, 3, 4, 5]
squares = list_comprehension(numbers)
print(f"Squares of the elements: {squares}") # Output: Squares of the elements: [1, 4, 9, 16, 25]