# lst=[1,2,3,5,6,7,12,23,22,34,56,'khan','ali','anything']
# for i in lst:
#     if i> 6:
#         print(i)
    # else:
    #     print('not found')


# while(True):
#     x=int(input("enter number\n"))
#     if x>100:
#         print("congrate u put grater value then 100\n")
#         break
#     else:
#         print("try again grater value then 100\n")
#         continue

no=20
guess=1
while(guess<=5):

    print("enter number for guessing..")
    x = int(input(""))
    if x<no:
        print(f"the {x} is to small\n")
    elif x>no:
        print(f"you enter {x}is to large ")

    else:
        print(f"you select right number is {x} ")
        print(f"u guess in {guess} time\n you win")
        break
    print(5-guess,"number of gusses left")
    guess+=1


else:
    if guess>5:
        print("ggame is ove")
