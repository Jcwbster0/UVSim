#include <iostream>
#include <fstream>
#include <string>
using namespace std;

// OPERATION FUNCTIONS -----------------------------------------------------------------------------------------
// I/O OPERATION
void read(string memoryList[], int address) { // 10
    int userInput;
    cout << "Please enter up to a 4 digit number: ";
    while (!(cin >> userInput) || userInput > 9999 || userInput < -9999) {  // Keep asking until the user enters a valid number
        cout << "Invalid input. Try again: ";
        cin.clear(); // Reset input errors
        cin.ignore(10000, '\n'); // Remove bad input
    }
    memoryList[address] = to_string(userInput);
}

void write(string memoryList[], int address) { // 11
    cout << "Content in address " << address << ": " << memoryList[address] << endl;
}

// LOAD/STORE OPERATION
int load(string memoryList[], int address) { // 20
    string numStr = memoryList[address];
    int numInt = stoi(numStr);
    return numInt;
}

void store(string memoryList[], int address, int accumulator) { // 21
    memoryList[address] = to_string(accumulator);
}

// ARITHMETIC OPERATION
int add() { // 30
    return 0;
}

int substract() { // 31
    return 0;
}

int divide() { // 32
    return 0;
}

int multiply() { // 33
    return 0;
}

// CONTROL OPERATION (minus HALT)
int branch() { // 40
    return 0;
}

int branchneg() { // 41
    return 0;
}

int branchzero() {
    return 0;
}

// MAIN FUNCTION -----------------------------------------------------------------------------------------
// Handles opening the file, inputting its contents into an array, and interpreting given instructions
int main() {
    string memory[99];
    int accumulator = 0;

    // Take in a user input and open the given file
    string userFile;
    ifstream file;

    cout << "Enter the name of your input file: ";
    cin >> userFile;

    file.open(userFile);
    if (!file.is_open())
    {
        cerr << "Error: Unable to open file!" << endl;
        return 1;
    }

    // Read the contents of the file into the memory array
    string line;
    int currentIndex = 0;
    while (getline(file, line)) {
        memory[currentIndex] = line;
        currentIndex += 1;
    }
    

    // For loop that will read all the contents of the memory index. Uncomment for debugging purposes!
    /*
    for (int i = 0; i < currentIndex; i++) {
        cout << memory[i] << endl;
    }
    */

    // Check for eof
    if (file.eof())
        cout << "File reading successful!" << endl;
    else
        cerr << "Error: File reading failed!" << endl;

    file.close();

    // Instruction reader
    int currentInstruction = 0;
    bool stop = false;
    while (!stop) {
        // Iterate over the array, reading in each instruction
        string instructionString = memory[currentInstruction].substr(1, 2); // Read the first two numbers, this is the instruction
        int instructionInt = stoi(instructionString);
        string addressString = memory[currentInstruction].substr(3, 2); // Read the last two numbers, this is the address
        int addressInt = stoi(addressString);

        // Check which instruction is read and execute the function
        switch (instructionInt) {
        case 10: // Read
            read(memory, addressInt);
            break;
        case 11: // Write
            write(memory, addressInt);
            break;
        case 20: // Load
            accumulator = load(memory, addressInt);
            break;
        case 21: // Store
            store(memory, addressInt, accumulator);
            break;
        case 30: // Add

            break;
        case 31: // Subtract

            break;
        case 32: // Divide

            break;
        case 33: // Multiply

            break;
        case 40: // Branch

            break;
        case 41: // Branch if Negative

            break;
        case 42: // Branch if Zero

            break;
        case 43: // Halt (No need for a seperatre function, just need to break the loop)
            cout << "Ending Program..." << endl;
            stop = true;
            break;
        }
        currentInstruction += 1;
    }

    return 0;
}