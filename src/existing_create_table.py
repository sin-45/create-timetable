import sys
import random
import csv
from pathlib import Path

csv_path = "other_file/"

def create_existing_table():
    csv_name = (csv_path + 
        input("CSVファイルの名前を入力してください (例: timetable): ")
        + ".csv")
    
    print(f"指定されたCSVファイル: {csv_name}")
    if Path(csv_name).is_file():
        with open(csv_name, "r", encoding="shift-jis") as f:
            reader = csv.reader(f)
            table = []
            for i in reader:
                table.append(list(i[0].split("\t")))
        return table
    else:
        print("指定されたCSVファイルが見つかりませんでした。")
        sys.exit(1)

if __name__ == "__main__":
    table = create_existing_table()
    # for i in table:
    #     print(*i, sep="\t")
