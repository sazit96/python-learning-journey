not_order = []
order = []

while True:
    item = int(input("New item: "))
    if(item == 0):
        print("Bye!")
        break
    else: 
        not_order.append(item)
        print(f"The list now: {not_order}")
        order = sorted(not_order)
        print(f"The list in order: {order}")