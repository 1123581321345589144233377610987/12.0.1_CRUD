import pickle
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

def menu():
    options = ["1","2","3","4"]
    choice = 0
    while choice not in options:
        print("Welcome to your email list manager!\n")
        print("Enter your selection:")
        print("1. Look up an email by name")
        print("2. Add a new entry")
        print("3. Change a person's email")
        print("4. Delete an entry")
        print("5. Quit")
        choice = input("")
    choice = int(choice)
    return choice


def main():
    try:
        pickled_file = open("pickled_file", "rb")
        customer_file = pickle.load(pickled_file)
        print(customer_file)
        pickled_file.close()
    except:
        customer_file = {}
    choice = 0
    while choice != QUIT:
        choice = menu()
        if choice == LOOK_UP:
            read(customer_file)
        elif choice == ADD:
            create(customer_file)
        elif choice == CHANGE:
            update(customer_file)
        elif choice == DELETE:
            delete(customer_file)


def read(file):
    name = input("Enter a name: ")
    if name in file:
        print(file[name])
    else:
        print("No data found. Try adding a new entry.")


def create(file):
    name = input("Enter a name: ")
    if name not in file:
        email = input("Enter email: ")
        file[name] = email
        save(file)
        print(f"The information you entered for {name} has been saved.")
    else:
        print("This name already exists.")


def update(file):
    yes = ["y", "Y", "YES", "yes", "Yes"]
    name = input("Enter name: ")
    if name in file:
        confirm = input(f"{name}'s email is currently listed as {file[name]}. Are you sure you want to change this? (y/n): ")
        if confirm in yes:
            email = input("Please enter new email: ")
            file[name] = email
            save(file)
            print("Confirmation message")
        else:
            print("No changes made")
    else:
        print("Data not found")


def delete(file):
    yes = ["y", "Y", "YES", "yes", "Yes"]
    name = input("Enter name: ")
    confirm = input("Are you sure you want to delete this entry? (y/n): ")
    if confirm in yes:
        if name in file:
            del file[name]
            save(file)
            print("This is a confirmation message. Your changes have been saved.")
        else:
            print("No changes made.")
    else:
        print("Entry not found.")


def save(file):
    try:
        pickled_file = open("pickled_file", "wb")
        pickle.dump(file, pickled_file)
        pickled_file.close()
    except Exception as exception:
        print("File was unable to be saved.")
        print(exception)

main()
