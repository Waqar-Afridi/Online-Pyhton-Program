# # fuction
# def add_num(a,b):
#     return a+b
# # print(add_num())
# a=int(input("enter n1..."))
# b=int(input("enter n2..."))
# total=add_num(a,b)
# print(total)

# word character finder
# def word_char(name):
#     return name[-1]
# print(word_char("waqar"))

# Even and odd
# def evve_odd(n):
#     if n%2==0:
#         print("No is even")
#     else:
#         print("No is odd")
# evve_odd(5)

# 2nd method

# def hy(a):
#     if a%2==0:
#         return 'even'
#     return 'odd'
# print(hy(6))

# no arg and no perameter
# def song():
#     return 'happy brith day'
# print(song())

# Palindrom

# def palindrom(word):
#     if word==word[::1]:
#         return True
#     else:
#         return False
# print(palindrom("eye"))

# grater then finder

def greater(num1,num2):

    if num1>num2:
        return 'num1 is grater'
    else:
        return 'num2 is grater'
n1 = int(input("enter num 1..."))
n2 = int(input("enter num 2..."))
print(greater(n1,n2))