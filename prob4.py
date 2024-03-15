list1 = [8, 5, 9, 2, 4]
list2 = [1, 2, 8, 3, 7]
intersection = list(filter(lambda x: x in list2, list1))
print(f"The intersection of the lists is: {intersection}")