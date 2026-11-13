# Cross Stitch Thread Calculator
### Video Demo:  <https://studio.youtube.com/video/OvWiGXR0gb8/edit>
### Description:
My final project is called Cross Stitch Thread Calculator. The aim of this project is to make it easier to figure out how much thread is needed for a cross stitch project, and how much it will cost to buy it all.

#### Libraries
I only used two libraries in this project: math and os.
I utilised the Math library in order to round numbers up, and the os library to access files in the directory.

#### Constants
Before setting out on this project, I knew that I would need some constant values. These were created from my own needs, as I knew that I was going to be the main user of the program.
**Skein length** defines how long the skein of thread is. In this case, it is 8 meters, but I defined it in centimeters to make it easier to do math with later on in the program.
**Strands used** is how many strands are used during stitching. More strands means less length in total, less strands means more total length of thread.
**Per stitch** is how much thread is used per cross stitch in cm. I worked this out by finding the length of one cross stitch, then working out the hypotenuse, and then addng together the lengths. Equation: (l * 2) + (h * 2)
**Waste** is how much thread used is wasted by jumping stitches, finishing threads, etc. This is an estimate.
**Cost** is how much a skein of thread costs in pence.

#### Main
My main function serves as a main menu for the program, where the user is directed to pick between the main three functions of the program:
- Create new project
- Open existing project
- Delete project

This function has a try/except statement in to catch if a user types in anything other than the three options.

#### Create
The purpose of this function is to create a new text file with the details for a new project to be started.

To start, the user is requested to name their project. This is in a while statement so the user is prompted to name the project until they have a unique project name.
Then, they are prompted to say how many colors they need for the project. This gives a number that the program can loop over to ensure that the user gets the opportunity to input all of the colors they need for their project.
When inputing a color, the user is prompted for the DMC number for the color of thread they require. This is not as simple as limiting the input to an int, as "Blanc" is a valid DMC name in place of the usual numbers. To work around this, the input is taken as a string and checked for if it is "blanc". If the name is not "blanc", the program attempts to turn it into an int. If it cannot achieve this, an error is raised and the function starts again from the beginning.
Once a name is counted as a valid input, the program then requests for the amount of stitches that the color is needed to cover. If anything other than an int is given, an error is raised and the function restarts.
Once these two valid inputs have been given, the program attempts to put them into a list of dictionaries. If the name of the color is already in the dictionary, then the program alerts the user that the color has already been counted.

Once each color has been added to the list of colors, the program goes over all of them to work out how many skeins they need using a custom function called **Calculator**. It uses this number to find out how much money it will cost for the color to be bought in total, also adding this to the list of colors.
Also in this section, a running total of cost, skeins and stitches is counted to be added to the final text document.

This file is created at the end of the function. The file opens a new text document titled the name of the project being created. The project name is added at the top of the file.
Then, the project loops over the list of colors, adding the name of the color, the cost of the color in total, the total stitches of the color, and the amount of skeins needed of the color.
Then, at the bottom of the document, is the project totals for the stitches, skeins, and cost.
Once this is done, the user is moved to the **Results** function. All this function does is read out the same information that is in the text document.

#### Calculator
The calculator function works out how many skeins is needed for a given color. It takes the amount of stitches, and the constants per_stitch, waste, strands_used, and skein_length to work this out.
The first calculation is how much thread is needed for the total stitches. This is worked out with this equation:
> length = (stitches * PER_STITCH) + WASTE

Then, to find out the usable length of a whole skein. This changes depending on how many threads are worked with at a time. This is the equation:
> skeinLength = STRANDS_USED * SKEIN_LENGTH

And then, finally, how many skeins will be needed to cover the total length needed.
> skeins = length/skeinLength

To get the amount of skeins needing to be purchased, this number is rounded up using the **math** library:
> skeins = math.ceil(skeins)

This final number is returned to the **create** function.

#### Open Project
The purpose of this function is to list the avaliable files to read from and let the user select one to look at. It achieves this by using the **os** library.
This is done with the following function:
> os.listdir()

The program looks at all of the items in the directory, and only lists the ones that end in .txt as that is the chosen format for the projects to be listed as. This is alongside a number that the user can input.
Accepting this input is the same as before, where if the number is not in the options, or if the user inputs a non-numerical digit, an error is raised and the user is reprompted to input an answer.
If there are no projects to choose from, the user is asked if they would like to create a project instead. Selecting yes on this question directs the user to the **create** function. Selecting no ends the program. Inputting anything else informs the user that they have made an invalid selection, and the program ends.
Once a valid selection is made, it prints each line to the terminal to show to the reader.

#### Delete
The final function follows a similar structure to the **Open project** function, where it uses the **os** library to show the user all avaliable projects.
It also raises errors in the same places, and follows the same structure.
The only difference is that upon selecting a valid project to delete, the user is asked if they are sure they wish to delete the selected project.
When the user selects yes, the item is deleted using:
> os.remove(projects[choice - 1])

the reason for choice - 1 is because the user may select the 1st entry in a list, but it is actually listed as item 0 in the list, since the computer counts from 0.
Selecting no results in the program ending.
Making an invalid selection results in the function restarting so a valid selection may be made.
