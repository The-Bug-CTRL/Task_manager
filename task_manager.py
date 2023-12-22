# importing libraries for the functions i need
import os
import datetime

# Get the current script directory
script_directory = os.path.dirname(os.path.abspath(__file__))

# Define the file paths for user and task files
user_file_path = os.path.join(script_directory, 'user.txt')
tasks_file_path = os.path.join(script_directory, 'tasks.txt')

# functions 

#  register user function
def reg_user():
    # Read existing usernames from 'user.txt'
    user_credentials = {}
    with open('user.txt', 'r') as user_file:
        for line in user_file:
            username, _ = line.strip().split(', ')
            user_credentials[username] = None  
    while True:
        new_username = input("Enter the new username: ")
        
        # Check if the username already exists
        if new_username in user_credentials:
            print("Username already exists. Please choose a different one.")
        else:
            new_password = input("Enter the new password: ")
            confirm_password = input("Please confirm the password: ")

            if new_password == confirm_password:
                # Add the new user to the dictionary
                user_credentials[new_username] = new_password
                
                # Append the new user to 'user.txt'
                with open('user.txt', 'a') as user_file:
                    user_file.write(f"\n{new_username}, {new_password}")
                
                print("User registered successfully!")
                break
            else:
                print("Passwords didn't match. Registration failed.")

# generate user reports function
import datetime

# generate user reports function
# this function when called generates statics on 
# the users reports and then displays it for viewing by the admin
def generate_user_reports(logged_in_user, user_credentials, tasks):
    user_count = 0
    task_count = 0
    user_task_counts = {}
    user_completed_tasks = {}
    user_overdue_tasks = {}

# Read user.txt and count the total number of users
    with open('user.txt', 'r') as user_file:
        for line in user_file:
            user_count += 1
    
    with open('tasks.txt', 'r') as tasks_file:
        for line in tasks_file:
            if line.strip():
                parts = line.strip().split(', ')
                username = parts[0]
                task_count += 1
                
                if username in user_task_counts:
                    user_task_counts[username] += 1
                else:
                    user_task_counts[username] = 1

            # Check if the task is completed or overdue
                status = parts[-1]
                if status == 'Yes':
                    user_completed_tasks[username] = user_completed_tasks.get(username, 0) + 1
                elif status == 'No':
                    user_overdue_tasks[username] = user_overdue_tasks.get(username, 0) + 1

# Calculate and print the results
    with open('user_overview.txt', 'w') as result_file:
        result_file.write("User Overview:\n")
        result_file.write(f"Total number of users: {user_count}\n")
        result_file.write(f"Total number of tasks generated: {task_count}\n\n")
        result_file.write("User Task Statistics:\n")
    
        for username in user_task_counts:
            total_tasks = user_task_counts[username]
            completed_tasks = user_completed_tasks.get(username, 0)
            overdue_tasks = user_overdue_tasks.get(username, 0)
        
            result_file.write(f"User: {username}\n")
            result_file.write(f"Total tasks assigned: {total_tasks}\n")
            result_file.write(f"Percentage of tasks assigned to the user: {total_tasks / task_count * 100:.2f}%\n")
            result_file.write(f"Percentage of completed tasks: {completed_tasks / total_tasks * 100:.2f}%\n")
            result_file.write(f"Percentage of tasks that must still be completed: {(total_tasks - completed_tasks) / total_tasks * 100:.2f}%\n")
            result_file.write(f"Percentage of overdue tasks: {overdue_tasks / total_tasks * 100:.2f}%\n\n")

    print("Results have been written to user_overview.txt.")


import datetime
# Generate tasks reports function
# this function produces statistics on the users' tasks and then 
# displays them once the function is called
def generate_task_reports(tasks, logged_in_user):
    total_tasks = 0
    completed_tasks = 0
    uncompleted_tasks = 0
    overdue_tasks = 0
    with open("tasks.txt", "r") as file:
    # Iterate through each line in the file
        for line in file:
            data = line.strip().split(", ")

        # Increment the total tasks counter
            total_tasks += 1

        # Check if the task is completed
            if data[-1] == "Yes":
                completed_tasks += 1
            else:
                uncompleted_tasks += 1
                  # Parse the due date and convert it to a datetime object
        due_date = datetime.datetime.strptime(data[-2], "%d %b %Y")
        current_date = datetime.datetime.today()

        # Check if the task is overdue
        if due_date < current_date:
            overdue_tasks += 1

