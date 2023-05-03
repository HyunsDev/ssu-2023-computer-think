from tkinter import *

root = Tk()
root.geometry("300x200")
root.title("cm/inch 변환")
root.config(padx=30, pady=10)

label_title = Label(root, text="변환할 길이를 입력하세요.", font=("나눔고딕", 20, "bold"))
label_title.grid(column=0, row=0, columnspan=2, padx=10, pady=10)

entry_input = Entry(root, width=15)
entry_input.focus()
entry_input.grid(column=0, row=1, sticky=E)

label_input = Label(root, text="cm", font=("나눔고딕", 10, "bold"))
label_input.grid(column=1, row=1, sticky=W)

l_result = Label(root, text="inch", font=("나눔고딕", 10, "bold"))
l_result.grid(column=0, row=3, columnspan=2)


def cm_to_inch():
    cm = float(entry_input.get())
    inch = cm * 0.393701
    l_result.config(text=f"{cm}cm = {inch:.2f} inch")
    entry_input.delete(0, END)


button = Button(root, text="변환", command=cm_to_inch)
button.grid(column=0, row=2, columnspan=2, pady=10)


root.mainloop()
