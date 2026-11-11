# UVSim Simulator : Instruction & Usage Guide


Welcome to UVSim! This software simulator is designed for computer science 
students to explore the fundamentals of machine language and computer architecture. 
UVSim acts as a simple yet powerful virtual machine capable of interpreting and 
executing machine language programs written in BasicML.

## SYSTEM OVERVIEW

* Memory: Equipped with a 250-word memory layout, referenced via location 
  numbers 000 through 249.
* Words: All information is handled in "words." A word can be a signed four-digit or six-digit
  decimal number. Four-digit words are converted to six-digit numbers to be used by the simulator
* CPU: A virtual CPU with a program counter (PC) and accumulator (AC).
* Accumulator: A specialized register used to hold data values during arithmetic and memory operations.
* Execution: BasicML programs load starting at memory location 000. Each 
  instruction occupies exactly one word. Instructions always carry a plus (+) 
  sign, whereas standalone data words can be plus (+) or minus (-).
* Instruction format: Each instruction contains an opcode and memory address.
* GUI: The interface allows the user to load files, run programs, input codes and change color settings.
* Memory display: Shows the current state of all 250 memory locations used by the simulator.

## PREREQUISITES
* Python installed on machine
* Tkinter for Python

## HOW TO RUN & USE

1. Prepare your BasicML file: 
   Create a standard text file (`.txt` extension required) containing your 
   BasicML instructions. Each instruction must be on its own line and follow either the signed 
   five-character format, such as `+1005`, or the signed seven-character format, such as `+010005`.
   Five-character words are converted to seven-character words by the simulator. Your program
   must include a HALT instruction, such as `+4300` or `+043000`, to terminate safely.

2. Launch the application:
   Run the `main.py` file.

3. Open an input file:
   Click **Open File** and select a `.txt` BasicML file. The selected file is loaded into the
   memory display starting at memory location `000`.

4. Run the program:
   Click **Run Program** to execute the loaded or manually edited program.

5. Run-time interaction:
   * READ operations, `+10XX` or `+010XXX`, pause execution and request input through the GUI.
     Enter an integer from `-999999` to `999999` in the input field, then click **Accept Input**.
   * WRITE operations, `+11XX` or `+011XXX`, display the contents of the requested memory
     location in the GUI output display.
   * Memory can be manually edited in the memory display before running or saving a program.

6. Change color settings:
   * Click **Color Settings** to choose custom primary, secondary, and text colors.
   * Color changes persist across sessions.
   * Colors can be reset back to the default settings.
   
## BASICML VOCABULARY REFERENCE 

An instruction word breaks down into two halves:
* First 2 or 3 Digits: Operation Code (Opcode) 
* Last 2 or 3 Digits: Operand (Target Memory Address)

### I/O Operations
* 10 or 010(READ):   Reads a word from keyboard into a specific memory address.
* 11 or 011(WRITE):  Outputs a word from a specific memory address to the output display.

### Load/Store Operations
* 20 or 020(LOAD):   Loads a word from a memory location directly into the accumulator.
* 21 or 021(STORE):  Saves the word in the accumulator into a memory location.

### Arithmetic Operations
* 30 or 030(ADD):      Adds memory location word to accumulator word; leaves result 
                 in accumulator.
* 31 or 031(SUBTRACT): Subtracts memory location word from accumulator word; leaves 
                 result in accumulator.
* 32 or 032(DIVIDE):   Divides accumulator word by memory location word; leaves 
                 result in accumulator (Includes divide-by-zero protection).
* 33 or 033(MULTIPLY): Multiplies memory location word by accumulator word; leaves 
                 result in accumulator.

### Control Operations
* 40 or 040(BRANCH):     Jumps execution directly to a specific memory location.
* 41 or 041(BRANCHNEG):  Jumps to a specific memory location if accumulator is negative.
* 42 or 042(BRANCHZERO): Jumps to a specific memory location if accumulator is zero.
* 43 or 043(HALT):       Terminates program execution safely.

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
* Non-integer or improperly formatted opcodes (must match strict 5-character or 7-character length)
* Input files exceeding the strict 250-word memory limit
* Missing critical HALT (+43XX) or (+043XXX) instructions required for execution initialization
* File type mismatch (ensures .txt structure)
* Accumulator overflow is handled by truncating values above +999999 or below -999999
* Halts the program if an infinite branching loop is suspected
