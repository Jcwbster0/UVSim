
class CPU:
    def __init__(self):
        self.programCounter = 0
        self.accumulator = 0
        self.memory = []

    def execute(self,controller, userInput=None):
        self.memory = controller.memory
       
        isUserInput = userInput is not None        
        #index self.memory to start at current programCounter
        while True:
            word = self.memory[self.programCounter]
            opcode = int(word[1:3])
            address = int(word[3:])
            print(f"{word}, {opcode}, {address}")
            branch = False

            match opcode:
                case 10: #read
                    if not isUserInput: 
                        controller.handleRead()
                        return "\nPlease enter input: "
                    self.read(controller, userInput, address)
                    #reset input to None so loop breaks out on subsequent read codes
                    isUserInput = False
                case 11: #write
                    print("write")
                    self.write(controller, address)
                case 20: #load
                    print("load")
                    print(self.accumulator)
                    self.load(address)
                    print(self.accumulator)
                case 21: #store
                    print("store")
                    self.store(address)
                case 30: #Add
                    print("add")
                    self.add(address)
                case 31: #subtract
                    self.subtract(address)
                case 32: #Divide
                    self.divide(address)
                case 33: #multiply
                    self.multiply(address)
                case 40: #branch
                    branch = self.branch()
                case 41: #branchneg
                    branch = self.branchNeg()
                case 42: #branchzero
                    branch = self.branchZero()
                case 43: #halt
                    print(self.memory)
                    self.programCounter = 0
                    return "end of program\n"

            if branch == True:
                self.programCounter = address
                branch = False
            else:
                self.programCounter += 1
        return

        #io functions, etc
    def read(self, controller, input, address):
        word = self.formatWord(input)
        self.memory[address] = word

    def write(self,controller, address):
        controller.handleWrite(self.memory[address])

    def store(self,address):
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
    
    def resetProgramCounter(self):
        self.programCounter = 0

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
