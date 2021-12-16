from custom_database import *
while True:
    for i in range(10):
        print('')
    choice = input('(1)Create new hash\n(2)Encrypt database\n(3)Decrypt database\n(4)Backup\n(5)Create database\n(6)Save\n(7)Edit database\nYour choice: ')
    if choice == "1":
        get.new_hash() #Makes a new hash
    if choice == "2":
        encrypt.all(password=str(input('Password: ')))
    if choice == "3":
        decrypt.all(password=str(input('Password: ')))
    if choice == "4":
        backup.all()
    if choice == "5":
        data_base.create.database(data_base=input('Enter the new databases name: ').lower(), type=input('column_row or list: '))
    if choice == "6":
        save.all()
    if choice == "7":
        choice=input('\n\n\n(1)Users\n(2)Add to row/list\n(3)Show databases\n(4)Delete database\nYour choice: ')
        if choice == "1":
            other=input('\n\n\n(1)Create user\n(2)Remove user\nYour choice: ')
            if other == "1":
                users.create(new_user=str(input('New username: ')), new_password=input('New password: '), new_permission=input('New permission: '))
            if other == "2":
                users.remove(user=str(input('User to remove: ')))
        if choice == "2":
            data_base.edit.add_row_term()
        if choice == "3":
            data_base.show.all_data_bases()
        if choice == "4":
            data_base.remove.one_set(data_base=str(input('Database: ')))
        choice=''
