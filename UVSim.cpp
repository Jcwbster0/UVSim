#include <iostream>
#include <fstream>
#include <string>
using namespace std;

//VALIDATION FUNCTIONS -----------------------------------------------------------------------------------------
bool is_txt_file(const string& filename) {
    if (filename.length() < 4) return false;
    string ending = filename.substr(filename.length() - 4);
    return ending == ".txt";
}

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
int add(int &accumulator, string memoryList[], int targetAddress) {// 30
    int memoryValue = load(memoryList, targetAddress);
    accumulator += memoryValue;
    return 0;
}

int subtract(int &accumulator, string memoryList[],int targetAddress) { // 31
    int memoryValue = load(memoryList, targetAddress);
    accumulator -= memoryValue;
    return 0;
}

int divide(int &accumulator, string memoryList[], int targetAddress) { // 32
    int memoryValue = load(memoryList, targetAddress);
    accumulator /= memoryValue;
    return 0;
}

int multiply(int &accumulator, string memoryList[], int targetAddress) { // 33
    int memoryValue = load(memoryList, targetAddress);
    accumulator *= memoryValue;
    return 0;
}

// CONTROL OPERATION (minus HALT)
bool branch(int& currAddress, int targetAddress) { // 40
    currAddress = targetAddress;
    return true;
}

bool branchneg(int& currAddress, int targetAddress, int accumulator) { // 41
    if (accumulator < 0) {
        currAddress = targetAddress;
        return true;
    }
    return false;
}

bool branchzero(int& currAddress, int targetAddress, int accumulator) { // 42
    if (accumulator == 0) { 
        currAddress = targetAddress;
        return true;
    }
    return false;
}

// MAIN FUNCTION -----------------------------------------------------------------------------------------
// Handles opening the file, inputting its contents into an array, and interpreting given instructions
int main() {
    string memory[100];
    for (int i =0; i < 100; i++) {
        memory[i] = "+0000";
    }
    int accumulator = 0;

    // Take in a user input and open the given file
    string userFile;
    ifstream file;

    cout << "Enter the name of your input file: ";
    cin >> userFile;

    file.open(userFile);
    if (!file.is_open()) {
        cerr << "Error: Unable to open file!" << endl;
        return 1;
    } 
    else if (!is_txt_file(userFile)) {
        cerr << "Error: Incompatible file extension .txt file expected!" << endl;
        return 1;
    }


    // Read the contents of the file into the memory array
    string line;
    bool containsHalt = false;
    int currentIndex = 0;
    while (getline(file, line)) {
        //Error handling block: program will not accept opcodes that contain characters other than integers or opcodes greater or less than length 5 ie "+4321" or "-1234. Also checks for maximum memory bounds and ensures the program contains HALT command." 
        if (line.empty()) {
            continue;
        }
        //this conditional check strips the carriage return operator for windows compiling on mac or linux
        if (line.back() == '\r') {
            line.pop_back();
        }
        if (currentIndex >= 100) {
            cerr << "Error: Input file exceeds 100-word memory limit." << endl;
            return 1;
        }
        try {
            int testValue = stoi(line);
            if ((line.length() != 5) || (line[0] != '-' && line[0] != '+')) {
                throw runtime_error("Error: Incompatible opcode: '" + line + "' on line " + to_string(currentIndex + 1));
            }
        }
        catch (const exception& e) {
            cerr << e.what() << endl;
            return 1;
        }
        if (line.substr(0,1) == "+" && line.substr(1,2) == "43") {
            containsHalt = true;
        }
        //initialize memory and increment after validation occurs 
        memory[currentIndex] = line;
        currentIndex += 1;
    }
   if (containsHalt == false) {
       cerr << "Error: opcode '43 (HALT)' is required to initialize program." << endl;
       return 1;
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
    else {
        cerr << "Error: File reading failed!" << endl;
        return 1;
    }
    file.close();

    // Instruction reader
    int currentInstruction = 0;
    bool stop = false;

    bool branchSuccessful;
    
    while (!stop && currentInstruction < 100) {
        // Iterate over the array, reading in each instruction
        string instructionString = memory[currentInstruction].substr(1, 2); // Read the first two numbers, this is the instruction
        int instructionInt = stoi(instructionString);
        string addressString = memory[currentInstruction].substr(3, 2); // Read the last two numbers, this is the address
        int addressInt = stoi(addressString);

        branchSuccessful = false;

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
            add(accumulator, memory, addressInt);
            break;
        case 31: // Subtract
            subtract(accumulator, memory, addressInt);
            break;
        case 32: // Divide
            divide(accumulator, memory, addressInt);
            break;
        case 33: // Multiply
            multiply(accumulator, memory, addressInt);
            break;
        case 40: // Branch
            branchSuccessful = branch(currentInstruction, addressInt);
            break;
        case 41: // Branch if Negative
            branchSuccessful = branchneg(currentInstruction, addressInt, accumulator);
            break;
        case 42: // Branch if Zero
            branchSuccessful = branchzero(currentInstruction, addressInt, accumulator);
            break;
        case 43: // Halt (No need for a separator function, just need to break the loop)
            cout << "Ending Program..." << endl;
            stop = true;
            break;
        }
        if (!branchSuccessful) {
            //Only increment on loops where a branching code was not executed
            currentInstruction += 1;
        }
    }

    return 0;
}
