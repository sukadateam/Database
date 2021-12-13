from custom_database import *
choice = input('(1)Create new hash\n(2)Encrypt database\n(3)Decrypt database\n(4)Backup\nYour choice: ')
if choice == "1":
    get.new_hash() #Makes a new hash
if choice == "2":
    encrypt.all(password=str(input('Password: ')))
if choice == "3":
    decrypt.all(password=str(input('Password: ')))
if choice == "4":
    backup.all()
