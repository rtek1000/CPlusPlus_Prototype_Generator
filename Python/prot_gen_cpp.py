#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Prototype generator for code functions
    
    By RTEK1000 - Mar/20/2024
    
    https://github.com/rtek1000/CPlusPlus_Prototype_Generator

    Usage:
    - The source file name must be placed after the script name:
    - - prot_gen_cpp.py main.cpp
    - - prot_gen_cpp.py scketch.ino

    Rules:
    - The function must be aligned in the first column
    - - Use automatic indentation before generating the prototypes:
    - - - VScode auto indent shortcut: Control + Shift + I
    - - - - (Some extensions may interfere with this)
    - - - Arduino IDE auto indent shortcut: Control + T
    -
    - If necessary, add the keyword to the 'header_array' variable (void, uint, String etc)
    - - The keyword does not need to be complete (uint: uint8_t, uint32_t)

    Info:
    - Function prototypes with multiple lines are supported
    -
    - Prototypes already present in the code are not listed

- Referece: https://cplusplus.com/doc/tutorial/variables/
"""

import os.path
import sys


#  Main definition
def main():
    #  If any keyword is missing, put it here:
    header_array = [
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

    #  Print 1 empty line
    print()

    filename = ""

    try:
        filename = sys.argv[1]
    except IndexError:
        print("Error, the source file name must be placed after the script name:")
        print("Example: C:\prot_gen_cpp.py main.cpp\r\n")
        return 0

    check_file = os.path.isfile(filename)

    if check_file == False:
        print("File not found: ", filename)
        return 0

    #  Open file, read only
    file1 = open(filename, "r")

    previousPrototype = ""

    prototypeLine = ""

    isPrototype = False

    codeLine = ""

    #  Loop
    while True:
        #  Get next line from file
        line = file1.readline()
        #  If line is empty
        if not line:
            #  End Of File is reached
            break
        #  Scan keyword list
        for header in header_array:
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
            #  Clear prototypeLine
            prototypeLine = ""
            #  Clear start of a prototype flag
            isPrototype = False
    #  Close file
    file1.close()


#  Main
if __name__ == "__main__":
    main()
