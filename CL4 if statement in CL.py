even_num=list(range(1,11))
even_list=[]
for i in even_num:
    if i%2==0:
     even_list.append(i)
     print(i)

# CL

even_number=[i for i in range(1,11) if i%2==0 ]
print(even_number)

odd_number=[i for i in range(1,11) if i%2!=0 ]
print(odd_number)