# 2.2 簡単なアプリケーション
# ウインドウ上の[Run]ボタンをクリックすると、プログラムで指定した動作を実行

# coding: utf-8　日本語が使える文字コードで保存

import tkinter as tk # GUIライブラリ。Pytonでは圧倒的人気を誇る。GUI：マウスや指で押せる画面のこと

 #ウインドウの作成「Tkクラスをインスタンス化」root(変数)でTkinterのウインドウを使えるように
root = tk.Tk()
# ウインドウのサイズ指定。geometryはメソッド（いくつかの処理をまとめたもの）
root.geometry("250x100")

#ウインドウ状態の維持
root.mainloop()