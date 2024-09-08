#If
# Example 1: Check if a number is positive
num = 10
if num > 0:
    print("The number is positive.")

# Example 2: Check if a string is non-empty
string = "Hello"
if string:
    print("The string is not empty.")

# Example 3: Check if a list has more than 5 elements
my_list = [1, 2, 3, 4, 5, 6]
if len(my_list) > 5:
    print("The list has more than 5 elements.")

# Example 4: Check if a person is an adult
age = 25
if age >= 18:
    print("The person is an adult.")

# Example 5: Check if a number is even
number = 8
if number % 2 == 0:
    print("The number is even.")

#..........................................................................................
#..........................................................................................

#If Else
# Example 1: Check if a number is positive or negative
num = -5
if num > 0:
    print("Positive")
else:
    print("Negative")

# Example 2: Check if a string is empty or not
text = ""
if text:
    print("String is not empty")
else:
    print("String is empty")

# Example 3: Check if someone is a teenager or not
age = 16
if age >= 13 and age <= 19:
    print("Teenager")
else:
    print("Not a teenager")

# Example 4: Check if a number is even or odd
number = 7
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# Example 5: Check if temperature is above or below freezing
temperature = -1
if temperature > 0:
    print("Above freezing")
else:
    print("Below freezing")

#..........................................................................................
#..........................................................................................

#If-Elif-Else
# Example 1: Check age categories
age = 30
if age < 13:
    print("Child")
elif age < 20:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

# Example 2: Check exam grade
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

# Example 3: Check the day of the week
day = "Tuesday"
if day == "Monday":
    print("Start of the week")
elif day == "Wednesday":
    print("Midweek")
elif day == "Friday":
    print("Almost the weekend")
else:
    print("It's a regular day")

# Example 4: Determine the size of a shirt
size = 42
if size < 36:
    print("Small")
elif size <= 40:
    print("Medium")
elif size <= 44:
    print("Large")
else:
    print("Extra Large")

# Example 5: Weather forecast decision
temperature = 25
if temperature < 0:
    print("It's freezing!")
elif temperature < 10:
    print("It's cold.")
elif temperature < 20:
    print("It's cool.")
else:
    print("It's warm.")

#....................................................................
#....................................................................

#Nested If-Else
# Example 1: Check if a number is positive, negative, or zero
num = 0
if num >= 0:
    if num == 0:
        print("The number is zero.")
    else:
        print("The number is positive.")
else:
    print("The number is negative.")

# Example 2: Check if the year is a leap year
year = 2024
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# Example 3: Check if a number is even or odd and within a certain range
number = 15
if number > 0:
    if number % 2 == 0:
        print("Positive and even")
    else:
        print("Positive and odd")
else:
    print("Negative number")

# Example 4: Check if a person is eligible for senior citizen benefits
age = 67
citizen = True
if age >= 65:
    if citizen:
        print("Eligible for senior citizen benefits.")
    else:
        print("Not eligible for senior citizen benefits (non-citizen).")
else:
    print("Not old enough for benefits.")

# Example 5: Determine the quadrant of a point on the coordinate plane
x, y = 3, -4
if x > 0:
    if y > 0:
        print("The point is in the first quadrant.")
    else:
        print("The point is in the fourth quadrant.")
else:
    if y > 0:
        print("The point is in the second quadrant.")
    else:
        print("The point is in the third quadrant.")
