import sys

from src import random_create_table, existing_create_table, pdf_create

def main():
    while True:
        t = input("既存の時間割を使用しますか？ (y/n): ")
        if t == "y" or t == "n":
            break
    
    if t == "y":
        table = existing_create_table.create_existing_table()

    else:
        table = random_create_table.create_random_table()

    day = input("必要な曜日をスペース区切りで入力してください.何も打たないと月～金となります").split()
    if len(day) == 0:
        day = ["月", "火", "水", "木", "金"]

    new_day = [""] + day
    new_table = [new_day[:]]

    for i in range(len(table)):
        new_table.append([f"{i+1}コマ"] + table[i])

    for i in range(len(new_table)):
        for j in range(len(new_table[i])):
            if new_table[i][j] == None:
                new_table[i][j] = ""

    pdf_create.create_pdf(new_table, "timetable.pdf")

if __name__ == "__main__":
    main()
