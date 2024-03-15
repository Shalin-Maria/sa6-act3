numbers = [2, 5, 9, 3, 4]

def find_max_number(numbers_list, compare_func):
  current_max = numbers_list[0]
  for num in numbers_list[1:]:
    if compare_func(current_max, num):
      current_max = num
  return current_max
compare_greater = lambda a, b: a > b and a != b
max_number = find_max_number(numbers, compare_greater)
print(f"The maximum number in the list is: {max_number}")