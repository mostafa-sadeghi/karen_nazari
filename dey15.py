

# loops  in python : for loop and while


# name = 'nikan'
# print(name[0])
# print(name[1])
# print(name[2])
# print(name[3])
# print(name[4])
# for x in name:
#     print(x)
# for x in name:
#     print(x, end='-')

# numbers = [1, 2, 3, 4, 5]
# for number in numbers:
#     print(number)

# numbers = (1, 2, 3)
# for i in numbers:
#     print(i)

# r = range(1, 5)
# print(r[0])
# for i in range(5):
#     print(i)


# عددهای زوجه کمتر از 100

# ایجاد لیست شامل اعداد یک تا صد
# روش اول
# numbers = []
# for i in range(1, 101):
#     numbers.append(i)
# print(numbers)
# روش دوم

# numbers = list(range(1, 101))

# print(numbers)

# find even numbers with for loop
# even_numbers = []
# for n in numbers:
#     if n % 2 == 0:
#         even_numbers.append(n)

# print(even_numbers)

# اعداد فرد بین 1000000, 1000700
# بدون استفاده از if

# odd_numbers = []
# for n in range(1_000_001, 1_000_701, 2):
#     odd_numbers.append(n)

# print(odd_numbers)

# excercise 1 : این کار رو با کمک if انجام بده
# excercise 2 : با کمک ترتل و حلقه فور مثلث، مربع و پنج ضلعی بکش


# import turtle

# s = turtle.Screen()
# s.setup(620, 620)
# s.bgcolor('black')

# p = turtle.Pen()
# p.shape('turtle')
# p.pensize(4)
# p.speed('fastest')  # p.speed(10)
# p.pencolor('red')
# COLORS = ["red", "green", "blue", "cyan", "silver"]
# n = -1
# for ang in range(0, 360, 15):
#     n = n + 1
#     if n == 5:
#         n = 0
#     p.pencolor(COLORS[n])
#     p.seth(ang)
#     if ang <= 270:
#         p.fillcolor(COLORS[n])
#         p.begin_fill()

#         p.circle(100)
#         p.end_fill()
#     else:
#         # p.fillcolor(COLORS[n])
#         # p.begin_fill()

#         p.circle(100)
#         # p.end_fill()


# p.penup()
# p.setpos(100, 270)
# p.pendown()
# p.write("Nice picture", font=("", 22, "bold"))
# p.hideturtle()  # p.ht()


# s.exitonclick()
