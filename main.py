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

if __name__ == "__main__":
    main()