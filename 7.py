inp = "random"

def show_menu():
    print("Menu")
    print("1. Add an item")
    print("2. Mark as done")
    print("3. View items")
    print("4. Exit")

while inp != '4':
    show_menu()
    inp = input('Enter your choice: ')

    if inp == '1': 
        print("Adding an item to the cart")
    elif inp == '2': 
        print("Marked an item as done")
    elif inp == '3':
        print("Given below all the items")
    elif inp == '4':
        print("Good Bye")
    else:
        print("Invalid inpput. Try again!")

