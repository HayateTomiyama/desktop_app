# 2.3 ウインドウ上にボタンを配置

# coding: utf-8

import tkinter as tk

# ウインドウの作成
root = tk.Tk()
root.geometry("250x100")

# Runボタンを配置　ボタンなどの部品のことをウィジェットという。
run_bottun = tk.Button(root, text = "Run") # (ウインドウ名, ボタンのtext)
run_bottun.place(x = 110, y = 30)

# ウインドウ状態の維持
root.mainloop()
