# File: RetrieverASM.py
# Author: Daudi Mwangi
# Date: 4/14/2023
# Section: 16
# E-mail: daudim1@umbc.edu
# Description: This is a program that emulates the Assembly language, read a file with
#              simplified assembly code and make it run correctly so that the program
#              runs as intended.


# function to handle move commands
# moves one location or value to another destination
def MOV(destination, sourceorval):
    source = ""
    value = ""
    goingto = int(destination[1])
    if "[" in sourceorval: # if it is a location
        source = int(sourceorval[1])
        RAM[goingto] = RAM[source]

    else: # if it is not a location
        value = sourceorval
        RAM[goingto] = value


# function to handle ADD commands
# function that either adds two values, two locations or a location
# and a value then puts it at the destination.
def ADD(destination, locorval1, locorval2):
    val1 = 0
    val2 = 0
    goingto = int(destination[1])

    if "[" in locorval1: # if it is a location
        val1 = RAM[int(locorval1[1])]
    else: # if not a location
        val1 = int(locorval1)

    if "[" in locorval2:
        val2 = RAM[int(locorval2[1])]
    else:
        val2 = int(locorval2)

    RAM[goingto] = int(val1) + int(val2)

# function to handle SUB commands
# function that either subtracts two values, two locations or a location
# and a value then puts it at the destination.
# subtracts the first value by the second value
def SUB(destination, locorval1, locorval2):
    val1 = 0
    val2 = 0
    goingto = int(destination[1])

    if "[" in locorval1:
        val1 = RAM[int(locorval1[1])]
    else:
        val1 = int(locorval1)

    if "[" in locorval2:
        val2 = RAM[int(locorval2[1])]
    else:
        val2 = int(locorval2)

    RAM[goingto] = int(val1) - int(val2)

# function to handle MUL commands
# function that either multiplies two values, two locations or a location
# and a value then puts it at the destination.
def MUL(destination, locorval1, locorval2):
    val1 = 0
    val2 = 0
    goingto = int(destination[1])

    if "[" in locorval1:
        val1 = RAM[int(locorval1[1])]
    else:
        val1 = int(locorval1)

    if "[" in locorval2:
        val2 = RAM[int(locorval2[1])]
    else:
        val2 = int(locorval2)

    RAM[goingto] = int(val1) * int(val2)

# function to handle DIV commands
# function that either divides two values, two locations or a location
# and a value then puts it at the destination.
def DIV(destination, locorval1, locorval2):
    val1 = 0
    val2 = 0
    goingto = int(destination[1])

    if "[" in locorval1:
        val1 = RAM[int(locorval1[1])]
    else:
        val1 = int(locorval1)

    if "[" in locorval2:
        val2 = RAM[int(locorval2[1])]
    else:
        val2 = int(locorval2)

    if val2 != 0:
        RAM[goingto] = int(val1) / int(val2)

# function to handle MOD commands
# function that either mods two values, two locations or a location
# and a value then puts it at the destination.
def MOD(destination, locorval1, locorval2):
    val1 = 0
    val2 = 0
    goingto = int(destination[1])

    if "[" in locorval1:
        val1 = RAM[int(locorval1[1])]
    else:
        val1 = int(locorval1)

    if "[" in locorval2:
        val2 = RAM[int(locorval2[1])]
    else:
        val2 = int(locorval2)

    RAM[goingto] = int(val1) % int(val2)

# function to handle CMP commands
# function that either compares two values, two locations or a location
# and a value then returns the relationship between them in string form.
def CMP(locorval1, locorval2):
    val1 = 0
    val2 = 0

    if "[" in locorval1:
        val1 = RAM[int(locorval1[1])]
    else:
        val1 = int(locorval1)

    if "[" in locorval2:
        val2 = RAM[int(locorval2[1])]
    else:
        val2 = int(locorval2)

    if int(val1) == int(val2):
        return "equal to"
    elif int(val1) > int(val2):
        return "greater than"
    else:
        return "less than"

# function to handle INT commands
# a function that either prints a location or a value
# can also take input and puts it into a destination.
def INT(inputprint, location):
    if inputprint.upper() == "PRINT":
        if "[" in location:
            print(RAM[int(location[1])])
        else:
            print(location)
    else:
        goingto = int(location[1])
        RAM[goingto] = input(">>")


if __name__ == '__main__':

    filenram = input("What file should we assemble and what size of ram should we use?").split()
    RAM = list()
    for i in range(int(filenram[1])): # make a list of zeroes with length given by the user.
        RAM.append(0)
    pointer = 0 # keeps track of the current command
    int(pointer)
    file1 = open(filenram[0], "r")
    commands = list()
    conditional = ""

# copy each line in the file and append it to a seperate list to search through later.
    for line in file1:
        # strip to get rid of invisible characters.
        # split to seperate the command with the values or locations
        command = (line.strip()).split()
        commands.append(command)

    # close the file after opening it.
    file1.close()

# while the pointer is less than the length of the commands
    while pointer < len(commands):
        # use .upper in case the command is in lowercase
        if commands[pointer][0].upper() == "ADD":
            # add two values and put it into commands at index pointer at index 1
            ADD(commands[pointer][1], commands[pointer][2], commands[pointer][3])
        elif commands[pointer][0].upper() == "SUB":
            SUB(commands[pointer][1], commands[pointer][2], commands[pointer][3])
        elif commands[pointer][0].upper() == "MUL":
            MUL(commands[pointer][1], commands[pointer][2], commands[pointer][3])
        elif commands[pointer][0].upper() == "MOD":
            MOD(commands[pointer][1], commands[pointer][2], commands[pointer][3])
        elif commands[pointer][0].upper() == "JMP":
            pointer = int(commands[pointer][1])
        elif commands[pointer][0].upper() == "CMP":
            conditional = CMP(commands[pointer][1], commands[pointer][2])
        elif commands[pointer][0].upper() == "MOV":
            MOV(commands[pointer][1], commands[pointer][2])
        elif commands[pointer][0].upper() == "DIV":
            DIV(commands[pointer][1], commands[pointer][2], commands[pointer][3])
        elif commands[pointer][0].upper() == "INT":
            INT(commands[pointer][1], " ".join(commands[pointer][2:len(commands)]))
        elif commands[pointer][0].upper() == "JG":
            if (conditional == "greater than"):
                # if the conditional is greater than then set
                # the pointer to what we want - 1
                # because at the end of the loop it will be
                # added by one so we land at what we want
                # beginning of the next loop.
                pointer = int(commands[pointer][1]) - 1
        elif commands[pointer][0].upper() == "JLE":
            if (conditional == "equal to" or conditional == "less than"):
                pointer = int(commands[pointer][1]) - 1
        elif commands[pointer][0].upper() == "JGE":
            if (conditional == "greater than" or conditional == "equal to"):
                pointer = int(commands[pointer][1]) - 1
        elif commands[pointer][0].upper() == "JE":
            if (conditional == "equal to"):
                pointer = int(commands[pointer][1]) - 1
        elif commands[pointer][0].upper() == "JL":
            if (conditional == "less than"):
                pointer = int(commands[pointer][1]) - 1
        elif commands[pointer][0].upper() == "JNE":
            if (conditional != "equal to"):
                pointer = int(commands[pointer][1]) - 1
        else:
            # if the command is HLT then it will make the loop
            # condition false so that we do not loop through it again.
            pointer = int(len(commands))
        # add the pointer by one because we do not
        # want the loop to run forever and because
        # we want to go through all of the commands
        # in the list.
        pointer += 1
