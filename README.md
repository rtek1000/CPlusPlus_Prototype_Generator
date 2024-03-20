# C++ Prototype Generator
Function prototype generator for C++ (Do you want to migrate Arduino IDE code to VS Code?)

----

Usage:

- Rules:

- - The first word on the line must be listed in the 'header_array' variable (void, uint, String etc)

- - The keyword does not need to be complete (uint: uint8_t, uint32_t)

- - The source file name must be placed after the script name, example: prot_gen_cpp.py main.cpp
 
- - Long line wrapping functions are not supported
 
- - The function must be aligned in the first column, use VScode's automatic indentation before generating the prototypes.
- - - VScode auto indent shortcut: Control + Shift + I

----

If you are looking for a way to generate code prototypes in C:

- [C Auto Prototypes](https://marketplace.visualstudio.com/items?itemName=Molitany.c-auto-prototypes)

----

### Licence

This library is free software; you can redistribute it and/or modify it under the terms of the GNU Lesser General Public License as published by the Free Software Foundation; either version 2.1 of the License, or (at your option) any later version.

This library is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along with this library; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
