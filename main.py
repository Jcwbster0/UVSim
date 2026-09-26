import MainWindow 
import CPU
import CPUController
import FileManager

def main():
    cpu = CPU.CPU()
    fileManager = FileManager.FileManager()
    controller = CPUController.CPUController(cpu, fileManager)

    window = MainWindow.MainWindow("Hello World", (600,600), controller)

if __name__ == "__main__":
    main()
    
