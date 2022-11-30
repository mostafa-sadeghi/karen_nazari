# shopping_list = []

# print(type(shopping_list))
# shopping_list.append("apple")
# shopping_list.append("banana")
# print("my shopping list is: ", shopping_list)

# x = shopping_list[0]
# print("first item of list is : ", x)
# y = shopping_list[1]
# print(f'second item of list is : {y}')


# numbers = [1, 2, 3, 4, 5]
# print("my list is :", numbers)
# numbers.append(6)
# print("my list is: ", numbers)

# x = numbers[0] + numbers[1] + numbers[2] + numbers[3] + numbers[4]
# print(f"sum of list numbers is: {x}")

# چسباندن رشته ها

# string = ['a','b','c','d']

# output = string[0] + string[1] + string[2] + string[3]
# print("output is : ", output)

# تغییر مقدار لیست
# string = ['a', 'b', 'c', 'd']

# string[1] = 'fffffff'
# print("new list is: ", string)
# حذف از لیست
# numbers = [1, 2, 3, 4, 5, 6]
# del numbers[3]
# print("numbers is :", numbers)

# slicing
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# new_numbers = numbers[3:8]
# print("new numbers is: ", new_numbers)

# exercise لیستی از کاراکترها
# chractres = ['a','b','c','d','e','f']

# slice 'c','d','e'
# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# even_numbers = numbers[1::2]
# print("even numbers are: ", even_numbers)


# exercise : نمایش اعدا فرد کمتر از 10

# numbers = [1, 2, 3, 4]
# characters = ['a', 'b']
# my_list = [numbers, characters]
# print(my_list[0][0])
# print(my_list[0][1])
# print(my_list[1][1])
# string = '*' + 2 > error
# string = '*' + '*'
# print(string)
# string = '*' * 3
# print(string)
# numbers = [1, 2, 3]
# new_numbers = numbers + [4, 5, 6]
# print(new_numbers)
# new_numbers = numbers * 3
# print(new_numbers)
# numbers[0] = 10
# print(numbers)
# string = 'abcd'
# string[0] = 'z'> error

# exercise 1:
'''
numbers_1 = [1,2,3,4,5]
numbers_2 = [6,7,8,9,10]
numbers_3 = [11,12,13,14]

make a list from above lists and iterate over them
یک لیست متشکل از سه لیست بالا بساز و تک تک آیتم های آن را نمایش بده

'''

# name = input('enter your name ')
# family = input('enter your family ')
# print('your name is', name, 'and your family is', family)
# print('your name is' + ' ' + name + ' ' + 'and your family is' + ' ' + family)
# print(f'your name is {name} and your family is {family}')
# print(type(x))

# class exercise: add two numbers

# numbers_1 = input('enter first number ')
# numbers_2 = input('enter second number ')

# output = int(numbers_1) + int(numbers_2)

# print(f'{numbers_1} + {numbers_2} = {output}')

# numbers = [1, 2, 3, 4]
# numbers.append(5)
# print(numbers)

# Exercise:
'''
numbers = []
از ورودی 4 عدد بگیر و در لیست بالا اضافه کن.
سپس مجموع اعداد را به صورت زیر نمایش بده
3 + 4 + 6 + 10 = 23

'''
# how to delete item from list چطور از لیست حذف کنیم

# x = ['a', 'b', 1, 'd']
# del x[1]
# print('my list is :', x)

# x.remove(1)
# print('my list after removing value "1"', x)
# x.remove('d')
# print('my list after removing value "d"', x)

numbers = [1, 2, 3, 4, 4, 3, 4, 2, 1]
print('count of 4:', numbers.count(4))

# Exercise :
'''
با استفاده از دستور اینپوت 5 عدد را از ورودی دریافت نماید و در لیست ذخیره کند.
در مر حله بعد عددی را از ورودی با اینپوت دریافت کند و تعداد تکرار آن عدد در لیست را نمایش دهدو
'''
