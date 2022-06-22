my_dict={"name":"waqar","age":24,"cellno":"xyz",
         "favt_moves":['walamba che yakhya shy','d ta ye ka']
    ,"fav_book":('operating system','networking','machine learning','security')}

my_dict1={"name1":"waqar1","agee":242,"cellnoq":"xyzq",
         "favt_movess":['walambaa chea yakhyaa shya','daa taa yee kaa']
    ,"fav_booka":('operatinga systema','networkinga','machinea learninga','securitya')}
# my_item=my_dict.items()
# print(my_item)
# print(my_dict.keys())
# print(my_dict.values())

#add and delete element in dict
# my_dict['favrt_song']=["hahhah",'heeehehehe']
# my_dict.update(my_dict1)
# my_dict.clear()
#print(my_dict)
# my_dict1.pop("name1")
# print(my_dict1)
# print(len(my_dict))
# `if "name12"in my_dict1:
#     print("ok")
# else:
#     print('no')`

#exerise of dict
# create_dict={'name':"waqar ahmad",'address':'mereobak hangu',
#              'age':'24 year old','gernder':"male"}
# x=input("ask for your information please!")
# if x=="name":
#     print("waqar ahmad",x)
# elif x=='address':
#         print("meerobak hangu",x)
# elif x=='age':
#     print('24 year old',x)
# elif x=='gender':
#     print("male",x)
# else:
#     print("dictionary is empty")

#2nd method
create_dict={'name':"waqar ahmad",'address':'mereobak hangu',
             'age':'24 year old','gernder':"male"}
print("please enter the word whose meaning you want!")
ax=input()
print(create_dict[ax])