# Calculate percentages
        percentage_incomplete = (uncompleted_tasks / total_tasks) * 100
        percentage_overdue = (overdue_tasks / total_tasks) * 100

# Print the results
        print(f"Total number of tasks: {total_tasks}")
        print(f"Total number of completed tasks: {completed_tasks}")
        print(f"Total number of uncompleted tasks: {uncompleted_tasks}")
        print(f"Total number of tasks that are overdue: {overdue_tasks}")
        print(f"Percentage of tasks that are incomplete: {percentage_incomplete:.2f}%")
        print(f"Percentage of tasks that are overdue: {percentage_overdue:.2f}%")

        # Create a report as a string
        report = f"Total number of tasks: {total_tasks}\n"
        report += f"Total number of completed tasks: {completed_tasks}\n"
        report += f"Total number of uncompleted tasks: {uncompleted_tasks}\n"
        report += f"Total number of tasks that are overdue: {overdue_tasks}\n"
        report += f"Percentage of tasks that are incomplete: {percentage_incomplete:.2f}%\n"
        report += f"Percentage of tasks that are overdue: {percentage_overdue:.2f}%\n"

           # Save the report to "task_overview.txt"
        with open("task_overview.txt", "w") as report_file:
            report_file.write(report)

import datetime
# function that allows the user to add a task to the task txt file
def add_task(logged_in_user):
    while True:
        due_date = input("Please enter the task's due date (dd mm yyyy): ")
        date_parts = due_date.split()
        if len(date_parts) == 3 and all(part.isdigit() for part in date_parts):
            day, month, year = map(int, date_parts)
            try:
                due_date = datetime.datetime(year, month, day)
                due_date = due_date.strftime("%d %b %Y")
                break
            except ValueError:
                print("Invalid date. Please enter a valid date in the format 'dd mm yyyy'.")
        else:
            print("Invalid date format. Please use the format 'dd mm yyyy'.")
    status = "No"
    while True:
        title = input("Please enter a name for the task: ")
        if title == "":
            print("Please enter a title!")
            continue  
        description = input("Please enter the task's description: ")
        if description == "":
            print("Please enter a description for the task!")
            continue  
        assignee_or_current_user = input("Please enter the username to assign this task or leave blank for your username to be assigned: ")
        if assignee_or_current_user != "":
            username = assignee_or_current_user 
        elif assignee_or_current_user == "":
            username = logged_in_user
            print("The task will be assigned to you!")
        task_data = f'{username}, {title}, {description}, {due_date}, {datetime.datetime.now().strftime("%d %b %Y")}, {status}\n'
        with open('tasks.txt', 'a') as tasks_file:
            tasks_file.write(f"\n{task_data}")
            print("Task added successfully!")
        break 

# function that allows the user to view all tasks in the txt file
def view_all(logged_in_user):
    with open('tasks.txt', 'r') as tasks_file:
        tasks = tasks_file.readlines()
        for task in tasks:
            task_data = [value.strip() for value in task.split(', ')]
            if len(task_data) == 6:
                username, title, description, due_date, current_date, status = task_data
                formatted_description = description.lstrip()
                formatted_description = formatted_description.ljust(60)  
                print(f'''Assigned to: {username}\nTitle: {title}\nDescription:
{formatted_description}\nDue Date: {due_date}\nCurrent Date: {current_date}\nStatus: {status}\n''')

