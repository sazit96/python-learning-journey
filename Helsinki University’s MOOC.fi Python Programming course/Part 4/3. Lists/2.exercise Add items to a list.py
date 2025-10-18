num_of_items = int(input("How many items: "))
i = 1
total_item = []
while i <= num_of_items:
    item = int(input(f"Item {i}: "))
    total_item.append(item)
    i += 1
print(total_item)
    
    