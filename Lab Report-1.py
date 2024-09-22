# 1. Matrix Addition: Write a Python program to add two matrices represented as nested lists.
def matrix_addition(matrix1, matrix2):
  """
  Adds two matrices represented as nested lists.

  Args:
    matrix1: The first matrix.
    matrix2: The second matrix.

  Returns:
    The sum of the two matrices.
  """
  rows = len(matrix1)
  cols = len(matrix1[0])
  result = [[0 for _ in range(cols)] for _ in range(rows)]
  for i in range(rows):
    for j in range(cols):
      result[i][j] = matrix1[i][j] + matrix2[i][j]
  return result
# Output
# [[3, 7], [9, 11]]
# 2.. Flatten Nested List: Write a Python program to flatten a given nested list and convert it into a
# single-dimensional list.
def flatten_nested_list(nested_list):
  """
  Flattens a nested list into a single-dimensional list.

  Args:
    nested_list: The nested list to flatten.

  Returns:
    The flattened list.
  """
  flat_list = []
  for item in nested_list:
    if isinstance(item, list):
      flat_list.extend(flatten_nested_list(item))
    else:
      flat_list.append(item)
  return flat_list
# Output
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 3. List Element Frequency: Given a nested list containing lists of integers, write a Python program
# to count the frequency of each element in the entire nested list.
def list_element_frequency(nested_list):
  """
  Counts the frequency of each element in a nested list.

  Args:
    nested_list: The nested list to analyze.

  Returns:
    A dictionary where keys are elements and values are their frequencies.
  """
  frequency = {}
  for sublist in nested_list:
    for element in sublist:
      if element in frequency:
        frequency[element] += 1
      else:
        frequency[element] = 1
  return frequency
# Output
#{1: 2, 2: 2, 3: 2, 4: 2, 5: 2, 6: 2, 7: 2, 8: 2, 9: 2, 10: 2}
# 4.. Transpose Matrix: Write a Python program to transpose a given matrix represented as a nested
# list.
def transpose_matrix(matrix):
  """
  Transposes a matrix represented as a nested list.

  Args:
    matrix: The matrix to transpose.

  Returns:
    The transposed matrix.
  """
  rows = len(matrix)
  cols = len(matrix[0])
  transposed_matrix = [[0 for _ in range(rows)] for _ in range(cols)]
  for i in range(rows):
    for j in range(cols):
      transposed_matrix[j][i] = matrix[i][j]
  return transposed_matrix
# Output
#[[1, 4], [2, 5], [3, 6]]
# 5. List of Lists Concatenation: Given a list of nested lists, write a Python program to concatenate
# all the sublists into a single flat list.
def list_of_lists_concatenation(nested_list):
  """
  Concatenates all sublists of a nested list into a single flat list.

  Args:
    nested_list: The nested list to concatenate.

  Returns:
    The concatenated flat list.
  """
  flat_list = []
  for sublist in nested_list:
    flat_list.extend(sublist)
  return flat_list
# Output
#[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 6. Tuple Concatenation: Write a Python program to concatenate two tuples and create a new tuple.
def tuple_concatenation(tuple1, tuple2):
  """
  Concatenates two tuples into a new tuple.

  Args:
    tuple1: The first tuple.
    tuple2: The second tuple.

  Returns:
    The concatenated tuple.
  """
  return tuple1 + tuple2
# Output
#(1, 2, 3, 4, 5, 6)
# 7. Tuple Unpacking: Given a tuple with three elements (x, y, z), write a Python program to unpack
# the tuple and assign the values to three variables.
def tuple_unpacking(tuple):
  """
  Unpacks a tuple with three elements and assigns them to variables.

  Args:
    tuple: The tuple to unpack.
  """
  x, y, z = tuple
  return x, y, z
# Output
#(1, 2, 3)
# 8. Tuple Sorting: Write a Python program to sort a tuple of integers in ascending order.
def tuple_sorting(tuple):
  """
  Sorts a tuple of integers in ascending order.

  Args:
    tuple: The tuple to sort.

  Returns:
    The sorted tuple.
  """
  sorted_tuple = tuple(sorted(tuple))
  return sorted_tuple
