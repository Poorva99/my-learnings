# 1
# total= int(input('enter a number: ')) # input function returns string data type by default
# n= int(input('enter a number: ')) # input function returns string data type by default
# # print(type(num2))
# avg=total/2
# print(avg)

# 2
# n1=int(input('enter a number: '))
# n2=int(input('enter a number: '))
# n3=int(input('enter a number: '))

# total=n1+n2+n3
# avg=total/3
# print(avg)

# 3 using for loop

# n=int(input('enter number for avg: '))
# total = 0
# for x in range(n):
#     num = int(input('enter a number: '))
#     total += num
#
# avg = total/n
# print(avg)

# 4 handling zero division error

# n = int(input('enter number for avg: '))
# if n != 0:
#     total = 0
#     for x in range(n):
#         num = int(input('enter a number: '))
#         total += num
#         print(x)
#
#     avg = total/n
#     print(avg)
# else:
#     avg = 0
#     print(avg)

# 5 remove negative input
# n = int(input('enter number for avg: '))
# if n != 0:
#     total = 0
#     for x in range(n):
#         num = int(input('enter a number: '))
#         total += num
#         print(x)

#     avg = total/n
#     print(avg)
# elif n<0:
#         print("Avg can't be calculated for negative number")
# else:
#     avg = 0
#     print(avg)


# 6(Poorva) take input until user enters a valid number ******* thought by poorva + 70
# recursive function - when not to use- when stopping recursive function depends on external factors.

# count = 0
#
# def fun():
#     global count
#     count+=1
#     n = int(input('enter number for avg: '))
#
#     if n != 0 and n>0:
#         total = 0
#         for x in range(n):
#             num = int(input('enter a number: '))
#             total += num
#             # print(x)
#         avg = total/n
#         return avg
#
#     elif n<0:
#         print("Avg can't be calculated for negative number")
#         fun()
#     else:
#         avg = 0
#         return avg
#
#
#
#
#
# average = fun()
# print(average)
# print(count)


# 6(poorva) take input until user enters a valid number

# while True:
#     n = int(input('enter number for avg: '))
#     if n != 0:
#         total = 0
#         for x in range(n):
#             num = int(input('enter a number: '))
#             total += num
#             print(x)
#             break
#         avg = total/n
#         print(avg)
#     elif n<0:
#             print("Avg can't be calculated for negative number")
#     else:
#         avg = 0
#         print(avg)
#         break

# 7 short circuiting


# n = int(input('enter number for avg: '))
# total = int(input('enter total: '))
#
# avg = n and total/n
#
# print(avg)

# 8 negative,

# n = int(input('enter number for avg: '))
# total = int(input('enter total: '))
#
# avg = n and total/n if n>=0 else "not valid"
#
# print(avg)




# Program to iterate through a list using indexing

# Program to iterate through a list using indexing

genre = ['pop', 'rock', 'jazz']

# iterate over the list using index
for i in genre:
    if 'p' in i:
        print("I like", i)



























































































































































