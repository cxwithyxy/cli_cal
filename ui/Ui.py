import tkinter

class Ui():
    
    app: tkinter.Tk
    main_stage: tkinter.Toplevel

    def __init__(self):
        self.app = tkinter.Tk()
        self.app.bind_all("<Control-w>", self.close)
        self.main_stage = tkinter.Toplevel(self.app)
        self.main_stage.attributes("-toolwindow", 1)
        self.main_stage.wm_attributes("-topmost", 1)
        self.app.withdraw()
    
    def close(self, *argus):
        self.app.destroy()

    def run(self):
        self.app.mainloop()

    def add_text(self, text: str):
        main_text = tkinter.Label(self.main_stage ,text = text)
        main_text.pack()