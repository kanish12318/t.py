from tkinter import *
window=Tk()
window.title("tkinter sample window")
window.geometry("300x300")
greeting=Label(text="hello user",fg="orange",bg="gold")
button=Button(text="click me",fg="white",bg="black")
greeting.pack()
button.pack()
frame=Frame(master=window,relief=RAISED,borderwidth=9)

frame.pack()
label=Label(master=frame,text="sample frame")
label.pack()
Textbox=Text(fg="blue",bg="yellow")
Textbox.pack()
window.mainloop()

