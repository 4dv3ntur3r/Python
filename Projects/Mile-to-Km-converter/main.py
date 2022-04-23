from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
window.minsize(width=300, height=100)
window.config(padx=30, pady=30)

input_miles = Entry()
input_miles.grid(column=1, row=0)
input_miles.config(width=15)


def convert_to_km():
    km = float(input_miles.get()) * 1.609
    label_converted.config(text=f"{round(km)}")


label_miles = Label(text="Miles", font=("Ariel", 10))
label_miles.grid(column=2, row=0)
label_miles.config(padx=10)

label_to = Label(text="is equal to", font=("Ariel", 10))
label_to.grid(column=0, row=1)
label_to.config(padx=10)

label_converted = Label(text="0", font=("Ariel", 10))
label_converted.grid(column=1, row=1)
label_converted.config(padx=10)

label_km = Label(text="Km", font=("Ariel", 10))
label_km.grid(column=2, row=1)
label_km.config(padx=10)

button = Button(text="Convert", command=convert_to_km)
button.grid(column=1, row=2)

window.mainloop()
