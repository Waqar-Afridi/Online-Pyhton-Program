print("enter number 1 ")
num1=(input())
print("enter number 2 ")
num2=(input())
try:

    print("the sum of these two number is :"
          ,int(num1)+int(num2))
except Exception as e:
    print(e)


print("this line is very important")