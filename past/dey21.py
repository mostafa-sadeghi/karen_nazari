# import turtle

# s = turtle.Screen()
# s.bgcolor('silver')
# p = turtle.Pen()
# p.shape('turtle')
# p.pencolor('red')
# p.pensize(4)

# p.penup()
# p.setpos(-90, 30)
# p.pendown()
# p.begin_fill()
# for i in range(5):
#     p.forward(150)
#     p.right(144)
# p.end_fill()
# p.penup()
# p.goto(80, -140)
# p.write("This is our nice star", font=12)

# s.exitonclick()
'''
    *
   * *
  * * * 
 * * * * 
* * * * *     
'''

# print(' '*4 + '* '*1)
# print(' '*3 + '* '*2)
# print(' '*2 + '* '*3)
# print(' '*1 + '* '*4)
# print(' '*0 + '* '*5)

# for i in range(5):
#     print(' '*(5-i-1) + '* ' * (i+1))

# number = int(input('enter how many stars do you want?'))
# for i in range(number):
#     print(' '*(number-i-1) + '* ' * (i+1))

'''
* * * * *
 * * * *
  * * *
   * *
    *

    '''
# print(' '*0 + '* '*5)
# print(' '*1 + '* '*4)
# print(' '*2 + '* '*3)
# print(' '*3 + '* '*2)
# print(' '*4 + '* '*1)

# for i in range(5):
#     print(' ' * i + '* ' * (5-i))

# number = int(input('how many stars do you want? '))
# for i in range(number):
#     print(' ' * i + '* ' * (number-i))

'''
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*
'''
# for i in range(9):
#     if i <= 9/2:
#         print('* ' * (i+1))
#     else:
#         print('* ' * (9-i))

number = int(input('enter how many stars do you want? '))
if number % 2 == 0:
    number -= 1
for i in range(number):
    if i <= number/2:
        print('* ' * (i+1))
    else:
        print('* ' * (number-i))
