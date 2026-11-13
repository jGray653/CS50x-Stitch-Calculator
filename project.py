# Libraries to include
import math
import os

# Constants
SKEIN_LENGTH = 800      # In cm
STRANDS_USED = 2        # Strands
PER_STITCH = 0.88       # In cm
WASTE = 10              # In cm
COST = 150              # In pence

# Functions
#---
def main():
    print("Welcome to my crude and hopefully accurate thread calculator for cross stitch products.")
    print("Please select one of the following options: ")
    print("1: Create new project")
    print("2: Open existing project")
    print("3: Delete existing project")
    try:
        choice = int(input("Choice: "))

        if choice == 1:
            create()
        elif choice == 2:
            open_proj()
        elif choice == 3:
            delete()
        else:
            print("Invalid selection, please try again")
    except ValueError: #Raise an error if the user uses anything other than numbers
        print("Please only use numbers")

#---
def create():
    # Total variables
    totStitch = 0
    totSkein = 0
    totCost = 0

    # Create a loop so the user creates a unique project name
    while True:
        name = input("What do you want to call this pattern?: ")
        if os.path.isfile(name + ".txt"):
            print("Project using that name already exists, please try again.")
        else:
            break

    # Allow for as many colors as the user wants
    c = int(input("How many colors are in the pattern?: "))

    colors = []
    print("==============================================")
    # Do the same thing for every color the user needs
    for i in range(c):
        print(f"Color {i + 1}")
        try:
            color = input("What is the DMC Number?: ").lower()
            if color != "blanc":
                color = int(color)

            if not any(t["color"] == color for t in colors): # Add dictionary for the color to list of colors as long as it is not already in there.
                stitch = int(input(f"How many stitches for {color}?: "))
                colors.append({"color" : color, "stitches" : stitch})
            else:
                print("This color has already been counted!")
        except ValueError:  # Raise an error if words other than "blanc" are used
            print("Please only use numerical values.")
            create()        # Start from the beginning of the function

    for c in colors:
        skeins = calculator(c)
        c["skeins"] = skeins

        cost = str((c["skeins"] * COST)/100) + "0"
        c["cost"] = cost

        totCost = totCost + ((c["skeins"] * COST)/100)
        totSkein = totSkein + c["skeins"]
        totStitch = totStitch + c["stitches"]

    # Create a new project file and add all of the needed information to it.
    with open(f"{name}.txt", "a") as file:
        file.write(f"{name}\n")
        file.write("==================================\n")
        for color in colors:
            file.write(f"  DMC {color["color"]}                    {color["cost"]}\n")
            file.write(f"   Stitches: {color["stitches"]}\n")
            file.write(f"   Skeins: {color["skeins"]}\n")
        file.write("==================================\n")

        file.write(f"Total Stitches: {totStitch}\n")
        file.write(f"Total Skeins: {totSkein}\n")
        file.write(f"Total Cost: {totCost}0\n")

    # Show the user the information in the terminal
    results(colors)

#---
def open_proj():
    print("Please select a project to open: ")
    projects = []
    i = 0
    for x in os.listdir(): #Find what project text documents are in the directory
        if x.endswith(".txt"): #If they end with txt, then they can be shown to the user
            i += 1  #Count what number project it is
            projects.append(x)  # add them to a list
            x , _ = x.split(".")    # remove the extension
            print(f"{i}: {x}") #then print them to show the user along with the number that they are

    if not projects: # if there are no projects, offer to create one instead
        print("There are no Projects, Would you like to create one? [y/n]")
        choice = input("Choice: ").lower()
        if choice == "y":
            create() #if yes, then move the user to the create function
        elif choice == "n":
            pass #otherwise, the program ends
        else:
            print("Invalid selection.")
    else: # if there are projects, then continue in this function
        try:
            choice = int(input("Choice: "))

            if projects[choice - 1]: #If the project they chose exists, then print all the lines within the file
                with open(projects[choice - 1]) as file:
                    for line in file:
                        print(line.strip("\n"))
            else: # otherwise, an error is raised and they redo the function
                raise IndexError
        except ValueError:
            print("Please only use numerical values.")
            open_proj()
        except IndexError:
            print("Not a valid project. Please try again.")
            open_proj()

#---
def delete():
    print("Please select a project to delete: ")
    projects = []
    i = 0
    for x in os.listdir(): #listing all existing projects
        if x.endswith(".txt"):
            i += 1
            projects.append(x)
            x , _ = x.split(".")
            print(f"{i}: {x}")

    if not projects: #if no projects exist to delete, then the program ends
        print("There are no Projects to Delete")
    else:
        try: #otherwise, they get the same option as the open project function
            choice = int(input("Choice: "))
            if projects[choice - 1]:
                print(f"Are you sure you want to delete {projects[choice - 1]}? [y/n] ")
                c = input("").lower()

                #user is prompted to make sure that they want to delete the project that they have chosen
                if c == "y": #if yes, then the file is deleted
                    os.remove(projects[choice - 1])
                elif c == "n": #if no, then the program ends
                    pass
                else: #if any invalid answer is given, an error is raised and the user returns to the beginning of the function
                    raise IndexError
        except ValueError:
            print("Please only use numerical values.")
            delete()
        except IndexError:
            print("This is not a valid selection, please try again.")
            delete()

#---
def calculator(color):
    # How much thread is used per color
    # Multiply the perCross by stitches
    # add waste
    stitches = color["stitches"]
    length = (stitches * PER_STITCH) + WASTE

    # How many skiens for that color
    # work out how long skein is when using howmany strands
    skeinLength = STRANDS_USED * SKEIN_LENGTH

    # Divide length by skein length to find out how many skeins is needed
    skeins = length/skeinLength
    skeins = math.ceil(skeins)

    return skeins

#---
def results(colors):
    print("==============================================")
    print("Thread Estimates:")
    for color in colors:
        print(f"  DMC {color["color"]}")
        print(f"    Stitches: {color["stitches"]}")
        print(f"    Skeins: {color["skeins"]}")
        print(f"    Total: £{color["cost"]}")
    print("==============================================")

    totalStitches = 0
    totalSkeins = 0
    totalCost = 0

    for color in colors:
        totalStitches = totalStitches + color["stitches"]
        totalSkeins = totalSkeins + color["skeins"]
        totalCost = totalCost + float(color["cost"])
    totalCost = str(totalCost) + "0"

    print(f"Stitches: {totalStitches}")
    print(f"Skeins: {totalSkeins}")
    print(f"Total: £{totalCost}")


if __name__ == "__main__":
    main()
