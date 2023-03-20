def print_intro():
    print("*" * 38)
    print("**    Welcome to the Snakes Cafe!   **")
    print("**    Please see our menu below.    **")
    print("**")
    print('** To quit at any time, type "quit" **')
    print("*" * 38)
    print("")

def print_menu():
    print("Appetizers")
    print("----------")
    for x in appetizers: print(x.capitalize())
    print("")

    print("Entrees")
    print("----------")
    for x in entries: print(x.capitalize())
    print("")

    print("Desserts")
    print("----------")
    for x in desserts: print(x.capitalize())
    print("")

    print("Drinks")
    print("----------")
    for x in drinks: print(x.capitalize())
    print("")

def print_order_prompt():
    print("*" * 38)
    print("** What would you like to order? **")
    print("*" * 38)
    print("")

def get_user_input():
    user_input = input("> ")
    return user_input.lower()

def quit_application():
    print("Your order is:")
    print(order)
    print("Thank you for using the Snakes Cafe!")

# variables
appetizers = ["Wings", "Cookies", "Spring Rolls"]
entries = ["Salmon", "Steak", "Meat Tornado", "A Literal Garden"]
desserts = ["Ice Cream", "Cake", "Pie"]
drinks = ["Coffee", "Tea", "Unicorn Tears"]
menu = appetizers + entries + desserts + drinks
for i in range(len(menu)):
    menu[i] = menu[i].lower()

order = []

print_intro()
print_menu()
print_order_prompt()
input_selection = get_user_input()

while input_selection.lower() != "quit":



    if input_selection in menu:
        # If item is in menu, add to order
        order.append(input_selection)


        # count number of times that item is in the order.
        count = 0
        for x in order:
            if x == input_selection:
                count = count + 1

        # if 1
        if count == 1:
            print("")
            print("**", count, "order of", input_selection.capitalize(), "have been added to your meal", "**")
            print("")
        else:
            print("")
            print("**", count, "orders of", input_selection.capitalize(), "have been added to your meal", "**")
            print("")
    else:
        print("Sorry, that item is not on the menu")

    # get more items
    input_selection = get_user_input()
else:
    quit_application()






