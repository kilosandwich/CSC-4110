from tkinter import *
from tkinter import ttk
from licenseFrame import LicenseConfirmFrame
from manageFrame import ManageFrame
from queryFrame import OperationFrame
from infoFrame import InfoFrame

class MainInterface:
    def __init__(self):
        self.root = Tk()
        self.root.title("ForestDB")
        self.root.geometry("800x500")

        self.tab_control = ttk.Notebook(self.root)
        self.license = LicenseConfirmFrame(self.root, self.packAfterAgree)
        self.license.pack()
        # self.tab_control.pack(expand=1, fill="both")

    def addTab(self, frame, label):
        self.tab_control.add(frame, text=label)

    def packAfterAgree(self):
        self.tab_control.pack(expand=1, fill="both")

    def mainloop(self):
        self.root.mainloop()

def main():
    interface = MainInterface()
    
    opFrame = OperationFrame(interface.root)
    
    interface.addTab(InfoFrame(interface.root).root, "info")
    interface.addTab(ManageFrame(interface.root, opFrame).root, "manage")
    interface.addTab(opFrame.root, "query")
    interface.mainloop()


if __name__ == "__main__":
    main()