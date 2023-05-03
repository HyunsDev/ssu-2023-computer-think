from tkinter import *

root = Tk()
root.title("cm/inch 변환")
root.config(padx=30, pady=10)

img1 = PhotoImage(file="img1.png")
img2 = PhotoImage(file="img2.png")

label_img = Label(root, image=img1)
label_img.pack()

button_img = Button(root, image=img2)
button_img.pack()


root.mainloop()
