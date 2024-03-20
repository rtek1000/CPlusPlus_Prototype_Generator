Usage:

- Rules:

- - The first word on the line must be listed in the 'header_array' variable (void, uint, String etc)

- - The keyword does not need to be complete (uint: uint8_t, uint32_t)

- - The source file name must be placed after the script name:
- - - prot_gen_cpp.py main.cpp
- - - prot_gen_cpp.py scketch.ino

- - Long line wrapping functions are not supported

- - The function must be aligned in the first column, use VScode's automatic indentation before generating the prototypes.
- - - VScode auto indent shortcut: Control + Shift + I
