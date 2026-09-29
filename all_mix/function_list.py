def intersection(list1, list2):
    return list(set(list1) & set(list2))


list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

result = intersection(list1, list2)
print("Intersection:", result)