# this function allows the user to view there tasks and then allows them to 
# change the data about the tasks then it also allows them to mark the tasks as completed or not
# and if they dont want to do anything it allows them to enter -1 to return to the menu
# and if there are any wrong inputs the code will print the appropriate messages
def view_mine(logged_in_user):
    if logged_in_user:
        with open('tasks.txt', 'r') as tasks_file:
            tasks = tasks_file.readlines()
            task_number = 1
            uncompleted_tasks = []
            
            for i, task in enumerate(tasks):
                task_data = [value.strip() for value in task.split(', ')]
                if len(task_data) == 6 and task_data[0] == logged_in_user:
                    username, title, description, due_date, current_date, status = task_data
                    if status.lower() == 'no':
                        print(f"Task {task_number}")
                        print(f"Assigned to: {username}\nTitle: {title}\nDescription: {description}\nDue Date: {due_date}\nCurrent Date: {current_date}\nStatus: {status}\n")
                        task_number += 1
                        uncompleted_tasks.append(task)

            if task_number == 1:
                print("You don't have any uncompleted tasks.")
                return

            print('''Please enter the task number you want to interact with or
                     enter -1 to return to the menu!''')
            choice = input("Please enter a number: ")
            
            if choice == '-1':
                return
            elif choice.isdigit():
                choice = int(choice)
                
                if 1 <= choice <= task_number - 1:
                    choice -= 1
                    selected_task_data = uncompleted_tasks[choice].strip().split(', ')
                    username, title, description, due_date, current_date, status = selected_task_data
                    
                    if status.lower() == 'yes':
                        print("This task is already marked as complete. You cannot edit it.")
                        return
                    
                    action = input("What would you like to do? Enter 'e' for editing or 'c' to mark as complete: ")
                    
                    if action == 'e':
                        print("Selected Task Details:")
                        print(f"Assigned to: {username}")
                        print(f"Title: {title}")
                        print(f"Description: {description}")
                        print(f"Due Date: {due_date}")

                        # Prompt the user to enter new task details
                        new_title = input("Enter a new title (or press Enter to keep the existing title): ")
                        new_description = input("Enter a new description (or press Enter to keep the existing description): ")
                        new_due_date = input("Enter a new due date (dd mm yyyy) (or press Enter to keep the existing due date): ")
                        
                        # Update the task data with new values if provided
                        if new_title:
                            selected_task_data[1] = new_title
                        if new_description:
                            selected_task_data[2] = new_description
                        if new_due_date:
                            date_parts = new_due_date.split()
                            if len(date_parts) == 3 and all(part.isdigit() for part in date_parts):
                                day, month, year = map(int, date_parts)
                                try:
                                    due_date = datetime.datetime(year, month, day)
                                    selected_task_data[3] = due_date.strftime("%d %b %Y")
                                except ValueError:
                                    print("Invalid date. Task not updated.")
                                    return  # Exit the function to avoid saving invalid data
                            else:
                                print("Invalid date format. Task not updated.")
                                return  # Exit the function to avoid saving invalid data
                        
                        # Join the updated task data back into a string
                        updated_task = ', '.join(selected_task_data)
                        # Update the task in the original tasks list
                        tasks[tasks.index(uncompleted_tasks[choice])] = updated_task + '\n'
                        
                        # Write all tasks (including the updated one) back to the 'tasks.txt' file
                        with open('tasks.txt', 'w') as tasks_file:
                            tasks_file.writelines(tasks)
                        
                        print("Task updated successfully.")
                    
                    elif action == 'c':
                        # Mark the task as complete
                        selected_task_data[-1] = 'Yes'  # Update the status to 'Yes' for complete
                        updated_task = ', '.join(selected_task_data)
                        tasks[tasks.index(uncompleted_tasks[choice])] = updated_task + '\n'
                        
                        # Write all tasks (including the updated one) back to the 'tasks.txt' file
                        with open('tasks.txt', 'w') as tasks_file:
                            tasks_file.writelines(tasks)
                        
                        print("Task marked as complete.")
                    
                    else:
                        print("Invalid action. Please enter 'e' to edit or 'c' to mark as complete.")
                
                else:
                    print("Invalid task number. Please enter a valid task number.")
            else:
                print("Invalid input. Please enter a valid number.")
    else:
        print("Invalid task number. Please enter a valid task number.")

# finding the paths to the txt files so that the program can access them
script_directory = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_directory)

# checking the user credentials against the user txt file
user_credentials = {}
with open('user.txt', 'r') as user_file:
    for line in user_file:
        username, password = line.strip().split(', ')
        user_credentials[username] = password

# Read existing tasks from 'tasks.txt'
with open('tasks.txt', 'r') as tasks_file:
    tasks = tasks_file.readlines()

with open('user.txt', 'r') as tasks_file:
    tasks = tasks_file.readlines()

with open('task_overview.txt', 'r') as tasks_file:
    tasks = tasks_file.readlines()

with open('user_overview.txt', 'r') as tasks_file:
    tasks = tasks_file.readlines()

#defining the tasks and user variables
tasks = 'tasks.txt'
users = 'user.txt'
user_overview = []
task_overview = []

