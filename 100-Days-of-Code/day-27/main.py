from tkinter import *

window = Tk()

window.title("My first GUI program")
window.minsize(width=500, height=300)

# Label

my_lable = Label(text="I am a Label", font=("Arial", 24, "bold"))
my_lable.pack()  # this is used to show the above lable in the GUI

# Can change the values as shown below

my_lable["text"] = "New Text"
my_lable.config(text="New Text")


# Button

def button_clicked():
    print("I got clicked")
    # my_lable["text"] = "I got clicked!"
    my_lable["text"] = input.get()


button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

input = Entry(width=10)
input.pack()

# Text
text = Text(height=5, width=30)
# Puts cursor in textbox.
text.focus()
# Adds some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get's current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# Spinbox
def spinbox_used():
    # gets the current value in spinbox.
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# Checkbutton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# Radiobutton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()

# place
# Place positions the item in the exact location which it is given
my_lable_2 = Label(text="Place label")
my_lable_2.place(x=0, y=0)

#grid
#This imagines the entire screen is a grid
#Grid and pack cant be in the same program have to choose one, preferred one is grid
# my_lable_3 = Label(text="grid label")
# my_lable_3.grid(colomn=0, row=o)

window.mainloop()
