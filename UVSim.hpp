#pragma once
#include <string>

// VALIDATION FUNCTIONS --------------------------------------------------------
bool is_txt_file(const std::string& filename);

// OPERATION FUNCTIONS ---------------------------------------------------------
// I/O OPERATION
void read(std::string memoryList[], int address);
void write(std::string memoryList[], int address);

// LOAD/STORE OPERATION
int load(std::string memoryList[], int address);
void store(std::string memoryList[], int address, int accumulator);

// ARITHMETIC OPERATION
int add(int &accumulator, std::string memoryList[], int targetAddress);
int subtract(int &accumulator, std::string memoryList[], int targetAddress);
int divide(int &accumulator, std::string memoryList[], int targetAddress);
int multiply(int &accumulator, std::string memoryList[], int targetAddress);

// CONTROL OPERATION (minus HALT)
bool branch(int& currAddress, int targetAddress);
bool branchneg(int& currAddress, int targetAddress, int accumulator);
bool branchzero(int& currAddress, int targetAddress, int accumulator);
