import tkinter
import gui


class MainWindow(tkinter.Tk):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupGui()

    def setupGui(self):
        self.title('Tk/Ttk Designer')
        self.iconbitmap('logo.png')
        self.geometry(f"{self.winfo_screenwidth() - 200}x{self.winfo_screenheight() - 200}")
        gui.make_gui(self)
        self.mainloop()


if __name__ == '__main__':
    win = MainWindow()
