class CPU:
    def __init__(self):
        self.programCounter = 0
        self.accumulator = 0
        self.memory = []
        self.totalCommands = 0

    def execute(self, controller, userInput=None):
        self.memory = controller.memory

        isUserInput = userInput is not None
        # index self.memory to start at current programCounter
        while True:
            if self.programCounter <= 99:
                word = self.memory[self.programCounter]
            else:
                word = "+4300"
                controller.pushToOutput(
                    "Program Counter Exceeds CPU Memory: forcing HALT", msgType="error"
                )
            opcode = int(word[1:3])
            address = int(word[3:])
            branch = False
            self.totalCommands += 1

            if self.totalCommands > 1000:
                controller.pushToOutput(
                    "Too many instructions processed (infinite branching?), forcing HALT\n",
                    msgType="error",
                )
                opcode = 43

            match opcode:
                case 10:  # read
                    if not isUserInput:
                        controller.pushToOutput(
                            "Opcode 10: Reading input", msgType="system"
                        )
                        controller.handleRead()
                        return "Please Enter Input in Field Above and Press Accept"
                    self.read(controller, userInput, address)
                    # reset input to None so loop breaks out on subsequent read codes
                    isUserInput = False
                case 11:  # write
                    controller.pushToOutput(
                        f"Opcode 11: Writing contents of address {address}",
                        msgType="system",
                    )
                    self.write(controller, address)
                case 20:  # load
                    controller.pushToOutput(
                        f"Opcode 20: Loading {self.memory[address]} into the accumulator\n",
                        msgType="system",
                    )
                    self.load(address)
                case 21:  # store
                    controller.pushToOutput(
                        f"Opcode 21: Storing {self.accumulator} in address {address}\n",
                        msgType="system",
                    )
                    self.store(address)
                case 30:  # Add
                    controller.pushToOutput(
                        f"Opcode 30: Adding {int(self.memory[address])} to {self.accumulator}\n",
                        msgType="system",
                    )
                    self.add(address)
                case 31:  # subtract
                    controller.pushToOutput(
                        f"Opcode 31: Subtracting {int(self.memory[address])} from {self.accumulator}\n",
                        msgType="system",
                    )
                    self.subtract(address)
                case 32:  # Divide
                    controller.pushToOutput(
                        f"Opcode 32: Dividing {self.accumulator} by {int(self.memory[address])}\n",
                        msgType="system",
                    )
                    if int(self.memory[address]) == 0:
                        controller.pushToOutput(
                            "Error: Division by 0, Program Terminated", msgType="error"
                        )
                        return
                    self.divide(address)
                case 33:  # multiply
                    controller.pushToOutput(
                        f"Opcode 33: Multiplying {int(self.memory[address])} by {self.accumulator}\n",
                        msgType="system",
                    )
                    self.multiply(address)
                case 40:  # branch
                    controller.pushToOutput(f"Opcode 40: Branch", msgType="system")
                    branch = self.branch()
                    controller.pushToOutput(
                        f"Branching to address {address}\n", msgType="system"
                    )
                case 41:  # branchneg
                    controller.pushToOutput(
                        "Opcode 41: Branch if accumulator is negative", msgType="system"
                    )
                    branch = self.branchNeg()
                    if branch == True:
                        controller.pushToOutput(
                            f"Accumulator is negative: Branching to address {address}\n",
                            msgType="system",
                        )
                    else:
                        controller.pushToOutput(
                            "Accumulator is not negative\n", msgType="system"
                        )
                case 42:  # branchzero
                    controller.pushToOutput(
                        "Opcode 42: Branch if accumulator is zero", msgType="system"
                    )
                    branch = self.branchZero()
                    if branch == True:
                        controller.pushToOutput(
                            f"Accumulator is zero: Branching to address {address}\n",
                            msgType="system",
                        )
                    else:
                        controller.pushToOutput(
                            "Accumulator is not zero\n", msgType="system"
                        )
                case 43:  # halt
                    self.programCounter = 0
                    self.totalCommands = 0
                    return "\n--------------\nend of program\n--------------\n"

            if branch == True:
                self.programCounter = address
                branch = False
            else:
                self.programCounter += 1
        return

        # io functions, etc

    def read(self, controller, input, address):
        word = self.formatWord(input)
        self.memory[address] = word

    def write(self, controller, address):
        controller.handleWrite(f"Address {address}: {self.memory[address]}")
        controller.pushToOutput("\n")

    def store(self, address):
        word = self.formatWord(self.accumulator)
        self.memory[address] = word

    def load(self, address):
        self.accumulator = int(self.memory[address])

    def branch(self):
        return True

    def branchNeg(self):
        if self.accumulator < 0:
            return True

    def branchZero(self):
        if self.accumulator == 0:
            return True

    def add(self, address):
        value = int(self.memory[address])
        self.accumulator += value
        self.accumTruncate()

    def subtract(self, address):
        value = int(self.memory[address])
        self.accumulator -= value
        self.accumTruncate()

    def multiply(self, address):
        value = int(self.memory[address])
        self.accumulator *= value
        self.accumTruncate()

    def divide(self, address):
        value = int(self.memory[address])
        self.accumulator /= value
        self.accumTruncate()

    def accumTruncate(self):
        if self.accumulator < -9999 or self.accumulator > 9999:
            isNegative = self.accumulator < 0
            self.accumulator = self.accumulator % 10000
            if isNegative == True:
                self.accumulator * -1

    def reset(self):
        self.programCounter = 0
        self.memory = []
        self.accumulator = 0

    def formatWord(self, input):
        isPositive = int(input) >= 0
        word = str(abs(int(input)))
        if isPositive:
            word = "+" + word
        else:
            word = "-" + word
        match len(word):
            case 2:
                word = word[:1] + "000" + word[1:]
            case 3:
                word = word[:1] + "00" + word[1:]
            case 4:
                word = word[:1] + "0" + word[1:]
        return word
