# simple to-do list app made by thedeadbolt

# defining functions to add, delete, and list tasks:
tasks = []  # array for tasks

def addTask():
    task = input("Enter your task please: ")
    tasks.append(task)
    print(f"Your task: '{task}' has been added to your to-do list!")

def deleteTask():
    listTask()
    try:
        taskToDelete = int(input("Enter the # of the task you want to delete: "))  # input the int of the number task you want to delete
        if 0 <= taskToDelete < len(tasks):
            print(f"Task '{tasks[taskToDelete]}' has been deleted.")
            tasks.pop(taskToDelete)
        else:
            print(f"Task #{taskToDelete} was not found. Select a different task.")
    except (ValueError, IndexError):
        print("Invalid input. Please enter a valid task number.")

def listTask():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):  # for the int. # of the task, in the task list :
            print(f"Task #{index}. {task}")  # prints task number + name

if __name__ == "__main__":  # good practice
    print("Welcome to thedeadbolt's to-do list app!")
    while True:
        print("\nWhat would you like to do?: ")
        print("1. Add a new task.")
        print("2. Delete a task.")
        print("3. List tasks.")
        print("4. Quit thedeadbolt's to-do list app.")
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTask()
        elif choice == "4":
            print("Exiting thedeadbolt's to-do list app. See you soon!")
            break
        else:
            print("Please select a valid option.")



