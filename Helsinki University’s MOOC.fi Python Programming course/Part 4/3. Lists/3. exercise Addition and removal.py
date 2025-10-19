my_list = []
print("The list is now",my_list)

while True: 
    choice = input("a(d)d, (r)emove or e(x)it: ")
    if choice == 'd':
        if len(my_list) == 0:
            my_list.append(1)
        else: 
            my_list.append(my_list[-1] + 1)
        print("The list is now",my_list)
    elif choice == 'r':
        my_list.pop()
        print("The list is now",my_list)
    elif choice == 'x':
        print("BYE!")
        break