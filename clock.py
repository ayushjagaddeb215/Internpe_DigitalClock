from tkinter import *


from time import strftime

root = Tk()
root.title("Clock")

label = Label(root, font=("calibri", 80, "bold"), background="black", foreground="cyan", padx=20, pady=20)
label.pack(anchor='center')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)  # Update the time every second
    
time()  # Call the time function to start the clock
root.mainloop()  # Start the Tkinter event loop