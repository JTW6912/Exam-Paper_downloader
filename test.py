import tkinter as tk

window = tk.Tk()
ListContent = tk.StringVar()
ListContent.set(['chinese','utuber'])
Lb = tk.Listbox(window,listvariable=ListContent)
Lb.pack()

window.mainloop()