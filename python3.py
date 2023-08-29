# 题目：计算1~100总和

for x in range(10):  # 循环10次
    x = x + 10  # 每次循环中x + 10
    print('变量x的值=' + str(x))  # 输出x的值（'变量x的值='）

sum = 0
for i in range(1, 101):
    sum = sum + i
    print(sum)