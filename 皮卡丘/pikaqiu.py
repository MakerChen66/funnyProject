#!/usr/bin/env python
# coding:utf-8
"""
@author: makerchen
@微信公众号： 小鸿星空科技
"""


from turtle import *
import turtle as t
from random import *


def infoPrt():
    print('coordinate: ' + str(t.pos()))
    print('angle: ' + str(t.heading()))

t.pensize(3)
t.hideturtle()
t.colormode(255)
t.color("black")
t.setup(700, 650)
t.speed(1)
t.st()
t.pu()
t.goto(-210,86)
t.pd()
infoPrt()

# 头
print('头')
t.seth(85)
t.circle(-100,50)
infoPrt()
t.seth(25)
t.circle(-170,50)
infoPrt()

# 右耳
print('右耳')
t.seth(40)
t.circle(-250,30)
infoPrt()

# 右耳尖
t.begin_fill()

# 左
t.circle(-250,22)

# 右
t.seth(227)
t.circle(-270, 15)
prePos = t.pos()
infoPrt()

# 下
t.seth(105)
t.circle(100, 32)
t.end_fill()
t.pu()
t.setpos(prePos)
t.pd()
t.seth(212)
t.circle(-270, 28)
prePos = t.pos()
t.pu()
t.goto(t.xcor()+5,t.ycor()-2)
t.pd()

# 躯干
print('躯干')
t.seth(280)
t.circle(500, 30)
infoPrt()

# 臀部
print('臀部')
t.seth(120)
t.circle(150, -11)
p_tail=t.pos()
t.circle(150, -44)
p_butt=t.pos()
infoPrt()

# 尾巴
t.pu()
t.setpos(p_tail)
t.pd()
t.begin_fill()
t.seth(50)
t.fd(25)
t.seth(-50)
t.fd(30)
p_tail1=t.pos
t.seth(-140)
t.fd(36)
t.end_fill()
t.seth(39)

# 右尾和h1
t.fd(72)

# 右尾和v1
t.seth(125)
t.fd(48)

# 右尾和h2
t.seth(40)
t.fd(53)

# 右尾和v2
t.seth(88)
t.fd(45)

# 右尾和h3
t.seth(35)
t.fd(105)

# 右尾和v3
t.seth(105)
t.circle(850, 8)
t.seth(215)
t.circle(850, 11)
t.seth(280)
t.fd(110)
t.seth(220)
t.fd(50)
t.seth(309)
t.fd(56)

# 底盘
print('底盘')
t.pu()
t.setpos(p_butt)
t.pd()
t.seth(20)
t.circle(120, -45)
infoPrt()

t.seth(330)
t.circle(-150, -30)
infoPrt()
prePos = t.pos()
t.pu()
t.goto(t.xcor()+20,t.ycor())
t.pd()
t.seth(230)
t.circle(-70, 120)
p_bot=t.pos()

# 两脚-right
t.pu()
t.setpos(p_butt)
t.setpos(t.xcor()+5,t.ycor()+5)
t.pd()
t.seth(-86)
t.fd(30)
t.seth(-93)
t.fd(33)
t.seth(-225)
t.circle(-150, 22)

# 两脚-left
t.pu()
t.setpos(p_bot)
t.setpos(t.xcor()+85,t.ycor()-43)
t.pd()
t.seth(-105)
t.fd(50)
t.seth(-225)
t.circle(-150, 22)

# 左躯干
print('躯干')
t.pu()
t.setpos(p_bot)
t.pd()
t.seth(90)
t.circle(450, 13)
p_lfhd = t.pos()
t.circle(450, 5)
t.pu()
t.circle(450, 5)
t.pd()
t.circle(450, 6)
infoPrt()

# 左脸
t.begin_fill()
t.fillcolor("pink")
print('左脸')
t.seth(330)
t.circle(50, -90)
infoPrt()

# 左酒窝
t.seth(30)
t.circle(-15, 120)
t.seth(-70)
t.circle(-30, 90)
t.end_fill()

# 左手
t.pu()
t.setpos(p_lfhd)
t.pd()
t.seth(160)
t.circle(150, 30)
infoPrt()
t.seth(180)
t.circle(-30, 150)
t.fd(67)
t.pu()
t.setpos(t.xcor()-40,t.ycor()-60)
t.pd()
t.seth(200)
t.circle(-5, 180)

