
■ JSONで暗記アプリ

作成日: 2026年1月25日 
バージョン: 0.1


■ 説明

JSONを読み込み、問題と解答と画像の表示ができる暗記アプリ。

CSVとは異なり、改行の読み込みなどもできる。

後々機能追加予定。


■ 使い方

1: エクセルファイルを作る

1行目に question, image_url , answer この3つの列を含んだ行を作る。
2行目以降に質問、画像URL、解答 を書く。改行OK

2: excel2json.py でJSONに変換をする。

必要なライブラリはrequirements.txt でインストールしておく。

3: index.html でJSONを読み込みする。

Pythonで生成されたJSONをindex.htmlで読み込みする。

