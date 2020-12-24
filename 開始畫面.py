import tkinter as tk
import tkinter.font as tkFont
from PIL import Image, ImageTk

window = tk.Tk()
window.title('breakoutclone')
window.geometry('800x600')
window.configure(background='white')

def closed():
    window.destroy()

load = Image.open("C:\\Users\\User\\Desktop\\python\\github\\頁面\\breakoutclone.png")  # 圖片
breakoutclone = ImageTk.PhotoImage(load)
img = tk.Label(window, image=breakoutclone)
img.image = breakoutclone
img.pack()

f1 = tkFont.Font(size = 20, family = "Courier New")  # 按鈕
start = tk.Button(window, text = "START", height = 1, width = 5, font = f1, command = closed)
start.pack()


window.mainloop()
