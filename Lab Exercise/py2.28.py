keys = ["name", "age", "city"]
values = ["Alice", 22, "Mumbai"]

merged_dict = {}

for i in range(len(keys)):
    merged_dict[keys[i]] = values[i]

print("Merged Dictionary:")
print(merged_dict)