# ask the user to login then if corrected credentials
# showing them the menu for users
# if credentials are wrong then it will deny access
logged_in_user = None
while True:
    if not logged_in_user:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        if user_credentials.get(username) == password:
            print("Login successful!\n")
            logged_in_user = username
        else:
            print("Invalid credentials. Please try again.\n")

    # displaying the menu for the logged in user
    else:
        menu = input('''Select one of the following options:
r - register a user
a - add task
va - view all tasks
vm - view my tasks
am - To access the Admin tools like generate-reports and display-statistics and see statistics(Admin Only Menu)
e - exit
: ''').lower()

        # if user chooses "r" then the program will run and
        # prompt the user to add a new user if they dont or incorrect credentials
        # the program will stop
        if menu == 'r':
            if logged_in_user == 'admin':
                reg_user()

        # if the user selects "a" the program will ask the user to add a task
        # if they dont, the program will ask the user to enter the right format of date and time
        # if the user wants to add a task to another user the program will ask them to
        # add the username of whom they want to add it to either themselves or another user
        elif menu == 'a':
            add_task(logged_in_user)

        # if the user selects "va" the program wil
        # display all the tasks in the task txt file
        elif menu == 'va':
            view_all(logged_in_user)

        # if the user selects "vm" the program will
        # display the task that that specific user has
        elif menu == 'vm':
            view_mine(logged_in_user)

        # if the user selects "m" this means they are an Admin user
        # and have the privileges to enter the specific password and username of an admin
        # to see the statistics of the users
        # that will be displayed in a separate menu
        # for the admin to select from
        if menu == 'am':
            if logged_in_user == 'admin':
                admin_username = "admin"
                admin_password = "adm1n"
                
                
                if user_credentials.get(admin_username) == admin_password:
                    admin_menu = input('''
Please select the option below for statistics:
gr - generate reports then you can view 
     them with the below options (Admin only) 
s - Statistics (Admin only)
ds - Display Reports (Admin only)
: ''').lower()
                    # if the user is a admin the admin only menu will appear once the admin has logged in 
                    # and the menu will display "s" for the statistics option                    
                    if admin_menu == "s":
                        with open('task_overview.txt', 'r') as file:
                                file_contents = file.read()
                                print(f"the file{'task_overview.txt'} exists, and its contents are:")
                                print(file_contents)
                        with open('user_overview.txt', 'r') as file:
                                file_contents = file.read()
                                print(f"the file{'task_overview.txt'} exists, and its contents are:")
                                print(file_contents)

                    # option gr is used to generate the reports for the users and the tasks
                    elif admin_menu == 'gr':
                        if logged_in_user == 'admin':
                            generate_user_reports(logged_in_user, user_credentials, tasks)
                            generate_task_reports(tasks, logged_in_user)
                            print("reports generated successfully")
                        else:
                            print("you dont have admin privileges to see task and user reports!")


                    # option ds for admins is there to see the more advanced report stats for the users and tasks
                    elif admin_menu == 'ds':
                        if os.path.exists('task_overview.txt') and os.path.exists('user_overview.txt'):
                            with open('task_overview.txt', 'r') as task_file:
                                task_file_contents = task_file.read()
                                print(f"The file 'task_overview.txt' exists, and its contents are:")
                                print(task_file_contents)

                            with open('user_overview.txt', 'r') as user_file:
                                user_file_contents = user_file.read()
                                print(f"The file 'user_overview.txt' exists, and its contents are:")
                                print(user_file_contents)
                        else:
                            print("One or both of the overview files do not exist.")
                            print("Generating the overview files...")

                         # Generate the user and task overview reports
                            generate_user_reports(logged_in_user, user_credentials, tasks)
                            generate_task_reports(logged_in_user, tasks)

                        # Recheck and display the generated overview files
                            with open('task_overview.txt', 'r') as task_file:
                                task_file_contents = task_file.read()
                                print(f"The file 'task_overview.txt' now exists, and its contents are:")
                                print(task_file_contents)

                            with open('user_overview.txt', 'r') as user_file:
                                user_file_contents = user_file.read()
                                print(f"The file 'user_overview.txt' now exists, and its contents are:")
                                print(user_file_contents)
                else:
                    print("you dont have admin credentials!")
            else:
                print("you do not have admin privileges!")
              


        # if the user wants to exit they can do so by 
        # selecting this from the menu and the program will exit        
        elif menu == 'e':
            print('Goodbye!!!')
            exit()