import pyshorteners
from tkinter import *
from PIL import ImageTk, Image

win = Tk()
win.geometry("500x400")
win.title("URL Shortener")
win.configure(bg="#252525")

def shorten_url():
    url = entry1.get()
    short_url = pyshorteners.Shortener().tinyurl.short(url)
    entry2.delete(0, END)
    entry2.insert(END, short_url)

# Background Images
bg_image = ImageTk.PhotoImage(Image.open("bg1.jpg"))
bg_label = Label(win, image=bg_image)
bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# Labels and Entries
Label(win, text="Enter the URL you want to shorten:", font=("Arial", 16), bg="#252525", fg="#ffffff").place(x=50, y=80)
entry1 = Entry(win, font=("Arial", 12), bd=3, width=40)
entry1.place(x=50, y=120)

Button(win, text="Shorten URL", font=("Arial", 12), bg="#f44336", fg="#ffffff", width=15, command=shorten_url).place(x=180, y=170)

Label(win, text="Shortened URL:", font=("Arial", 16), bg="#252525", fg="#ffffff").place(x=50, y=230)
entry2 = Entry(win, font=("Arial", 12), bg="#ffffff", width=40, bd=3)
entry2.place(x=50, y=270)

win.mainloop()