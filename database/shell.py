#add_column has had no testing done at all.
#remove_column has had no testing done at all.
#Optimize save file has had no test done at all.
from custom_database import *
profanityFilter.setup()
while True:
    for i in range(10):
        print('')
    if users.return_login_cred() == False:
        choice = input('(1)Create new hash\n(2)Encrypt database\n(3)Decrypt database\n(4)Backup\n(5)Create database\n(6)Save\n(7)Edit database\n(8)Optimize save file\n(9)Check profanity\n(10)Login\nYour choice: ')
    else:
        choice = input('(1)Create new hash\n(2)Encrypt database\n(3)Decrypt database\n(4)Backup\n(5)Create database\n(6)Save\n(7)Edit database\n(8)Optimize save file\n(9)Check profanity\n(10)Logout\nYour choice: ')
    if choice == "9":
        print(list1)
        if profanityFilter.filter(var=input('Your input: ').lower()) == 1:
            print('Match Found')
        else:
            print('Match Not Found')
    if users.return_login_cred() != False:
        if choice=="10":
            users.logout()
            choice=''
    if users.return_login_cred() == False:
        if choice=="10":
            users.login_request(user=input('Username: '), password=input('Password: '))
    if choice == "1":
        get.new_hash() #Makes a new hash
        get.encrypt_hash(other=True, passw=input('Backup Password: '))
    if choice == "2":
        encrypt.all(password=str(input('Password: ')))
    if choice == "3":
        decrypt.all(password=str(input('Password: ')))
    if choice == "4":
        backup.create(backup_name=input('What is your backup name: '), password=input('Enter you encryption Password: '))
    if choice == "5":
        data_base.create.database(data_base=str(input('Enter the new databases name: ')).lower(), type=str(input('column_row or list: ')))
    if choice == "6":
        save.all()
    if choice == "8":
        choice=input('Would you like to save (y/n): ').lower()
        if choice == "y":
            optimize.run(save_optimizations=True)
        if choice == "n":
            optimize.run(save_optimizations=False)
        choice = ''
    if choice == "7":
        choice=input('\n\n\n(1)Users\n(2)Add to row\n(3)Show databases\n(4)Delete database\n(5)Remove row\n(6)Show items in database\n(7)Add Column\n(8)Remove Column\n(9)Overload\nYour choice: ')
        if choice == "9":
            import random
            for i in range(int(input('Choose a Number(100-10000);No comas: '))):
                a=''
                b=''
                for i in range(8):
                    a+=random.choice('12q9fhecycgy43gf6ucw4b6fxnc')
                for i in range(8):
                    b+=random.choice('12q9fhecycgy43gf6ucw4b6fxnc')
                data_base.edit.add_row(data_base=input('Enter database to overload: '), new_row=[a, b], split=False)
            save.all()
        if choice == "1":
            other=input('\n\n\n(1)Create user\n(2)Remove user\nYour choice: ')
            if other == "1":
                users.create(new_user=str(input('New username: ')), new_password=str(input('New password: ')), new_permission=str(input('New permission: ')))
            if other == "2":
                users.remove(user=str(input('User to remove: ')))
        if choice == "2":
            data_base.edit.add_row_term()
        if choice == "3":
            data_base.show.all_data_bases()
        if choice == "4":
            data_base.remove.one_set(data_base=str(input('Database: ')))
        if choice == "5":
            data_base.edit.remove_row(data_base=str(input('Database: ')))
        if choice == "6":
            data_base.show.all_in_database(database=str(input('Database: ')))
        if choice == "7":
            data_base.edit.add_column(data_base=str(input('Database: ')), column_name=str(input('What is the new column: ')))
        if choice == "8":
            data_bas=str(input('Database: '))
            data_base.show.show_column(data_base=data_bas)
            data_base.edit.remove_column(data_base=data_bas, column=str(input('Column to remove: ')))
        choice=''
