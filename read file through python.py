f=open("waqar.txt")
# print(f.read())  ---> ye file me jitne b text hai on sab ko print karaega
# readline()...> is k zary hm ak ak line ko print karsakty hai
# print(f.readline())   #---> print line 1
# print(f.readline())   #---> print line 2
# print(f.readline())   #---> print line 3

print(f.readlines())  #---> ye hamary text ko list me print kary ga ak list dega

f.close()