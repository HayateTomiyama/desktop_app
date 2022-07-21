# 3.5 例外処理について
# 3.4はちゃんとわかってる内容だったので無視

# osのインポート
import os

# フォルダの作成
# os.mkdir("newFloder")
# しようと思ったけど、もしかしたらこのフォルダは既にあるかもしれない・・・？
# そんな時に、try-exept構文を使う
# 例外が発生することを想定しているときに使う

try:
    os.mkdir("newFloder")
except:
    print("Error!")


### if文を使いたかったら ###
if os.path.exists("newFolder"):
    print("already exists")
else:
    os.mkdir("newFolder")

### 特定の例外を指定 ###
try:
    os.mkdir("newFolder")
except(FileExistsError):
    print("already exists")

