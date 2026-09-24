
# OPERATION FUNCTIONS -----------------------------------------------------------------------------------------
# I/O OPERATION
def read(memoryList, address):
    while True:
        try:
            userInput = int(input("Please enter up to a 4 digit number: "))
            if -9999 <= userInput <= 9999:
                break
            print("Invalid input. Try again:")

        except ValueError:
            print("Invalid input. Try again:")

    if userInput >= 0:
        userString = f"+{userInput:04d}"
    else:
        userString = f"-{abs(userInput):04d}"

    memoryList[address] = userString

def write(memoryList, address):
    print(f"Content in address {address}: {memoryList[address]}")

def load(memoryList, address):
    return int(memoryList[address])

def store(memoryList, address, accumulator):
    if accumulator >= 0:
        userString = f"+{accumulator:04d}"
    else:
        userString = f"-{abs(accumulator):04d}"
    memoryList[address] = userString

# ARITHMETIC OPERATION
def truncate(accumulator):
    if accumulator > 9999 or accumulator < -9999:
        if accumulator < 0:
            return -(abs(accumulator) % 10000)
        else:
            return accumulator % 10000

    return accumulator


def add(accumulator, memoryList, targetAddress):
    memoryValue = load(memoryList, targetAddress)
    accumulator += memoryValue

    return truncate(accumulator)

def subtract(accumulator, memoryList, targetAddress):
    memoryValue = load(memoryList, targetAddress)
    accumulator -= memoryValue

    return truncate(accumulator)

def divide(accumulator, memoryList, targetAddress):
    memoryValue = load(memoryList, targetAddress)

    if memoryValue == 0:
        print("Error: Division by zero!")
        quit()

    accumulator = int(accumulator / memoryValue)

    return truncate(accumulator)

def multiply(accumulator, memoryList, targetAddress):
    memoryValue = load(memoryList, targetAddress)
    accumulator *= memoryValue

    return truncate(accumulator)

# CONTROL OPERATION (minus HALT)
def branch(targetAddress):
    return targetAddress

def branchneg(targetAddress, accumulator):
    if accumulator < 0:
        return targetAddress
    return None

def branchzero(targetAddress, accumulator):
    if accumulator == 0:
        return targetAddress
    return None



# MAIN FUNCTION -----------------------------------------------------------------------------------------
# Handles opening the file, inputting its contents into an array, and interpreting given instructions
def main():
    memory = []
    for x in range(100):
        memory.append("+0000")
    accumulator = 0

    # File reading block
    print("Enter the name of your input file: ")
    userFile = input()

    if not userFile.endswith(".txt"):
        print("Error: Incompatible file extension .txt file expected!")
        quit()

    containsHalt = False
    currentIndex = 0
    with open(userFile) as f:
        for x in f:
            # Error Handling
            if "\n" in x:
                x = x[:-1]
            if currentIndex >= 100:
                print("Error: File exceeds 100-word limit")
                quit()
            if (len(x) != 5 or ("-" not in x[0] and "+" not in x[0])):
                print("Error: Incompatible opcode: ", x, " on line ", currentIndex + 1)
                quit()
            if "+43" in x:
                containsHalt = True
            # Input current line into memory
            memory[currentIndex] = x
            currentIndex += 1
    if containsHalt == False:
        print("Error: opcode '43 (HALT)' is required to initialize program.")
        quit()

    # Instruction reading block
    currentInstruction = 0
    stop = False

    while ((not stop) and currentInstruction < 100):
        # Iterate over the array, reading in each instruction
        instruction = int(memory[currentInstruction][1:3])
        address = int(memory[currentInstruction][3:])

        branchSuccessful = False

        match instruction:
            case 10: # Read
                read(memory, address)
            case 11: # Write
                write(memory, address)
            case 20: # Load
                print(f"Loading {memory[address]} into the accumulator")
                accumulator = load(memory, address)
            case 21: # Store
                print(f"Storing {accumulator} in address {address}")
                store(memory, address, accumulator)
            case 30: # Add
                print(f"Adding {int(memory[address])} to {accumulator}")
                accumulator = add(accumulator, memory, address)
            case 31: # Subtract
                print(f"Subtracting {int(memory[address])} from {accumulator}")
                accumulator = subtract(accumulator, memory, address)
            case 32: # Divide
                print(f"Dividing {accumulator} by {int(memory[address])}")
                accumulator = divide(accumulator, memory, address)
            case 33: # Multiply
                print(f"Multiplying {int(memory[address])} by {accumulator}")
                accumulator = multiply(accumulator, memory, address)
            case 40:
                newAddress = branch(address)

                if newAddress is not None:
                    currentInstruction = newAddress
                    branchSuccessful = True
            case 41:
                newAddress = branchneg(address, accumulator)

                if newAddress is not None:
                    print("Negative Branch")
                    currentInstruction = newAddress
                    branchSuccessful = True
            case 42:
                newAddress = branchzero(address, accumulator)
                if newAddress is not None:
                    print("Zero Branch")
                    currentInstruction = newAddress
                    branchSuccessful = True
            case 43: # Halt
                print("HALT Command: Ending Program...")
                stop = True

        if not branchSuccessful:
            # Only increment on loops where a branching code was not executed
            currentInstruction += 1

    return 0


if __name__=="__main__":
    main()