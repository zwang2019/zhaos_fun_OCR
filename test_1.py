from tkinter import *

TRANSCOLOUR = 'gray'

def on_resize(evt):
    tk.configure(width=evt.width,height=evt.height)
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
    print(canvas.winfo_width())


tk = Tk()

# Can not change the window size and window on top
tk.resizable(0, 0)
tk.wm_attributes('-topmost',1)

# transparent
tk.wm_attributes('-transparentcolor', TRANSCOLOUR)

# window size and title
tk.geometry('388x33+500+500')
tk.title('Scan CARD No. Here:')

# canvas?
canvas = Canvas(tk)
canvas.pack(fill=BOTH, expand=Y)

canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=TRANSCOLOUR, outline=TRANSCOLOUR)
tk.bind('<Configure>', on_resize)

tk.mainloop()
