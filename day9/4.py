from tkinter import *

root = Tk()
root.title("이미지 업로드하기")
img1 = PhotoImage(file="img2.png")
canvas = Canvas(root, height=680, width=680, bg="ivory")
canvas.pack()
canvas.create_image(340, 340, image=img1)
canvas.create_text(340, 400, text="너무 졸려요", font=("나눔바른펜", 30, "bold"), fill="white")
root.mainloop()
