numbers = [1, 2, 3]
n = 2
power_lambda = lambda x: x ** n 
powered_numbers = list(map(power_lambda, numbers))
print(f"The list of numbers raised to the power of {n} is: {powered_numbers}")