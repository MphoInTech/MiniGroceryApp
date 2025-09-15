user = input("Hello what is your name ?")
print(f"Welcome to LIST-IT APP{user}!!!")

grocery_list = []

while True:
    print("What would you like to do on LIST-IT today ? \n Choose from the options below :")
    print("1. Add an item to the list")
    print("2. Remove an item")
    print("3. View the list")
    print("4. Exit")

    user_input = input("What would you like to do ? ")

    if user_input == "1":
        add_item = input("Please type the item you'd like to add")
        grocery_list.append(add_item)
        print("Item added successfully!")

    elif user_input == "2":
        remove_item = input("Please type the item you'd like to remove")
        if remove_item in grocery_list:
            grocery_list.remove(remove_item)
            print("Item removed successfully!")
        else:
            print("Sorry this item " + remove_item + " is not in the list")
    elif user_input == "3":
        print("Here is your list:")
        for items in grocery_list:
            print(items)
    elif user_input == "4":
        print("Thank you for using LIST-IT" + user + "!" + "\n Here is your final list:")
        grocery_list.sort()
        print(grocery_list)
        break
    else:
        print("Invalid input, Please try again.")
    