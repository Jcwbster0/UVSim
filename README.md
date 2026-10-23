
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
* CPU: A virtual CPU with a program counter (PC) and accumulator (AC).
* Accumulator: A specialized register used to hold data values during aritmetic and memory operations.
* Execution: BasicML programs load starting at memory location 00. Each 
  instruction occupies exactly one word. Instructions always carry a plus (+) 
  sign, whereas standalone data words can be plus (+) or minus (-).
* Instruction format: Each instruction contains an opcode and memory address.
* GUI: The interface allows the user to load files, run programs, input codes and change color settings.
* Memory display: Shows the current state of all 100 memory locations used by the simulator.

## PREREQUISITES
* Python installed on machine
* Ktinker for Python

## HOW TO RUN & USE

1. Prepare your BasicML file: 
   Create a standard text file (.txt extension required) containing your 
   BasicML opcodes. Each opcode must be on its own line and follow the signed 
   five-character format (e.g., +1005). Your program *must* include a HALT 
   instruction (+4300) to terminate safely.

2. Launch the application:
   Run the main.py file

3. Provide the input file:
   The application will immediately prompt you to select a file. Press open file and select a file

4. Run the program:
   The application will immediately begin executing your program.

5. Run-Time Interaction:
   * READ Operations (+10XX): If your script executes a READ, the simulator 
     will pause and ask you to "Please enter up to a 4 digit number: ". Type 
     the number and hit Accept Input.
   * WRITE Operations (+11XX): Prints out the exact contents stored at the 
     requested memory register straight to your console screen.
   * Update Memory: Allows you to manually edit the value stored in a specific memory location.
   
6. Change color settings:
   * Change the primary or secondary color of the application by clicking on 
     the color button.
   * Change the text color of the application by clicking on the text color 
     button.
   * Color changes will persist across sessions or can be reset back to default settings.
   
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

## GUI Features
* Open file button: Opens a file dialog to select a BASICML file for execution.
* Run Program button: Executes the loaded file.
* Input field: Allows user to enter input values for READ operations.
* Accept Input button: Submits the input value to the program.
* Output display: Shows the result of executed operations.
* Color Settings button: Opens a color selection dialog.
* Custon colors: Allows users to select custom primary, secondary, and text colors.
* Reset Colors button: Resets the colors to default settings.
* Memory display: Shows the current state of memory locations.

## MEMORY DISPLAY
The memory display shows the current state of memory locations. Allows editing of memory values.

## SYSTEM ERROR HANDLING 
It safely flags and terminates on the following structural issues:
* Non-integer or improperly formatted opcodes (must match strict 5-character length)
* Input files exceeding the strict 100-word memory limit
* Missing critical HALT (+43XX) instructions required for execution initialization
* File type mismatch (ensures .txt structure)
* Accumulator overflow is handled by truncating values above +9999 or below -9999
* Halts the program if an infinite branching loop is suspected



