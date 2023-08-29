import random

scissors = "电脑出的是剪刀"
rock = "电脑出的是石头"
paper = "电脑出的是布"
correct_guess = 0
total_guuss = 0
while True:
    my_choice = input("石头,剪刀,布!")

    if my_choice == "结束":
        break
    total_guuss = total_guuss + 1
    computer_choice = random.choice(["石头", "剪刀", "布"])
    if computer_choice == "剪刀":
        print(scissors)
    elif computer_choice == "石头":
        print(rock)
    else:
        print(paper)
    if my_choice == computer_choice:
        print("这局平局\n")
        continue
    win = False
    if my_choice == "剪刀":
        if computer_choice == "布":
            win = True
    elif my_choice == "石头":
        if computer_choice == "剪刀":
            win = True
    elif my_choice == "布":
        if computer_choice == "石头":
            win = True
    else:
        print("请输入其下一种选择：剪刀,石头,布,结束\n")
        continue
    if win:
        correct_guess = correct_guess + 1
        print("这局你赢了！\n")
    else:
        print("这局你输了！\n")
if total_guuss == 0:
    print("第一局不能结束！")
else:
    print("你猜对了{0}次！你的胜率是{1}%".format(correct_guess,
     correct_guess / total_guuss * 100.0))
