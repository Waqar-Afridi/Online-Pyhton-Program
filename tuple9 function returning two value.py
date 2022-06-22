def number(int1 ,int2):
    add =int1+int2
    mul=int1*int2
    return add,mul
#print(type(number(4,5)))   # agr ap ese print karegy to ye apko answer typle me dega

add,mul=number(4,5)
print(f"the addition of two value is ={add}")
print(f"the multiplication of two value is ={mul}")