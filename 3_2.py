# 3.2 ファイル操作の基本

# OS依存の機能を利用する場合は、osモジュールを利用する
# osのインポート
import os

# ファイルの移動をしたいときはshutilモジュールを使用
# シャティルと読む
#  shutilのインポート
import shutil 

# フォルダの作成
# ""に絶対パスor相対パスを入力
os.mkdir("newFolder")
# サブフォルダを作りたいときは
os.mkdir("newFolder/subFolder")
# mkdir関数では既にあるフォルダを作ることはできないので注意

# テキストファイルの作成
# ""内はファイル名ではなくパスであることに注意
# "w+"はテキストファイル内の内容をすべて消去し、新たな書き込みを行う
# ファイルが既に存在する場合は上書き、存在しない場合は新規作成
file = open("text.txt", "w+")

# ファイルを閉じる
file.close()

# ファイルの移動
# 名前ではなくパスを使う
shutil.move("text.txt", "newFolder")
# 上書きを許可する場合
# shutil.move("test.txt", "newFolder/test.txt")

# ファイルの削除
os.remove("newFolder/text.txt")
# ファイルの削除はos.removeでできるが、
# フォルダの削除はrmtree関数を使う
# フォルダの削除
shutil.rmtree("newFolder")
# これらで削除されたフォルダやファイルは、ゴミ箱に行くのはなく完全に削除される
