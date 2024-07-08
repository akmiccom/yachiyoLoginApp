@echo off 
echo このディレクトリに仮想環境を作成しますか？

pause


python -m venv .venv

rem アップグレード pip
python.exe -m pip install --upgrade pip --proxy http://10.103.1.2:8080

rem requirements.txt を参照したのインストール
pip install -r requirements.txt --proxy http://10.103.1.2:8080

rem 仮想環境の実行
.venv/Scripts/activate.ps1

