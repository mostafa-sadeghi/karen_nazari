# about function
# python built-in functions  توابع داخلی پایتون
# min max sum

# numbers = [1, 2, 3]
# print('min is', min(numbers))
# print('max is', max(numbers))
# print('sum is', sum(numbers))
# print('len is', len(numbers))

# تعریف تابع
# def ave(scores):
#     count = 0
#     total = 0
#     for score in scores:
#         count += 1
#         total += score
#     return f'student average is : {(total/count):.2f}'


# scores = []
# print('''Welcome to our program.
# our peogram is used to calculate average of student.
# ''')
# for i in range(3):
#     score = float(input('enter student score> '))
#     scores.append(score)

# result = ave(scores)
# print(result)
# print(ave(scores))

# def add(number1,number):
#     return number1+number2

# exercise:  greet function to say hello

# define a function    تعریف تابع


def greet(name, family):
    return f'Hello {name} {family}'


# calling the function   صدازدن تابع
name = input("enter a name> ")
family = input("enter a family> ")
result = greet(name, family)
print(result)


# while loop
