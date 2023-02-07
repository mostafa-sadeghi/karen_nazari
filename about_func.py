# def my_func():
#     print("hello")
#     print("welcome to our python class")
#     print("we are going to learn everythings about python")


# my_func()

# def my_func(name):
#     print(f"hello {name}")
#     print("welcome to our python class")
#     print("we are going to learn everythings about python")


# name = input('enter your name: ')
# my_func(name)

# def my_func(name, course):
#     print(f"hello {name}")
#     print(f"welcome to our {course} class")
#     print(f"we are going to learn everythings about {course}")


# name = input('enter your name: ')
# course = input('enter course name:')
# my_func(name, course)


# add     sub     mul     div

def greet(name, family):
    return f'hello {name} {family}'


# print(__name__)
if __name__ == "__main__":
    n = input('enter student name ')
    f = input('enter student family ')
    print(greet(n, f))
