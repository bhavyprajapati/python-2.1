list1 = ["id", "name", "marks"]
list2 = [101, "Ravi", 89]

result = {}

for i in range(len(list1)):
    result[list1[i]] = list2[i]

print("Dictionary created from two lists:")
print(result)
