import sys
import random


def yn_input(input_str):
    while True:
        temp = input(input_str + " (y/n): ")
        if temp == "y" or temp == "n":    
            return temp
        else:
            print("yかnを入力してください。")

def create_random_table():
    num_days = int(input("日数を入力してください: "))
    num_lecs = int(input("一日のコマ数を入力してください: "))
    space = yn_input("空きコマを作成しますか？")
    learning_sub = input("学習科目を入力してください (スペース区切り): ").split()
    random_sub_cnt = yn_input("コマ数を各授業ごとに決めますか？")
    
    learning_sub_dict = dict()
    if random_sub_cnt == "n":
        sub_cnt = int(input("授業のコマ数を入力してください: "))
        if sub_cnt * len(learning_sub) > num_days * num_lecs:
            print("科目数が時間割のコマ数を超えています。")
            sys.exit(1)
        total_sub_cnt = sub_cnt * len(learning_sub)
        for sub in learning_sub:
            learning_sub_dict[sub] = sub_cnt
    else:
        total_sub_cnt = 0
        for sub in learning_sub:
            sub_cnt = int(input(f"{sub}のコマ数を入力してください: "))
            learning_sub_dict[sub] = sub_cnt
            total_sub_cnt += sub_cnt
        if total_sub_cnt > num_days * num_lecs:
            print("科目数が時間割のコマ数を超えています。")
            sys.exit(1)
    
    table = [[None for _ in range(num_days)] for _ in range(num_lecs)]
    table_list = [None] * (num_days * num_lecs - total_sub_cnt)
    for sub in learning_sub_dict:
        for _ in range(learning_sub_dict[sub]):
            table_list.append(sub)
    
    random.seed(0) # 追跡可能
    random.shuffle(table_list)
    random.shuffle(table_list)

        
    for i in range(num_days):
        idx = 0
        for j in range(num_lecs):
            if space == "n" and table_list[i*num_lecs + j] is None:
                pass
            else:
                table[idx][i] = table_list[i*num_lecs + j]
                idx += 1
    
    return table