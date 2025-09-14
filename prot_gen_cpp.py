#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Prototype generator for code functions
    
    By RTEK1000 - Mar/20/2024
    
    https://github.com/rtek1000/CPlusPlus_Prototype_Generator

    Usage:
    - The source file name must be placed after the script name (Option: -I):
    - - prot_gen_cpp.py main.cpp
    - - prot_gen_cpp.py scketch.ino
    - - prot_gen_cpp.py main.cpp -I
    - - prot_gen_cpp.py scketch.ino -I
    -
    - Options:
    - - If only the name of the source file is given,
        by default it prints in the terminal and
        saves it in the ProTypes.txt file
    -
    - - If after the name of the source file, -I is entered,
        then prints it in the terminal and saves it in the
        ProTypes.txt file, but above the first routine
        found along with the code found in the source file

    Rules:
    - The function must be aligned in the first column
    - - Use automatic indentation before generating the prototypes:
    - - - VScode auto indent shortcut: Control + Shift + I
    - - - - (Some extensions may interfere with this)
    - - - Arduino IDE auto indent shortcut: Control + T
    -
    - If necessary, add the keyword to the 'header_list' variable (void, uint, String etc)
    - - The keyword does not need to be complete (uint: uint8_t, uint32_t)

    Info:
    - Function prototypes with multiple lines are supported
    -
    - Prototypes already present in the code are listed

