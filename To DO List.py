# TO DO LIST:-
try:
    with open("tasks.txt","r") as file:
        tasks = []
        for line in file:
            task, done_flag = line.strip().split(" | ")
            tasks.append([task, done_flag == "1"])
except FileNotFoundError:
  tasks = []

while True:
    print("\n---TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Edit Task")
    print("4. Remove Task")
    print("5. Exit")

    choice = input("Enter your choice:- ")

    if choice == "1":
        task = input("Enter a task: ")
        tasks.append([task,False])
        print("Task added successfully!")

    elif choice == "2":
        print("\nYour tasks: ")
        if len(tasks) == 0:
            print("No Tasks yet!")
        else:
            for i, task in enumerate(tasks, 1):
                status = "✅" if task[1] else "❌"
                print(f"{i}. {task[0]} {status}")
            
            try:
                num = int(input("Enter task number to toggle status: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1] [1] = not tasks [num - 1] [1]
                    print("status updated successfully!")
            except:
                print("Invalid input")

                

    elif choice == "3":
        print("\nYour tasks: ")
        for i,task in enumerate(tasks,start = 1):
            status = "✅" if task[1] else "❌"
            print(f"{i}. {task[0]} {status}") 

        try:
            num = int(input("Enter task number to edit: "))
            if 1 <= num <= len(tasks):
                new_task = input("Enter the new task: ")
                tasks[num - 1] = new_task
                print("Task updated successfully!")
            else:
                print("Invalid task number!")
        except ValueError:
            print("Please enter a valid number!")



    elif choice == "4":
        num = int(input("Enter task number to remove: "))
        if 0 < num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid number!")

    elif choice == "5":
        with open("tasks.txt","w") as file:
            for task, done in tasks:
                done_flag = "1" if done else "0"
                file.write(f"{task} | {done_flag} \n")
        print("Tasks saved. Exiting...")
        break
    else:
        print("Invalid input try again! ")
        