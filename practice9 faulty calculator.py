# age=int(input("enter your age "))
# if age>18 and age<=60:
#     print("you can drive")
# elif age==18:
#     print("plse come to office we want to chick you physicaly")
# elif age<18 :
#     print("you cant drive becasue you are to young")
# else:
#     print("sorry you are very old men")


# "in" key and "not in" key

# lst=[1,2,3,4,5,6]
# print(4 in lst)
# print(9 not in lst)
# if 9 not in lst:
#     print("True")
# else:
#     print("False")


# faulty calculater:

print("enter the first number:")
no1=int(input())
print("enter the operators '+,-,*,/':")
op=(input())
print("enter the second number:")
no2=int(input())

if op=="+":
    if no1==56 and no2==9 or no1==9 and no2==56:
        print(f"the sum of {no1} and {no2} is = 77")
    else:
        print(f"the sum of {no1} and {no2} is =",no1+no2)

elif op=='-':
    print(f"the difference of {no1} and {no2} is =", no1 - no2)

elif op == '*':
    if no1 == 45 and no2 == 3 or no1 == 3 and no2 == 45:
        print(f"the multiplication of {no1} and {no2} is = 555")
    else:
        print(f"the multiplication of {no1} and {no2} is =", no1 * no2)

elif op == '/':
    if no1 == 56 and no2 == 6 or no1 == 6 and no2 == 56:
        print(f"the division of {no1} and {no2} is = 4")
    else:
        print(f"the division of {no1} and {no2} is =", no1 / no2)

else:
    print("invalid input")