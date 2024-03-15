sample_strings = ["blue", "red", "green", "black", "purple"]
sort_by_length = lambda x: (len(x), x)  
sorted_string = sorted(sample_strings, key=sort_by_length)
print(sorted_string)