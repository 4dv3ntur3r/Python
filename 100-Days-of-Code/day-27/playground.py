from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

# Label

my_lable = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_lable.grid(column=0, row=0)  # this is used to show the above lable in the GUI

# Can change the values as shown below

my_lable["text"] = "New Text"
my_lable.config(text="New Text")
my_lable.config(padx=10, pady=10)


# Button

def button_clicked():
    print("I got clicked")
    # my_lable["text"] = "I got clicked!"
    my_lable["text"] = input.get()

button2 = Button(text="New Button")
button2.grid(column=3, row=0)

button1 = Button(text="Click Me", command=button_clicked)
button1.grid(column=2, row=1)



# Entry

input = Entry(width=10)
input.grid(column=4, row=2)

window.mainloop()