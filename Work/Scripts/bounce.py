"""
一个橡胶球从100米高处落下，每次落地后都会反弹到原高度的3/5。编写一个程序bounce.py，打印出前10次反弹的高度表格。"""

height = 100
bounce = 1
while bounce <= 10:
    height = height * (3 / 5)
    print(bounce, round(height, 4))
    bounce += 1
