from tkinter import *
from random import randint

root = Tk()
root.title('Strong Password Generator')
root.iconbitmap('')
root.geometry("600x400")


def new_rand():
    pw_entry.delete(0, END)
    pw_length = int(my_entry.get())

    my_password = ''

    for x in range(pw_length):
        my_password += chr(randint(33, 126))

    pw_entry.insert(0, my_password)


def clipper():
    root.clipboard_clear()
    root.clipboard_append(pw_entry.get())


# lable of Frame
lf = LabelFrame(root, text="How Many Characters?")
lf.pack(pady=20)

# Create Entry Box to design number of character
my_entry = Entry(lf, font=("Helvatica", 24))
my_entry.pack(pady=20, padx=20)

# Create Entry Box Our Returned Password
pw_entry = Entry(root, text='', font=("Helvetica", 24), bg="systembuttonface")
pw_entry.pack(pady=20)

# create a frame for our button
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create Our Buttons
my_button = Button(my_frame, text="Generate Strong Password", command=new_rand)
my_button.grid(row=0, column=0, padx=20)

clip_button = Button(my_frame, text="Copy to clipboard", command=clipper)
clip_button.grid(row=0, column=1, padx=10)

root.mainloop()
