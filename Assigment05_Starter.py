# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# NSandhu,5/10/2022,Added code to begin assignment 5
# NSandhu,5/15/2022,Finished main code, began testing
# NSandhu,5/16/2022,Fixed following bugs: data not saving to text file, "data saved" printing multiple times,
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
# strMenu = ""   # A menu of user options // THIS VARIABLE IS NOT USED, MENU IS HARD-CODED (NS, 5/10/22)
strChoice = ""  # A Capture of the user option selection

# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

# Open list file in read mode; cursor position starts at the top of file and moves as it is read
# Loop through all lines (assuming no header), assign data to dicRow, then append dicRow to lstTable
toDoList = open(objFile, "r+")
for strData in toDoList:
    row = strData.split(",")
    dicRow = {"Task": row[0], "Priority": row[1].strip()}
    lstTable.append(dicRow)
toDoList.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while True:
    print("""
    Menu of Options
    1) Show current data
    2) Add a new Task to your To-Do List
    3) Remove an existing Task from To-Do List
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if strChoice.strip() == '1':
        print("Here is a summary of current items in the table:")
        for row in lstTable:
            print(f"Task: {row['Task']},  Priority: {row['Priority']}")
        continue
    # Step 4 - Add a new item to the list/Table
    elif strChoice.strip() == '2':
        dicRow = {"Task": input("Please enter Task Name: "), "Priority": input("Please enter Task Priority: ")}
        lstTable.append(dicRow)
        print("Data has been added to the list!")
        continue
    # Step 5 - Remove a new item from the list/Table
    elif strChoice.strip() == '3':
        userListDel = input("Would you like to remove a Task on the list? Enter Y or N: ")
        while True:
            if userListDel.lower() == "y":
                userTaskDel = input("Enter Task Name to remove: ")
                i = 0
                flag = 0
                for data in lstTable:
                    if data["Task"].lower() == userTaskDel.lower():
                        print(f"The following Task has been removed: {data['Task']}")
                        flag = 1
                        i += 1
                        lstTable.remove(data)
                    else:
                        i += 1
                        if i == len(lstTable) and flag == 0:
                            print("Task not found.")
                break
            elif userListDel.lower() == "n":
                print("List unchanged. Returning to main menu...")
                break
            else:
                print("Please select either Y or N: ")
                continue
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif strChoice.strip() == '4':
        toDoList = open(objFile, "w+")
        for data in lstTable:
            toDoList.write(str(data["Task"]) + "," + str(data["Priority"]) + "\n")
        print("Data written to file!")
        toDoList.close()
        continue
    # Step 7 - Exit program
    elif strChoice.strip() == '5':
        print("Program will end when 'Enter' is pushed...")
        input()
        break  # and Exit the program
    else:
        print("This is not a valid menu option, please select again.")
