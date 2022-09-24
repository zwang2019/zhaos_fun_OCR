from tkinter import *
import time

TRANSCOLOUR = 'gray'

def on_resize(evt):
    root.configure(width=evt.width,height=evt.height)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
    print(canvas.winfo_width())


root = Tk()

# Can not change the window size and window on top
root.resizable(0, 0)
root.wm_attributes('-topmost',1)

# transparent
root.wm_attributes('-transparentcolor', TRANSCOLOUR)

# window size and title
root.geometry('388x33+500+500')
root.title('Scan CARD No. Here:')

# canvas?
canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=Y)

canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
root.bind('<Configure>', on_resize)

# here is looping, so...
root.mainloop()
