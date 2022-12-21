name = input('enter your name: ')
age = int(input('enter your age: '))

# if age >= 18:
#     print(name, 'You are adult')
#     print()
#     print('ok')
# if age == 18:

#     print('you are 18 years old')


if age >= 18:
    print(name, 'You are adult')
    print()
    print('ok')
# elif age >= 12 and age < 18:
elif 12 <= age < 18:
    print('junior')
else:
    print('Kid')

# if age == 11 or age == 12


# Exercise1:
'''
برنامه ای بنویسید که سن کاربر را در یافت نماید و 
در صورتی که سن کاربر 
مساوی 
11 یا 12 یا 15 یا 18 
باشد
ok را نمایش دهد
'''

# exercise 2:
'''
برنامه ای بنویسید که سه عدد از ورودی در یافت کند
و در صورتی که مجموع آنها بزرگتر از 20 باشد 
پیغام
ok
و در غیر اینصورت
notok 
را نمایش دهد.
'''