- Referece: https://cplusplus.com/doc/tutorial/variables/
"""

import os.path
import sys

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
    
#  Main definition
def main():
    #  If any keyword is missing, put it here:
    header_list = [
        "char",
        "wchar",
        "signed",
        "unsigned",
        "short",
        "int",
        "long",
        "float",
        "double",
        "bool",
        "void",
        "byte",
        "word",
        "const",
        "decltype",
        "uint",
        "String",
    ]
    
    prototypes_list = []
    
    source_list = []

    #  Print 1 empty line
    print()

    filename = ""
    
    fileType1 = ""
    
    filename2 = "ProTypes.txt"

    insertIntoCode = False

    try:
        filename = sys.argv[1]
    except IndexError:
        print("Error, the source file name must be placed after the script name:\r\n")
        print("Example: C:\>prot_gen_cpp.py main.cpp")
        print("- Print and save in " + filename2 + " file")
        print("Optional: C:\>prot_gen_cpp.py main.cpp -I")
        print("- Print and save in the " + filename2 + " file betweet the source code\r\n")
        print("Example: C:\>prot_gen_cpp.py sketch.ino")
        print("Optional: C:\>prot_gen_cpp.py sketch.ino -I\r\n")
        print("Example: $prot_gen_cpp.py sketch.ino")
        print("Optional: $prot_gen_cpp.py sketch.ino -I\r\n")
        return 0

    check_file = os.path.isfile(filename)

    if check_file == False:
        print("File not found: ", filename)
        return 0
    
    try:
        if sys.argv[2].upper() == "-I":
            insertIntoCode = True
    except IndexError:
        insertIntoCode = False
  
    if insertIntoCode == True:
        print("The user chose to insert the prototypes into the source file code: " + filename + "\r\n")
        print("The output filename is: " + filename2 + "\r\n")
        
        if "." in filename:
            filenameSplited = filename.lower().split(".")
            if len(filenameSplited) == 2:
                if filenameSplited[1] == "ino" or filenameSplited[1] == "pde":
                    fileType1 = "setup"
                    print("file type: setup")
                else:
                    fileType1 = "main"
                    print("file type: main")
            else:
                print("1- source file name not recognized")
        else:
            print("2- source file name not recognized")
    #  Open file, read only
    file1 = open(filename, "r")
    
    check_file2 = os.path.isfile(filename2)
    
    userInputVal = "n"
    
    if check_file2 == True:
        userInputVal = input("File " + filename2 + " exists. Do you want to replace the file? (Default: n) [y/n]:")
    
    print(os.path.join(__location__, filename2))
    
    print()
    
    if check_file2 == True:
        if userInputVal != "y":
            print("File will not be replaced, just output to the terminal\r\n")
        else:
            try:
                if userInputVal == "y":
                    file2 = open(os.path.join(__location__, filename2), "w")
                    file2.close()
            except FileNotFoundError:
                print("Error creating file: " + filename2 + "\r\n")
    else:
        try:
            file2 = open(os.path.join(__location__, filename2), "w")
            file2.close()
        except FileNotFoundError:
            print("Error creating file: " + filename2 + "\r\n")
    
    isFileOutputEnabled = False
    
    if check_file2 == False or userInputVal == "y":
        isFileOutputEnabled = True
        
    previousPrototype = ""

    prototypeLine = ""

    isPrototype = False

    codeLine = ""
    
    firstRoutineLocation = 0
    
    lineCounter1 = 0;
    
    firstPrototypeFound = False

    #  Loop
    while True:
        #  Get next line from file
        line = file1.readline()
        
        if insertIntoCode == True:
            #  Store source data
            source_list.append(line)
        #  If line is empty
        if not line:
            #  End Of File is reached
            break
        #  Scan keyword list
        for header in header_list:
            #  Copy line data
            codeLine = line
            #  Is the comment delimiter present?
            if "//" in codeLine or "/*" in codeLine:
                #  Initialize position as 'not present' flag
                delimiterC1 = 0xFFFFFFFF
                #  Initialize position as 'not present' flag
                delimiterC2 = 0xFFFFFFFF
                if "//" in codeLine:
                    #  Save delimiter position "//" and add 1
                    delimiterC1 = codeLine.find("//") + 1
                if "/*" in codeLine:
                    #  Save delimiter position "/*" and add 1
                    delimiterC2 = codeLine.find("/*") + 1
                # Compare position
                if delimiterC1 < delimiterC2:
                    #  Save code only
                    codeLine = codeLine[:delimiterC1]
                if delimiterC1 > delimiterC2:
                    #  Save code only
                    codeLine = codeLine[:delimiterC2]
            #  Get only the first word of the line
            word1 = codeLine.split(" ", 1)[0]
            #  Are the keyword and delimiter present?
            if header == word1 and "(" in codeLine:
                #  Set line as the start of a prototype
                isPrototype = True
            #  Clear codeLine
            codeLine = ""
        #  Has the beginning of a prototype been found?
        if isPrototype == True:
            #  Store subsequent lines
            prototypeLine = prototypeLine + line
        #  Are both delimiters present?
        if "(" in prototypeLine and ")" in prototypeLine:
            #  Save delimiter position ")" and add 1
            delimiterR = prototypeLine.find(")") + 1
            #  Check if line terminator is present
            if ";" in prototypeLine:
                #  Check if the next character is a line terminator
                if prototypeLine[delimiterR] == ";":
                    #  Do not print, it is already a prototype
                    isPrototype = False
            #  Is the character "{" present?
            if "{" in prototypeLine:
                #  Remove the "{" character
                prototypeLine = prototypeLine.replace("{", "")
            #  Insert prototype terminator (";")
            prototypeLine = (
                prototypeLine[:delimiterR] + ";" + prototypeLine[delimiterR:]
            )
            #  Remove from the end anything that is not a readable character from the line
            prototypeLine = prototypeLine.rstrip()
            #  Filter in case line repetition occurs (bug?)
            if prototypeLine != previousPrototype:
                #  As long as there are spaces
                while prototypeLine[0] == " ":
                    #  Remove space
                    prototypeLine = prototypeLine[1:]
                #  Do not print if it is already a prototype
                if isPrototype == True:
                    #  Print prototype
                    print(prototypeLine)
                    #  Save prototype
                    previousPrototype = prototypeLine
                    #  Check if write is enabled for filename2 file
                    if isFileOutputEnabled == True:
                        prototypes_list.append(prototypeLine)
                    #  Get prototypeLine lowercase to compare
                    prototypeLine_lower = prototypeLine.lower()
                    #  If user selected insert prototypes into code
                    if insertIntoCode == True and firstPrototypeFound == False: # and fileType1 in prototypeLine_lower:
                        firstPrototypeFound = True
                        #  Save main() or setup() position
                        firstRoutineLocation = lineCounter1
                        print("firstRoutineLocation: ", firstRoutineLocation)
                    # else:
            #  Clear prototypeLine
            prototypeLine = ""
            #  Clear start of a prototype flag
            isPrototype = False
        # Inc lineCounter1
        lineCounter1 += 1    

    #  Close file
    file1.close()

    if insertIntoCode == True:       
            firstRoutineLocation = firstRoutineLocation

    if isFileOutputEnabled == True:
        lineCounter1 = 0
        try:
            with open(os.path.join(__location__, filename2), "a") as fileOutput:
                if insertIntoCode == True:
                    for source in source_list:
                        #  print("lineCounter1: ", lineCounter1)
                        if firstRoutineLocation == lineCounter1:
                            fileOutput.write("\r\n")
                            fileOutput.write("// Function prototypes (generated by prot_gen_cpp.py):\r\n")
                            for prototype in prototypes_list:
                                fileOutput.write(prototype + "\r\n")
                            fileOutput.write("\r\n")
                            fileOutput.write(source)
                        else:
                            fileOutput.write(source)
                        lineCounter1 += 1
                else:
                    for prototype in prototypes_list:
                        fileOutput.write(prototype + "\r\n")
                      
        except FileNotFoundError:
            print("Error writing file: " + filename2 + "\r\n")

#  Main
if __name__ == "__main__":
    main()
