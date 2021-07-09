from os import makedirs
import tkinter as tk
from tkinter import image_names, ttk
#ttk.Button(master=root, image=)

#class ImageButton (ttk.Button):
#    def __init__ (master):
#        img = tk.PhotoImage(file="./ButtonImage_test.png")
#        super.__init__(master=master, image=img)
# rootメインウィンドウの設定
root = tk.Tk()
root.title("application")
root.geometry("250x150")

# メインフレームの作成と設置
frame = tk.Frame(root)
frame.pack(fill = tk.BOTH, padx=20,pady=10)

# 画像ファイルをインスタンス変数に代入
img = tk.PhotoImage(file="./ButtonImage_test.png")

# 画像のリサイズ
small_img = img.subsample(2, 1)
big_img = img.zoom(2, 2)

# 各種ウィジェットの作成
button = tk.Button(frame, text="画像", image=img, compound="top")
button_small = ttk.Button(frame, text="小画像", image=small_img, compound="top")
button_big = tk.Button(frame, text="大画像", image=big_img, compound="top")

# 各種ウィジェットの設置
button.grid(row=0, column=0, padx=5)
button_small.grid(row=0, column=1, padx=5)
button_big.grid(row=0, column=2, padx=5)

root.mainloop()