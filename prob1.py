sum_of_digits = lambda num: sum(int(digit) for digit in str(num))
number = 4465
result = sum_of_digits(number)
print(f"The sum of the digits of {number} is: {result}")