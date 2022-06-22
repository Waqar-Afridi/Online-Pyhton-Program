 #square ={1:1,2:4,3:9}
square={value:value**2 for value in range(1,6) }
print(square)

string = "waqar"
word_count={key:string.count(key) for key in string}
print(word_count)