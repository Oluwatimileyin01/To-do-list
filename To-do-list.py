import sys
tasks = []
print("WELCOME TO YOUR TO-D0-LIST.")

def menu():
    print("1.Add Tasks \n2.View Tasks \n3.Delete Tasks \n4.Quit")


def View():
    for x in tasks:
        print(f"Tasks: {x}")
    print("1. Main menu 2. Quit")
    user = int(input("Select: "))
    choice = [1,2]
    if user == 1:
        Main()
    elif user == 2:
        sys.exit()
    while user not in choice:
        print("Invalid input")
        user = input("Select: ")

def Delete():
    print("Tasks: ")
    for x in tasks:
        print(x)
    choice =int(input("Enter the number of task number to delete: "))
    del tasks[choice]
    print("Task deleted successfully")
    print("1. Main menu 2. Quit")
    user = int(input("Select: "))
    choice = [1,2]
    if user == 1:
        Main()
    elif user == 2:
        sys.exit()
    while user not in choice:
        print("Invalid input")
        user = input("Select: ")


def Add():
    task = input("Enter your Task ")
    tasks.append(task)
    print("Task Added \n 1. Add more task \n 2. Main menu")
    user = int(input("Select: "))
    choice = [1,2]
    if user == 1:
        Add()
    elif user == 2:
        Main()
    while user not in choice:
        print("Invalid input")
        user = input("Select: ")


def Main():
    menu()
    user = [1,2,3,4]
    choice = int(input("select "))
    while choice not in user:
        print("Invalid input, Try again")
        choice = int(input("select "))
    if choice ==1:
        Add()
    elif choice == 2:
        View()
    elif choice == 3:
        Delete()
    elif choice == 4:
        sys.exit()

Main()