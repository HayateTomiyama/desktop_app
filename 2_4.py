# 2.4 ボタンに機能を付与

# coding: utf-8

### 関数 ###
def run_func():
    print("Hello!") # もともとあるprint関数などは組み込み関数という
    print("World!")

### GUI ###
import tkinter as tk

root = tk.Tk()
root.geometry("250x100")

# Runボタン
run_button = tk.Button(root, text = "Run", command = run_func) # ボタンを押すと関数を実行
run_button.place(x = 110, y = 30)

# ウインドウ状態の維持
root.mainloop()