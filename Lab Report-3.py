# 1. Password Validator
def password_validator():
    while True:
        password = input("Enter password: ")
        if len(password) >= 8 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
            print("Password accepted.")
            break
        else:
            print("Invalid password. Try again.")
            continue
# password_validator()
# Output: Depends on input (Password accepted or Invalid password)

# 2. Divisible by 3 or 5
def divisible_by_3_or_5():
    for i in range(1, 51):
        if i % 3 == 0 or i % 5 == 0:
            print(i)
# divisible_by_3_or_5()
# Output: 3, 5, 6, 9, 10, 12, 15, 18, ..., 45, 48, 50

# 3. Positive Number Sum
def positive_number_sum():
    total = 0
    while True:
        num = int(input("Enter a positive number (negative to stop): "))
        if num < 0:
            break
        total += num
    print("Sum of positive numbers:", total)
# positive_number_sum()
# Output: Depends on input (Sum of positive numbers: Total)

# 4. Word Palindrome Checker
def palindrome_checker():
    while True:
        word = input("Enter a word: ")
        if len(word) < 3:
            continue
        if word == word[::-1]:
            print(f"{word} is a palindrome.")
        else:
            print(f"{word} is not a palindrome.")
# palindrome_checker()
# Output: Depends on input (word is a palindrome or not)

# 5. Vowel Counter
def vowel_counter():
    word = input("Enter a string: ")
    count = 0
    vowels = "aeiouAEIOU"
    for char in word:
        if char in vowels:
            count += 1
    print("Number of vowels:", count)
# vowel_counter()
# Output: Depends on input (Number of vowels)

# 6. Unique Characters
def unique_characters():
    string = input("Enter a string: ")
    chars = set()
    for char in string:
        if char in chars:
            print("String does not contain all unique characters.")
            break
        chars.add(char)
    else:
        print("String contains all unique characters.")
# unique_characters()
# Output: Depends on input (String contains all unique characters or not)

# 7. Student Information System
def student_information_system():
    info = {}
    while True:
        choice = input("Choose the information to submit (name, age, address): ")
        if choice == "age":
            info['age'] = float(input("Enter age: "))
        else:
            info[choice] = input(f"Enter {choice}: ")[:5]
        another = input("Submit another info? (yes/no): ")
        if another.lower() == "no":
            break
    print(info)
# student_information_system()
# Output: Depends on input (Stored data in dictionary)

# 8. Grocery Shop
def grocery_shop():
    bucket_list = []
    while True:
        action = input("Add or Remove items (add/remove): ")
        item = input("Enter item: ")
        if action == "add":
            bucket_list.append(item)
        elif action == "remove" and item in bucket_list:
            bucket_list.remove(item)
        print("Current bucket list:", bucket_list)
        more = input("Continue? (yes/no): ")
        if more == "no":
            break
# grocery_shop()
# Output: Depends on input (List of added/removed items)

# 9. Unique Characters in Strings
def unique_sorted_characters():
    n = int(input("Enter number of strings: "))
    all_chars = set()
    for _ in range(n):
        string = input("Enter string: ")
        all_chars.update(set(string))
    sorted_chars = sorted(all_chars)
    print(sorted_chars)
# unique_sorted_characters()
# Output: Depends on input (Sorted list of unique characters)

# 10. Minimize Product Cost
def minimize_product_cost():
    products = {
        'Rice': [45, 42, 41, 40],
        'Salt': [34, 35, 36, 36],
        'Fish': [200, 202, 201, 205],
        'Orange': [100, 99, 101, 102]
    }
    product = input("Input the product name: ")
    min_cost = min(products[product])
    print(f"{product} -> market {products[product].index(min_cost) + 1} value = {min_cost}")
# minimize_product_cost()
# Output: Depends on input (Minimized product cost)

# 11. Student Email Generator
def student_email_generator():
    n = int(input("Enter number of students: "))
    emails = []
    for _ in range(n):
        name = input("Enter student name: ")
        if len(name) > 20:
            continue
        email = f"{name.lower()}_{len(name)}_{ord(name[0])}"
        emails.append(email)
    print("Generated emails:", emails)
# student_email_generator()
# Output: Depends on input (Generated email list)

# 12. String Compression
def string_compression():
    n = int(input("Enter number of strings: "))
    max_length = int(input("Enter maximum string length: "))
    for _ in range(n):
        string = input("Enter string: ")[:max_length]
        compressed = ""
        count = 1
        for i in range(1, len(string)):
            if string[i] == string[i-1]:
                count += 1
            else:
                compressed += f"{count}{string[i-1]}"
                count = 1
        compressed += f"{count}{string[-1]}"
        print(compressed)
# string_compression()
# Output: Depends on input (Compressed strings)

# 13. To-Do List Manager
def to_do_list():
    tasks = []
    while True:
        action = input("Add/Complete/Show tasks (add/complete/show): ")
        if action == "add":
            task = input("Enter task: ")
            tasks.append({'task': task, 'completed': False})
        elif action == "complete":
            task = input("Enter task to complete: ")
            for t in tasks:
                if t['task'] == task:
                    t['completed'] = True
        elif action == "show":
            for t in tasks:
                print(f"Task: {t['task']}, Completed: {t['completed']}")
        if input("Continue? (yes/no): ") == "no":
            break
# to_do_list()
# Output: Depends on input (Added/Completed tasks)

# 14. Rotate String
def rotate_string():
    m = int(input("Size of String m= "))
    string = input("Input String: ")[:m]
    n = int(input("Number of characters to rotate: "))
    print(string[n:] + string[:n])
# rotate_string()
# Output: Depends on input (Rotated string)

# 15. Employee Name to Numerical Value
def employee_numerical_value():
    n = int(input("Enter number of employees: "))
    values = []
    for _ in range(n):
        name = input("Enter employee name: ")
        ascii_sum = sum(ord(c) for c in name)
        values.append(ascii_sum)
    print("Numerical Values:", values)
# employee_numerical_value()
# Output: Depends on input (List of ASCII sums)

# 16. Password Generator
def password_generator():
    string = input("Enter the string to generate password (length 10): ")[:10]
    password = string[:3].upper() + "!@#$" + string[-3:].lower()
    print("Generated password:", password)
# password_generator()
# Output: Depends on input (Generated password)

# 17. Sum of Even Numbers
def sum_of_even_numbers():
    x = [3, 4, 5, 7, 8, 10, "dghf", "cbxgc", 3.5, 6.2]
    total = sum(i for i in x if isinstance(i, int) and i % 2 == 0)
    print("Sum of even numbers:", total)
# sum_of_even_numbers()
# Output: 22