# Output
#(1, 2, 3, 4, 5)
# 9. Tuple Frequency Count: Given a tuple containing various elements, write a Python program to
# count the frequency of a specific element in the tuple.
def tuple_frequency_count(tuple, element):
  """
  Counts the frequency of a specific element in a tuple.

  Args:
    tuple: The tuple to analyze.
    element: The element to count.

  Returns:
    The frequency of the element in the tuple.
  """
  frequency = tuple.count(element)
  return frequency
# Output
#2
# 10. Tuple to List: Write a Python program to convert a tuple into a list.
def tuple_to_list(tuple):
  """
  Converts a tuple into a list.

  Args:
    tuple: The tuple to convert.

  Returns:
    The converted list.
  """
  return list(tuple)
# Output
#[1, 2, 3, 4, 5]
# 11. Tuple Reversal: Write a Python program to reverse a tuple without using any built-in functions.
def tuple_reversal(tuple):
  """
  Reverses a tuple without using built-in functions.

  Args:
    tuple: The tuple to reverse.

  Returns:
    The reversed tuple.
  """
  reversed_tuple = tuple[::-1]
  return reversed_tuple
# Output
#(5, 4, 3, 2, 1)
# 12. Tuple Slicing: Given a tuple, write a Python program to extract a slice of elements from it.
def tuple_slicing(tuple, start, end):
  """
  Extracts a slice of elements from a tuple.

  Args:
    tuple: The tuple to slice.
    start: The starting index of the slice.
    end: The ending index of the slice (exclusive).

  Returns:
    The sliced tuple.
  """
  return tuple[start:end]
# Output
#(2, 3, 4)
# 13. Duplicate Removal: Write a Python program that takes a list of elements as input and creates a
# new set containing only the unique elements from the list.
def duplicate_removal(list):
  """
  Removes duplicate elements from a list and returns a set of unique elements.

  Args:
    list: The list to remove duplicates from.

  Returns:
    A set containing only the unique elements from the list.
  """
  return set(list)
# Output
#{1, 2, 3, 4, 5}
# 15:Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the
# resulting list. If a list has an odd number of elements, leave the last element in place.
def swap_adjacent_items(numbers):
  """
  Swaps adjacent items in a list in pairs.

  Args:
    numbers: The list of numbers to swap.

  Returns:
    The list with swapped items.
  """
  for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
  return numbers
# Output
#[2, 1, 4, 3, 5]
# 16.Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the
# resulting list.
def swap_min_max(numbers):
  """
  Swaps the minimal and maximal elements in a list.

  Args:
    numbers: The list of numbers to swap.

  Returns:
    The list with swapped minimal and maximal elements.
  """
  min_index = numbers.index(min(numbers))
  max_index = numbers.index(max(numbers))
  numbers[min_index], numbers[max_index] = numbers[max_index], numbers[min_index]
  return numbers
# Output
#[5, 2, 3, 4, 1]
# 17. Write a Python program to count the number of strings from a given list of strings. The string length is
# 2 or more and the first and last characters are the same.
def count_strings(strings):
  """
  Counts strings in a list that have a length of at least 2 and the same first and last characters.

  Args:
    strings: The list of strings to count.

  Returns:
    The number of strings that meet the criteria.
  """
  count = 0
  for string in strings:
    if len(string) >= 2 and string[0] == string[-1]:
      count += 1
  return count
# Output
#2
# 18. Write a python program which contains a list of the some names of items.
# case-01:Find out the length of each item and store in an another list.
# case-02:Access each item's name and convert the lower case letters into uppercase as well as convert the
# uppercase letters into lowercase letters.
def process_names(names):
  """
  Processes a list of names by:

  1. Finding the length of each name and storing it in a separate list.
  2. Converting lowercase letters to uppercase and uppercase letters to lowercase.

  Args:
    names: The list of names.

  Returns:
    A tuple containing:
      - The list of lengths of the names.
      - The list of names with case conversions.
  """
  lengths = [len(name) for name in names]
  converted_names = [name.swapcase() for name in names]
  return lengths, converted_names
# Output
#[3, 3, 3, 4], ['ABC', 'XYZ', 'ABA', '1221']