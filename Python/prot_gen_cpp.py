#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
    Prototype generator for code functions
    
    By RTEK1000 - Mar/20/2024
    
    https://github.com/rtek1000/CPlusPlus_Prototype_Generator

- Rules:
- - The first word on the line must be listed in the header_array variable (void, uint, String etc)
- - The keyword does not need to be complete (uint: uint8_t, uint32_t)
- - The source file name must be placed after the script name: prot_gen_cpp.py main.cpp
- - Long line wrapping functions are not supported
- - The function must be aligned in the first column, use VScode's automatic indentation before generating the prototypes.
- - - VScode auto indent shortcut: Control + Shift + I

- Referece: https://cplusplus.com/doc/tutorial/variables/
"""

import os.path
import sys


#  Main definition
def main():
    #  If any keyword is missing, put it here:
    header_array = ["char", "wchar", "signed", "unsigned", \
                    "short", "int", "long", "float", \
                    "double", "bool", "void", "byte", \
                    "word", "const", "decltype", \
                    "uint", "String"]
    
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

    # Open file, read only
    file1 = open(filename, 'r')
    
    previousPrototype = ""
    
    # Loop
    while True:
        # Get next line from file
        line = file1.readline()
                
        #  If line is empty
        if not line: 
            #  End Of File is reached
            break    
        
        #  Line has at least 3 character?
        if len(line) > 2: 
            #  Get only the first word of the line
            word1 = line.split(' ', 1)[0] 
            #  Word has at least 3 character?
            if len(word1) > 2:   
                #  Scan keyword list
                for header in header_array: 
                    #  Keyword and delimiters found?
                    if header in line and "(" in line and ")" in line:  
                        #  Save position of first delimiter ")" and add 1
                        terminator1 = line.find(")") + 1   
                        #  Is the value of the first terminator greater than 0?
                        if terminator1 > 0:
                            #  Remove from the ends anything that is not a readable character from the line
                            newline = line.strip()    
                            #  Insert prototype terminator (";")
                            newline = newline[:terminator1] + ';' + newline[terminator1:]
                            #  Filter in case line repetition occurs (bug?)
                            if newline != previousPrototype:
                                #  Save prototype
                                previousPrototype = newline
                                #  Print prototype
                                print(newline)    
    # Close file
    file1.close()


#  Main
if __name__ == "__main__":
    main()
