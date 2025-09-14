# C++ Prototype Generator
Function prototype generator for C++ (Do you want to migrate Arduino IDE code to VS Code?)

----

Usage:
- The source file name must be placed after the script name (Option: -I):
- - python prot_gen_cpp.py main.cpp
- - python prot_gen_cpp.py scketch.ino
- - python prot_gen_cpp.py main.cpp -I
- - python prot_gen_cpp.py scketch.ino -I
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

----

If you are looking for a way to generate code prototypes in C:

- [C Auto Prototypes](https://marketplace.visualstudio.com/items?itemName=Molitany.c-auto-prototypes)

----

### Licence

This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