# 右手
t.pu()
t.setpos(p_lfhd)
t.setpos(t.xcor()+180,t.ycor()+5)
t.pd()
t.seth(200)
t.circle(-50, 100)
t.pu()
t.circle(-50, 15)
t.pd()
t.circle(-50, 65)
t.pu()
t.setpos(t.xcor()+10,t.ycor()-45)
t.pd()
t.seth(80)
t.fd(10)
t.seth(165)
t.circle(10, 60)
t.seth(90)
t.fd(5)
t.seth(165)
t.circle(10, 60)
t.seth(95)
t.fd(5)
t.seth(185)
t.circle(10, 60)
t.seth(105)
t.fd(10)
t.seth(230)
t.fd(20)
t.seth(145)
t.fd(10)
t.seth(285)
t.fd(20)

# 右酒窝
t.begin_fill()
t.fillcolor("pink")
t.pu()
t.setpos(t.xcor()-40,t.ycor()+110)
t.pd()
t.circle(27, 360)
t.end_fill()

"""画嘴"""
color("black", "#F35590")

# 下嘴弧度并填充颜色
penup()
goto(-100, 72)
pendown()
begin_fill()
setheading(260)
forward(60)
circle(-11, 150)
forward(55)
print(position())
penup()
goto(-128.46, 71.97)
pendown()
end_fill()

#嘴中最上方的阴影部分
color("#6A070D", "#6A070D")
begin_fill()
penup()
goto(-99.00, 72.00)
pendown()
penup()
goto(-104.29, 48.3)
pendown()
penup()
goto(-142, 45)
pendown()
penup()
goto(-150.40, 62.74)
pendown()
penup()
goto(-128.46, 71.97)
pendown()
penup()
goto(-99.00, 72.00)
pendown()
end_fill()

#上嘴唇
color("black","#FFD624")
penup()
goto(-168, 65)
pendown()
begin_fill()
setheading(-25)
for i in range(2):
    setheading(-25)
    circle(35, 70)
end_fill()

#嘴中第二个阴影部分
color("#AB1945", "#AB1945")
penup()
goto(-142, 45)
pendown()
begin_fill()
setheading(40)
circle(-33, 70)
goto(-104,48.3)
penup()
goto(-108,33)
pendown()
setheading(155)
circle(25, 70)
end_fill()

# 左眼
t.pu()
t.color("black")
t.setpos(t.xcor()-40,t.ycor()+90)
t.pd()
t.circle(5)
t.pu()
t.setpos(t.xcor()+5,t.ycor()+10)
t.pd()
t.begin_fill()
t.seth(190)
t.circle(15, 130)
t.seth(310)
t.circle(10, 15)
t.seth(0)
t.circle(17, 133)
t.seth(90)
t.circle(10, 15)
t.end_fill()
t.pu()
t.setpos(t.xcor()+2,t.ycor()-15)
t.pd()
t.color("white")
t.begin_fill()
t.circle(5)
t.end_fill()

# 右眼
t.pu()
t.setpos(t.xcor()+85,t.ycor()+15)
t.pd()
t.color("black")
t.circle(5)
t.pu()
t.setpos(t.xcor()+5,t.ycor()+10)
t.pd()
t.begin_fill()
t.seth(190)
t.circle(20, 130)
t.seth(310)
t.circle(10, 15)
t.seth(0)
t.circle(22, 133)
t.seth(90)
t.circle(13, 15)
t.end_fill()
t.pu()
t.setpos(t.xcor()-7,t.ycor()-15)
t.pd()
t.color("white")
t.begin_fill()
t.circle(7)
t.end_fill()

# 左耳
t.color("black")
t.pu()
t.goto(-210,86)
t.setpos(t.xcor()+15,t.ycor()+38)
t.pd()
t.seth(90)
t.circle(-250,30)
t.begin_fill()

# 左
t.circle(-250,18)

# 右
t.seth(270)
t.circle(-270, 12)
prePos = t.pos()

# 下
t.seth(180)
t.circle(100, 30)
t.end_fill()
t.pu()
t.setpos(prePos)
t.pd()
t.seth(270)
t.circle(-270, 18)
t.screensize(50,50,bg='yellow')

# 输出文字
printer = t.Turtle()
printer.hideturtle()
printer.penup()
printer.goto(-350,-100)
printer.write("皮\n\n",move = True, align="left", font=("楷体", 30, "bold"))
printer.goto(-350,-150)
printer.write("卡\n\n",move = True, align="left", font=("楷体", 30, "bold"))
printer.goto(-350,-200)
printer.write("丘\n\n",move = True, align="left", font=("楷体", 30, "bold"))
printer.goto(-350,-250)
printer.write("！！\n\n",move = True, align="left", font=("楷体", 30, "bold"))

t.hideturtle()
t.done()