#If you want to integrate this code with your previous code that uses the subprocess module, you can do so by combining them within a single script. Here's how you might integrate both code snippets:
import sys
import subprocess

if sys.version_info[0] == 2:
    from Tkinter import *
else:
    from tkinter import *

class Fullscreen_Window:
    def __init__(self):
        self.tk = Tk()
        self.tk.wm_state("zoomed")
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.state = False
        self.tk.bind("<F11>", self.toggle_fullscreen)
        self.tk.bind("<Escape>", self.end_fullscreen)

    def toggle_fullscreen(self, event=None):
        self.state = not self.state
        self.tk.attributes("-fullscreen", self.state)
        return "break"

    def end_fullscreen(self, event=None):
        self.state = False
        self.tk.attributes("-fullscreen", False)
        return "break"

if __name__ == "__main__":
    w = Fullscreen_Window()
    w.tk.mainloop()

    proc = subprocess.Popen(
        [
            "C:/Users/aivar/Desktop/plink.exe",
            "-ssh",
            #"-t",
            "-batch",
            "-pw",
            "pi-top",
            "pi@pi-top",
            "python3",
            "/home/pi/Desktop/prob.py",
        ],
        stdout=subprocess.PIPE,
        stdin=subprocess.PIPE,
        universal_newlines=True,
    )

    while True:
        c = proc.stdout.read(1)
        print(c, end="")
        if c == ":":
            print("ennekirj")
            proc.stdin.write("Aivar\n")
            proc.stdin.flush()
            print("pealekirj")