
# UVSim Simulator : Instruction & Usage Guide


Welcome to UVSim! This software simulator is designed for computer science 
students to explore the fundamentals of machine language and computer architecture. 
UVSim acts as a simple yet powerful virtual machine capable of interpreting and 
executing machine language programs written in BasicML.

## SYSTEM OVERVIEW

* Memory: Equipped with a 100-word memory layout, referenced via location 
  numbers 00 through 99.
* Words: All information is handled in "words." A word is a signed four-digit 
  decimal number (e.g., +1234, -5678).
* Architecture: Contains a virtual CPU and an Accumulator—a specialized 
  register used to hold data values during mathematical calculations.
* Execution: BasicML programs load starting at memory location 00. Each 
  instruction occupies exactly one word. Instructions always carry a plus (+) 
  sign, whereas standalone data words can be plus (+) or minus (-).

## PREREQUISITES & COMPILATION
Included is a compiled executable for unix systems (UVSim) and windows (UVSim.exe)

FOR WINDOWS:

    From the Command Prompt enter the path to the .exe file and press enter, for example:
    
    C:\Users\windowsuser>H:\UVSim.exe
    Enter the name of your input file: H:test_programs\Test1.txt
    File reading successful!
    Please enter up to a 4 digit number: 9999
    Please enter up to a 4 digit number: 9999
    Content in address 9: +9999
    Ending Program...

This version of UVSim is built using C++. To compile and execute this project, 
ensure you have a standard C++ compiler installed on your system.

Recommended Tooling:
* GCC/G++ compiler (or Clang/MSVC depending on your OS)
* Terminal or Command Prompt access

How to Compile:
Open your command line interface, navigate to the source directory, and run 
the following compilation command:

    g++ -std=c++17 -o UVSim UVSim.cpp
    clang++ -std=c++17 -o UVSim UVSim.cpp

## HOW TO RUN & USE

1. Prepare your BasicML file: 
   Create a standard text file (.txt extension required) containing your 
   BasicML opcodes. Each opcode must be on its own line and follow the signed 
   five-character format (e.g., +1005). Your program *must* include a HALT 
   instruction (+4300) to terminate safely.

2. Launch the application:
   Execute the compiled binary from your terminal:
   
    ./UVSim

3. Provide the input file:
   The application will immediately prompt you: "Enter the name of your input file: "
   Type the exact name of your text file (e.g., program.txt) and press Enter.

4. Run-Time Interaction:
   * READ Operations (+10XX): If your script executes a READ, the simulator 
     will pause and ask you to "Please enter up to a 4 digit number: ". Type 
     the number and hit Enter.
   * WRITE Operations (+11XX): Prints out the exact contents stored at the 
     requested memory register straight to your console screen.

## BASICML VOCABULARY REFERENCE 

An instruction word breaks down into two halves:
* First 2 Digits: Operation Code (Opcode) 
* Last 2 Digits: Operand (Target Memory Address)

### I/O Operations
* 10 (READ):   Reads a word from keyboard into a specific memory address.
* 11 (WRITE):  Outputs a word from a specific memory address to the screen.

### Load/Store Operations
* 20 (LOAD):   Loads a word from a memory location directly into the accumulator.
* 21 (STORE):  Saves the word in the accumulator into a memory location.

### Arithmetic Operations
* 30 (ADD):      Adds memory location word to accumulator word; leaves result 
                 in accumulator.
* 31 (SUBTRACT): Subtracts memory location word from accumulator word; leaves 
                 result in accumulator.
* 32 (DIVIDE):   Divides accumulator word by memory location word; leaves 
                 result in accumulator (Includes divide-by-zero protection).
* 33 (MULTIPLY): Multiplies memory location word by accumulator word; leaves 
                 result in accumulator.

### Control Operations
* 40 (BRANCH):     Jumps execution directly to a specific memory location.
* 41 (BRANCHNEG):  Jumps to a specific memory location if accumulator is negative.
* 42 (BRANCHZERO): Jumps to a specific memory location if accumulator is zero.
* 43 (HALT):       Terminates program execution safely.

## SYSTEM ERROR HANDLING 
It safely flags and terminates on the following structural issues:
* Non-integer or improperly formatted opcodes (must match strict 5-character length)
* Input files exceeding the strict 100-word memory limit
* Missing critical HALT (+43XX) instructions required for execution initialization
* File type mismatch (ensures .txt structure)



