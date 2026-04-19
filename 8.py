inp = "random"
data = []

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
        item = input("Enter the name of the item: ")
        data.append(item)
        print("Added item:", item)
    elif inp == '2': 
        item = input("What is to be marked as done? ")
        if item in data: 
            data.remove(item)
            print("Removed item: ", item)
        else:
            print("This item doesn't exist.")
    elif inp == '3':
        print("Given below all the items")
        for item in data:
            print(item)
    elif inp == '4':
        print("Good Bye")
    else:
        print("Invalid inpput. Try again!")

