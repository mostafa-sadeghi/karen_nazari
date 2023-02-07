'''
    *
   * *
  * * *
 * * * *
* * * * *
'''

# n = int(input('how many stars do you want? '))
# for i in range(n):
#     print(' '*(n-i-1) + '* '*(i+1))

# i = 0
# while i < n:
#     print(' '*(n-i-1) + '* '*(i+1))
#     i += 1

'''
* * * * *
 * * * *
  * * *
   * *
    *
'''
# i = 0
# while i < 5:
#     print(' '*i + '* ' * (5-i))
#     i += 1

'''
*
* *
* * *
* * * *
* * *
* *
*
'''
# n = int(input('> '))
# for i in range(n):
#     if i < n/2:
#         print('* ' * (i+1))
#     else:
#         print('* ' * (n-i))
# Exercise: do it with while loop


'''
  *
* *
  *
'''

'''
    *
  * *
* * *
  * * 
    *
'''


'''
      *
    * *
  * * *
* * * *
  * * *
    * *
      *
'''


m = int(input('enter how many stars do you want?'))
j = 2
i = 0
while i < m:
    if i < m/2:
        print(' ' * (m-2*i-1) + '* '*(i+1))

    else:
        print(' ' * (j) + '* '*(m-i))
        j += 2
    i += 1
