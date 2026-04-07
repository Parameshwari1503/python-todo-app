tasks = []
while True:
 print("\n--- TO DO LIST ---")
 print("1. Add task")
 print("2. View task")
 print("3. Delete task")
 print("4. Exit")
 choice=input("Enter choice: ")
 if choice == '1':
  task = input("Enter task: ")
  tasks.append(task)
  print("Task added!")

 elif choice == '2':
   print("\nYour Tasks:")
   for i in range(len(tasks)):
     print(i+1,".",tasks[i])

 elif choice=='3':
    num = int(input("Enter task number to delete:"))
    if num <= len(tasks):
      tasks.pop(num - 1)
      print("Task deleted!")
    else:
       print("Invalid number")
       
 elif choice=='4':
    print("Exiting...")
    break
 else:
    print("Invalid choice")
          

   

