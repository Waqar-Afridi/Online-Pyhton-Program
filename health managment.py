# HEALTH MANAGEMENT SYSTEM
# 3 clients--> Harry,Rohan and Hammad
# Total 6 files,i.e[2 files for diet and exercise for each person---> ]

def getdate():
    '''Pre Defined function by harryBhai'''
    import datetime
    return datetime.datetime.now()

clients = ['Harry','Rohan','Hammad']

def ClientsWork(client_name):
    '''Work for client'''

    if client_name in clients :
        print('What You Want To do (1)Exercise (2)Diet')
        client_option = int(input())

        if client_option == 1:

            with open(('Python_vid32File_' + str(client_name) + 'Exercise' + '.txt'), 'w+') as user_file:
                user_exercise_done = user_file.write(input('''Write The Exercises That You Want To Do: '''))

                user_file.seek(0)

                content = user_file.read()

                print('Time: ' + str(getdate()) + '\nExercise that ' + client_name + ' did are: ')
                print(content)

        elif client_option == 2:

            with open(( 'Python_vid32File_' + client_name + 'Diet' + '.txt'), 'w+') as user_file:
                user_exercise_done = user_file.write(input('Write What You Want To Eat: '))

                user_file.seek(0)

                content = user_file.read()
                print('Time: ' + str(getdate()) + '\nFood that ' + client_name + ' took are: ')
                print(content)
    else :
        print('NO SUCH NAME FOUND !!!')



ask_name = input('Enter person\'s name from the list: ' + str(clients))
ClientsWork(ask_name)
