# 3.1 外部アプリケーションの操作

# サブプロセスのインポート
# subprosess: モジュール。関数をいくつかまとめて一つのファイルに記述したもの
# pythonに予め用意されてるモジュールで、他のアプリケーションを起動したり、
# 実行結果を取得する事ができる
import subprocess

# Webブラウザのパス
# ショートカットのパスをコピーしてもうまくいかない。実行ファイルのパスにする
# タスクマネージャーから実行ファイルのある場所に飛ぶ
ie = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
# ""直前のr: raw文字列という。pythonでバックスラッシュを改行と判断させないために文字と思わせる

# git-bash.exeのパス
git = r"C:\Program Files\Git\git-bash.exe"

# Hello.txtのパス
file = r"C:\Users\Hayate Tomiyama\OneDrive\デスクトップ\python\desktop_app\hello.txt"


#### Webブラウザでファイルを開く ###
# subprocess.run([ie, file])
# 開きたいアプリケーション、そのアプリで開きたいファイルの順にする
# subprocess.run(r"パス")と入力することも可能

### 複数のアプリケーションを順番に起動する ###
# subprocess.run(ie)
# subprocess.run(file)
# この場合、一個目のウインドウを閉じてから二個目が起動する感じになる。

### 複数のアプリケーションを同時に実行したい場合 ###
# Webブラウザアプリを起動
subprocess.Popen(ie)
# git-bashを起動
subprocess.Popen(git)
# Popen関数はテキストファイルとかだと上手くいかないので注意



