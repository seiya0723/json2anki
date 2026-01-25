import pandas as pd
import json

def excel_to_json(input_file, output_file):
    # 1. Excelファイルを読み込む
    # engine='openpyxl' を指定することで .xlsx に対応
    df = pd.read_excel(input_file, engine='openpyxl')

    # 2. DataFrameを辞書のリスト形式に変換
    # to_dict('records') を使うと [ {"列名": 値}, {"列名": 値}, ... ] の形になる
    data_list = df.to_dict(orient='records')

    # 3. JSONファイルとして保存
    with open(output_file, 'w', encoding='utf-8') as f:
        # ensure_ascii=False で日本語が化けるのを防ぐ
        # indent=4 で読みやすい形式にする
        json.dump(data_list, f, ensure_ascii=False, indent=4)

    print(f"変換完了: {output_file}")

# 実行
excel_to_json('test.xlsx', 'quiz_data.json')
