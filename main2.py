import turtle


def on_click(x, y):
    turtle.bye()  # 关闭Turtle图形窗口


screen = turtle.Screen()
screen.onclick(on_click)  # 设置点击事件处理函数

turtle.done()  # 运行Turtle绘图循环
