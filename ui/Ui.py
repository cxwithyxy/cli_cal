import tkinter
import pyperclip

class Ui():
    
    app: tkinter.Tk
    main_stage: tkinter.Toplevel
    clipboard_content: str

    def __init__(self):
        self.app = tkinter.Tk()
        self.app.bind_all("<Control-w>", self.close)
        self.app.bind_all("<Control-c>", self.copy_result)
        self.main_stage = tkinter.Toplevel(self.app)
        self.main_stage.attributes("-toolwindow", 1)
        self.main_stage.wm_attributes("-topmost", 1)
        self.main_stage.title("cli_cal v1.201907251616")
        self.main_stage.protocol("WM_DELETE_WINDOW", self.close)
        self.app.withdraw()
    
    def close(self, *argus):
        self.app.destroy()

    def set_clipboard_content(self, content: str):
        self.clipboard_content = content

    def copy_result(self, *argus):
        if(self.clipboard_content):
            pyperclip.copy(self.clipboard_content)


    def run(self):
        self.add_text("ctrl + w = 关闭窗口")
        self.add_text("ctrl + c = 复制结果")
        self.app.mainloop()

    def add_text(self, text: str):
        main_text = tkinter.Label(self.main_stage ,text = text, font=(48))
        main_text.pack()