Usage:
- The source file name must be placed after the script name (Option: -I):
- - prot_gen_cpp.py main.cpp
- - prot_gen_cpp.py scketch.ino
-
- Options:
- - If only the name of the source file is given,
    by default it prints in the terminal and
    saves it in the PropTypes.txt file
-
- - If after the name of the source file, -I is entered,
    then prints it in the terminal and saves it in the
    ProTotypes.txt file, but above the first routine
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
- Prototypes already present in the code are not listed
