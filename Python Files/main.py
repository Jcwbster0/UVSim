import MainWindow 
import CPU
import CPUController
import FileManager
import ColorController

def main():
    cpu = CPU.CPU()
    colorConfig = ColorController.ColorController()
    fileManager = FileManager.FileManager()
    controller = CPUController.CPUController(cpu, fileManager)

    window = MainWindow.MainWindow("UVSim", (1000,600), controller, colorConfig)

if __name__ == "__main__":
    main()
    
