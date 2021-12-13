#Things to do next:
#Check to make sure save class works as intended.
import sys, os
from pyAesCrypt.crypto import decryptFile, encryptFile
password=None
from settings import *
if sys.version[0:len(required_version)] != required_version:
    print('Required python version:', required_version)
    print('Current python version:',sys.version[0:len(required_version)])
if sys.version[0:len(required_version)] == required_version:
    import random, shutil
    try:
        from directory import path
    except ModuleNotFoundError:
        print('Please setup application.')
    print('Set path:', path)
    os.chdir(path)
    from reset import *
    try:
        from data_save import *
    except:
        try:
            from data import *
        except:
            pass
    import pyAesCrypt
    def exit():
        exit
    class restore:
        def all():
            from files_to_backup import backup_files
            global path
            mod_path=path.replace('database','Backups')
            for i in range(len(backup_files)):
                shutil.copy(mod_path+'\\'+backup_files[i], path+'\\'+backup_files[i])
    class backup:
        def all():
            from files_to_backup import backup_files
            global path
            mod_path=path.replace('database','Backups')
            for i in range(len(backup_files)):
                shutil.copy(path+'\\'+backup_files[i],mod_path)
    class info:
        def operating_system():
            global system
            return system
        def python_version():
            return sys.version[0:len(required_version)]
        def app_version():
            global program_version
            return program_version
    class get:
        def get_hash():
            try:
                password = get.password()
                decrypt.hash(password)
                global drive_letter
                file=open(drive_letter+':/hash.txt','r').read()
                return file
            except ValueError:
                print('Incorrect password!')
        def new_hash():
            get.random_hash()
            get.encrypt_hash()
            password=None
        def encrypt_hash():
            password=get.password()
            global drive_letter
            pyAesCrypt.encryptFile(drive_letter+':/hash.txt', drive_letter+':/hash.aes', password)
            os.remove(drive_letter+':/hash.txt')
        def password():
            return input('Password: ')
        def new_password(new_password=None):
            if new_password != None:
                pass
                #Ask for current password to allow change.
                #Change password.
                #Delete current hash.
                #Create new hash with new password.
                #Tell user process completed.
            if new_password == None:
                print(errors.cannot_call_func())
        def random_hash(length=100):
            ah=''
            for i in range(length): 
                ah+=random.choice('ajfygweuoichwgbuieucr73rwecb638781417983b 623v9923 r t72344y 23uc3u2b4n9832 4b2c794y 237bc2423nc482b3c427 rfgshdfuw38263872guihfef86w4t878whryfeg48tg34hf7w')
            global drive_letter
            file=open(drive_letter+':/hash.txt','w')
            file.write(ah)
            file.close()
    class decrypt:
        def hash(password):
            pyAesCrypt.decryptFile('E:/hash.aes','E:/hash.txt',password)
            global drive_letter
            return open(drive_letter+':/hash.txt','r').read()
        def data(password):
            try:
                pyAesCrypt.decryptFile('data.aes','data.py',password)
                os.remove('data.aes')
            except:
                pass
        def cache(password):
            pyAesCrypt.decryptFile('cache.aes','cache.py',password)
            os.remove('cache.aes')
        def opt(password):
            pyAesCrypt.decryptFile('opt.aes','opt.py',password)
            os.remove('opt.aes')
        def all(password):
            #decrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
            try:
                d_password=decrypt.hash(password)
                decrypt.data(d_password)
            except ValueError:
                print('Wrong password.')
            try:
                global drive_letter
                os.remove(drive_letter+':/hash.txt')
            except:
                pass
            #decrypt.cache(d_password)
            #decrypt.opt(d_password)
    class encrypt:
        def data(password):
            global fail_safe
            failed=False
            if fail_safe==True:
                try:
                    open('data.aes','r')
                    print('Existing file found. Cannot encrypt.')
                    failed=True
                except:
                    pass
            if failed == False:
                global do_not_remove
                pyAesCrypt.encryptFile('data.py','data.aes',password)
                if do_not_remove==False:
                    os.remove('data.py')
        def cache(password):
            global do_not_remove
            pyAesCrypt.encryptFile('cache.py','cache.aes',password)
            if do_not_remove==True:
                os.remove('cache.py')
        def opt(password):
            global do_not_remove
            pyAesCrypt.encryptFile('opt.py','opt.aes',password)
            if do_not_remove==True:
                os.remove('opt.py')
        def all(password):
            d_password=decrypt.hash(password)
            #encrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
            encrypt.data(d_password)
            #encrypt.cache(d_password)
            #encrypt.opt(d_password)
            try:
                global drive_letter
                os.remove(drive_letter+':/hash.txt')
            except:
                pass
    class save:
        def all():
            from vars_to_save import list
            file=open('data_save.py','w')
            for i in range(len(list)):
                file.write(list[i]+'='+str(globals()[list[i]])+'\n')
            file.write('\n')
            file.close()
    class clear:
        def normal():
            for i in range(100):
                print('')
    class check_type:
        def data_format(data_base=None):
            #Call to return data_base type.
            if data_base != None:
                global data_bases
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        return (data_bases[i])[3]
            if data_base == None:
                print(errors.cannot_call_func('check_type.data_format()'))
        def data_base_exists(data_base=None):
            if isinstance(data_base, str) == False and data_base != None:
                print(errors.not_str())
            if isinstance(data_base, str) == True or data_base==None:
                if data_base != None:
                    global data_bases
                    found=False
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            found = True
                    return found
                if data_base == None:
                    print(errors.cannot_call_func('check_type.data_base_exists()'))
    class users:
        def disable(user=None):
            #Disables a user
            if user != None:
                global known_users, active_users
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        active_users[i]=False
            if user == None:
                print(errors.cannot_call_func('users.disable()'))
        def enable(user=None):
            #Enables a user
            if user != None:
                global known_users, active_users
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        active_users[i]=True
            if user == None:
                print(errors.cannot_call_func('users.disable()'))
        def create(new_user=None, new_password=None, new_permission=None):
            global known_users, passwords, permissions
            if new_user != None and new_password != None:
                skip=False
                for i in range(len(known_users)):
                    if known_users[i]==new_user:
                        skip=True
                        print(errors.user_exists())
                if skip == False:
                    if isinstance(new_user, str) == True:
                        if isinstance(new_password, str) == True:
                            if isinstance(new_permission, str) == True or new_permission==None:
                                known_users.append(new_user)
                                passwords.append(new_password)
                                permissions.append(new_password)
                                active_users.append(True)
                    if isinstance(new_user, str) == False:
                        print('new_user must be str')
                    if isinstance(new_permission, str) == False:
                        print('new_permission must be str')
                    if isinstance(new_permission, str) == False and new_permission != None:
                        print('new_password must be str or None') 
            if new_user == None or new_password == None:
                print(errors.cannot_call_func('users.create()'))
        def remove(user=None):
            if user != None:
                found=False
                global known_users, passwords, permissions
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        known_users.pop(i)
                        passwords.pop(i)
                        permissions.pop(i)
                        active_users.pop(i)
                        found=True
                if found==False:
                    print(errors.user_not_found())
            if user == None:
                print(errors.cannot_call_func('users.remove()'))
        def show_all():
            global known_users
            for i in range(len(known_users)):
                print('User: '+known_users[i])
                print('Permission: '+permissions[i])
        def change_permissions():
            pass
        def change_name():
            pass
        def change_password():
            pass
        def return_users():
            return known_users
        def login_request(user=None, password=None):
            #Will return True if credentials are correct, if not will return False
            if user != None and password != None or password==None:
                global known_users, passwords, user_logged, user_permission
                if isinstance(user, str)==True and isinstance(password, str)==True or password == None:
                    if user in known_users:
                        for i in range(len(known_users)):
                            if known_users[i]==user:
                                if passwords[i]==password:
                                    if active_users[i]==True:
                                        user_logged=known_users[i]
                                        user_permission=permissions[i]
                                        return True
                                    if active_users[i]==False:
                                        print('User is not active.')
                if isinstance(user, str) == False:
                    print(errors.not_str())
                if isinstance(password, str) == False and password != None:
                    print(errors.not_str())
                if user not in known_users:
                    print(errors.user_not_found())
                if user_logged==False:
                    return False
            if user == None:
                print(errors.cannot_call_func('users.login_request()'))
        def logout():
            global user_logged, user_permission
            user_permission=None
            user_logged=None
        def return_login_cred():
            global user_logged, user_permission
            return user_logged, user_permission
    class data_base:
        class edit:
            def add_item(data_base=None, item_to_add=None):
                #Used for the list types.
                global data_bases, lists
                if data_base != None and item_to_add != None:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            if (data_bases[i])[3]=="list":
                                for x in range(len(lists)):
                                    if (lists[x])[0]==data_base:
                                        (lists[x])[1].append(item_to_add)
                                        print(lists)
                                        break
                if data_base == None or item_to_add == None:
                    print(errors.cannot_call_func('data_base.edit.add_item()'))
            def remove_item(data_base=None, item_to_remove=None):
                #Used for the list types.
                global data_bases, lists
                if data_base != None and item_to_remove != None:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            if (data_bases[i])[3]=="list":
                                for x in range(len(lists)):
                                    if (lists[x])[0]==data_base:
                                        try:
                                            (lists[x])[1].remove(item_to_remove)
                                            print(lists)
                                        except:
                                           pass
                                        break
                if data_base == None or item_to_remove == None:
                    print(errors.cannot_call_func('data_base.edit.remove_item()'))
            def add_row(data_base=None, new_row=None):
                #You can add as many objects to a row as you please, but it may not fit in your assinged constraints. No problems will occur though.
                if data_base != None and new_row != None:
                    if isinstance(new_row, list) == True:
                        row.append([data_base,new_row])
                    if isinstance(new_row, list) == False:
                        print(errors.not_list())
                if data_base == None or new_row == None:
                    print(errors.cannot_call_func('data_base.edit.add_row()'))
            def remove_row(data_base=None):
                if data_base != None:
                    global row
                    rows=[]
                    rows_count=0
                    a=0
                    #Gather sets that correspond with called data_base
                    try:
                        for i in range(len(row)):
                            if (row[i-a])[0]==data_base:
                                rows.append(row[i-a])
                                row.pop(i-a)
                                a+=1
                                rows_count+=1
                    except:
                        pass
                    #Print known sets on screen.
                    for i in range(len(rows)):
                        print('#'+str(i)+' : '+str(rows[i]))
                    try:
                        a=input('Choose a set to delete: ')
                        try:
                            a=a.replace('#','')
                        except:
                            pass
                        a=int(a)
                    except ValueError:
                        print('Please enter the corresponding number #?')
                    #If input is correct then ask user if they wish to remove it.
                    if isinstance(a, int) == True:
                        if rows_count-1 >= a:
                            print('Remove:',rows[a])
                            choice = input('Are you sure(y/n): ').lower()
                            if choice == "yes" or "y":
                                rows.pop(a)
                            elif choice == "no" or "n":
                                print('No changes have occured.')
                            else:
                                print('Invalid response.')
                        if rows_count <= a:
                            print('That item does not exist.')
                    for i in range(len(rows)):
                        row.append(rows[i])
                if data_base == None:
                    print(errors.cannot_call_func('data_base.edit.remove_row()'))
                #Must be column_row
            def add_column(data_base=None, column_name=None):
                global debug, data_bases
                if data_base != None and column_name != None:
                    if debug==True:
                        print("Adding column at",data_base,"with name",column_name.lower())
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            if (data_bases[i])[3]=="column_row":
                                (data_bases[i])[4].append(column_name.lower())
                if data_base == None or column_name == None:
                    print(errors.cannot_call_func('data_base.edit.add_column()'))
            def remove_column(data_base=None, column=None, remove_row=False):
                if data_base != None and column != None or '':
                    global data_bases, debug, row
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            if debug==True:
                                print('Database Found!')
                            if (data_bases[i])[3] == "column_row":
                                if debug==True:
                                    print("Correct data_base type!")
                                if column in (data_bases[i])[4]:
                                    print("Removed: "+str(column))
                                    a=len((data_bases[i])[4])
                                    for e in range(a):
                                        if ((data_bases[i])[4])[e] == column:
                                            print(e)
                                            break
                                    (data_bases[i])[4].remove(column)
                                    print(data_bases[i])
                                    rows=[]
                                    rows_count=0
                                    a=0
                                    #Gather sets that correspond with called data_base
                                    try:
                                        for i in range(len(row)):
                                            if (row[i-a])[0]==data_base:
                                                rows.append(row[i-a])
                                                row.pop(i-a)
                                                a+=1
                                                rows_count+=1
                                    except:
                                        pass
                                    #Remove or Empty column(s) in row(s)
                                    if remove_row==False:
                                        for i in range(rows_count):
                                            ((rows[i])[1])[e]=None
                                    if remove_row==True:
                                        for i in range(rows_count):
                                            ((rows[i])[1]).pop(e)
                                    print(rows)
                if data_base == None or column == None or '':
                    print(errors.cannot_call_func('data_base.edit.remove_column()'))
                #Goes through all lists for the column and changes it to equal None.
                #Must be column_row
        class empty:
            #Clear all info in 1 or more databases.
            def all():
                global lists, row
                lists=[]
                row=[]
            def one(data_base=None):
                if data_base != None:
                    a=0
                    global row, lists
                    for i in range(len(row)):
                        if (row[i-a])[0]==data_base:
                            row.pop(i-a)
                            a+=1
                    a=0
                    for i in range(len(lists)):
                        if (lists[i-a])[0]==data_base:
                            lists.pop(i-a)
                            a+=1
                if data_base == None:
                    print(errors.cannot_call_func('data_base.empty.one()'))
        class reset:
            #Redirects to data_base.empty.
            def all():
                data_base.empty.all()
            def one():
                data_base.empty.one()
        class show:
            def show_column(data_base=None):
                if data_base != None:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            if (data_bases[i])[3]=="column_row":
                                print((data_bases[i])[4])
                if data_base == None:
                    print(errors.cannot_call_func('data_base.show.show_column()'))
            def show_row(data_base=None):
                #Must be column_row type
                global row
                if data_base != None:
                    for x in range(len(row)):
                        if (row[x])[0]==data_base:
                            print(row[x])
                if data_base == None:
                    print(errors.cannot_call_func('data_base.show.show_row()'))
            def show_lists(data_base=None):
                global lists
                if data_base != None:
                    for x in range(len(lists)):
                        if (lists[x])[0]==data_base:
                            print(lists[x])
                if data_base == None:
                    print(errors.cannot_call_func('data_base.show.show_lists'))
            def all_in_database(data_base=None):
                global data_bases, row, debug, sets, rows, type
                sets=[]
                rows=[]
                type=None
                if data_base != None:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            if (data_bases[i])[3] == 'list':
                                if debug==True:
                                    print('(System) List found')
                                    type='list'
                                    break
                            if (data_bases[i])[3] == 'column_row':
                                if debug==True:
                                    print('Data base found!')
                                    type='column_row'
                                    break
                    for x in range(len((data_bases[i])[4])):
                        sets.append(((data_bases[i])[4])[x])
                    for n in range(len(row)):
                        if (row[n])[0] == data_base:
                            rows.append((row[n])[1])
                    print(sets)
                    for i in range(len(rows)):
                        print(rows[i])
                if data_base == None:
                    print(errors.cannot_call_func('data_base.show.all()'))
            def all_data_bases():
                global data_bases
                print('Known databases:')
                for i in range(len(data_bases)):
                    print('  ',(data_bases[i])[0])
            def info(data_base=None):
                global data_bases, type
                if data_base != None:
                    type=None
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            if (data_bases[i])[3] == 'list':
                                if debug==True:
                                    print('(System) List found')
                                    type='list'
                                    break
                            if (data_bases[i])[3] == 'column_row':
                                if debug==True:
                                    print('Data base found!')
                                    type='column_row'
                                    break
                    if type == "column_row":
                        print('Database Name:',(data_bases[i])[0])
                        print('Database status:',(data_bases[i])[1])
                        print('Database access:',(data_bases[i])[2])
                        print('Database type:',(data_bases[i])[3])
                    if type == "list":
                        print('Database Name:',(data_bases[i])[0])
                        print('Database status:',(data_bases[i])[1])
                        print('Database access:',(data_bases[i])[2])
                        print('Database type:',(data_bases[i])[3])
        class remove:
            def all():
                global data_bases, row, lists
                data_bases=[]
                lists=[]
                row=[]
            def one_set(data_base=None):
                global data_bases, row, lists
                if data_base != None:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            data_bases.pop(i)
                            break
                    for x in range(len(row)):
                        try:
                            if (row[x-1])[0]==data_base:
                                row.pop(x-1)
                        except IndexError:
                            pass
                    for x in range(len(lists)):
                        try:
                            if (lists[x-1])[0]==data_base:
                                lists.pop(x-1)
                        except:
                            pass
                if data_base == None:
                    print(errors.cannot_call_func('data_base.remove.one()'))
            def reset_to_standard(reset_users=False):
                global data_bases, row, lists, allowed_types, allowed_users, data_bases_reset, row_reset, lists_reset, allowed_types_reset, allowed_users_reset, known_users, passwords, known_users_reset, passwords_reset, permissions, permissions_reset
                data_bases=data_bases_reset
                row=row_reset
                lists=lists_reset
                if reset_users==True:
                    allowed_types=allowed_types_reset
                    allowed_users=allowed_users_reset
                    known_users=known_users_reset
                    passwords=passwords_reset
                    permissions=permissions_reset
        class create:
            def database(data_base=None, status=True, type=None, owner='all', columns=None):
                if data_base != None and type != None:
                    if isinstance(owner, str) == True and isinstance(type, str) == True and isinstance(owner, str) == True and isinstance(status, bool) :
                        if columns==None or isinstance(columns, list) == True:
                            global data_bases
                            if type == "list":
                                data_bases.append([data_base, status, owner, 'list'])
                            if type == "column_row":
                                if columns==None:
                                    data_bases.append([data_base, status, owner, 'column_row', []])
                                if columns != None:
                                    data_bases.append([data_base, status, owner, 'column_row', columns])
                    if isinstance(status, bool) == False:
                        print(errors.not_bool(item='status'))
                    if columns != None and isinstance(columns, list) == False:
                        print(errors.not_list(item='columns'))
                    if isinstance(owner, str) == False:
                        print(errors.not_str(item='owner'))
                    if isinstance(data_base, str) == False:
                        print(errors.not_str(item='type'))
                    if isinstance(type, str) == False:
                        print(errors.not_str(item='data_base'))
                if data_base == None and type == None:
                    print(errors.cannot_call_func('data_base.create.datebase()'))
            def data_base(data_base=None, type=None):
                data_base.create.database(data_base=data_base, type=type)
                #Redirects to correct def
    class password_restrictions:
        def set_min_length(value=None):
            global min_length
            if value != None and isinstance(value, int) == True:
                min_length=value
            if isinstance(value, int) == False:
                print(errors.not_int(item='value'))
            if value == None:
                print(errors.cannot_call_func('password_restrictions.set_min_length()'))
        def set_max_length(value=None):
            global max_length
            if value != None and isinstance(value, int) == True:
                max_length=value
            if value == None:
                print(errors.cannot_call_func('password_restrictions.set_max_length()'))
        def cannot_contian():
            #Password cannot contain these
            pass
    class errors:
        def cannot_call_func(var):
            return '(Error) The function '+var+' that was called is missing 1 or more required variables.'
        def not_list(item=None):
            if item==None:
                return '(Error) A list was expected, but was not given.'
            if item != None:
                return '(Error) A list was expected, but was not given. Item: '+str(item)
        def user_not_found():
            return '(Error) The user specified was not found.'
        def not_str(item=None):
            if item==None:
                return '(Error) A string was expected, but was not given.'
            if item != None:
                return '(Error) A string was excepted, but was not given. Item: '+str(item)
        def user_exists():
            return('(Error) This user already exists.')
        def not_bool(item=None):
            if item==None:
                return '(Error) A bool was expected, but was not given.'
            if item != None:
                return '(Error) A bool was expected, but was not given. Item: '+str(item)
        def not_int(item=None):
            if item==None:
                return '(Error) A int was expected, but was not given.'
            if item != None:
                return '(Error) A int was expected, but was not given. Item: '+str(item)
    #Test bench
    #<--Indent to here
