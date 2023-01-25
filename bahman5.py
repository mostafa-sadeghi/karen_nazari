# while loop
# numbers = [1, 2, 3, 4]
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2
# print(numbers)


# exercise 1: برنامه بالا رو با حلقه while  بنویس

# name = 'karen'
# for n in name:
#     print(n)

# exercise 2: برنامه بالا رو با حلقه while  بنویس


# for i in range(4):
#     print('ok')
########################################## WHILE LOOP ############################
# 1. counter یا شمارنده
# 2. condition یا شرط حلقه
# 3. update the counter بروزرسانی شمارنده
# i = 0
# while i < 4:
#     print('ok')
#     i = i + 1  # i+=1


# حلقه بی نهایت
# while True:
#     print("ok")

#########################################################

string = input("enter a name ")
# print(string[-1::-1])

# for i in range(len(string)-1, -1, -1):
#     print(string[i])

i = len(string) - 1
while i >= 0:
    print(string[i])
    i -= 1  # i = i -1
