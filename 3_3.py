# テキスト処理の基本
# アプリケーションの環境設定などをテキストファイルに保存する際や、
# テキストベースの入出力ファイルの読み込み・書き込みなどを行うアプリケーションに利用

# テキストファイルの作成
# フォルダの作成はmkdir
file = open("test.text", "w+")

# ファイルへの書き込み
file.write("OK?")

# ファイルを閉じる
file.close()

# ファイルへ追記したいとき
# "a+"で読み書き両用
file = open("test.text", "a+")


### with構文について ###
# with 処理 as 変数:で、処理の開始と終了で必要な処理を勝手にやってくれる
# close関数を使わなくても勝手にファイルを閉じてくれる
with open("test.txt", "a+") as file:
    file.write("OK?")

# ファイルの読み込み
# 書き込まれている文字を読み込む
# 第２引数は"r"、読み込み専用
with open("test.txt", "r") as file:
    v = file.read()

print(v)

