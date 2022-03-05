import tkinter as tk

win=tk.Tk()

win.title("Rachel & Cynthia")

label= tk.Label(win,text="Hello world!")
count =0
def clickOK():
    global count
    count =count+1
    label.configure(text ="click OK " + str(count)+" ha ha")
label.pack()
button= tk.Button(win, text="OK",command=clickOK)
button.pack()

win.mainloop()

