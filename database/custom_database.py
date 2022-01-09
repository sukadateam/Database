#Things to do next:
#Fix support issues with linux.
#Find a fix for path variable. May cause issues on some devices.
#Create support for macos.
#Create a python test file to test all functions.
from multiprocessing import Process as p
from multiprocessing.spawn import freeze_support
import sys, os
from pyAesCrypt import decryptFile, encryptFile
password=None
from settings import *
found=True
try:
    import directory
    import version
except:
    found=False
if found==False:
    print('Automatic setup in progess.')
    import get_directory
    import version_config
list1=[]
try:
    from history_desc import *
except:
    print('Could not find the required file: history_desc.py You may experience problems.')
print('This Project is hosted on github. github.com/sukadateam')
print('If problems occur, try to check if a new version exists.')
if sys.version[0:len(required_version)] != required_version:
    print('Required python version:', required_version)
    print('Current python version:', sys.version[0:len(required_version)])
if sys.version[0:len(required_version)] == required_version:
    from datetime import date
    today=date.today()
    d1 = today.strftime("%m/%d/%Y")
    alphabet='abcdefghijklmnopqrstuvwxyz'
    from settings import *
    import random, shutil
    try:
        from directory import path
        print('Set path:', path)
        os.chdir(path)
    except ModuleNotFoundError:
        print('custom_database is not setup. Please setup with .bat or .sh file to enable this program.')
        exit()
    try:
        if dont_load_save==False:
            from data_save import *
            import_type='data_save'
        if dont_load_save==True:
            from data import *
            import_type='data'
    except:
        try:
            from data import *
            import_type='data'
        except:
            pass
    if import_type=="data":
        print('Import type: Default')
    if import_type=="data_save":
        print('Import type: Save file')
    #On linux this import line may say could not import, but it will if the package is installed.
    import pyAesCrypt
    class inventory:
        def calc():
            #Gives a informed idea if items, how many are in the system, how many are currently being used, and how many are not being used.
            pass
        def display():
            #Displays the calculations.
            pass
    def check_settings():
        #Checks settings.py to make sure all settings are correct and will not cause a proplem.
        #If one or more items come back as a problem they will be listed,
        print('\nIncorrect settings: ')
        error_found=False
        if isinstance(do_not_remove, bool) != True:
            print('  do_not_remove')
            error_found=True
        if isinstance(fail_safe, bool) != True:
            print('  fail_safe')
            error_found=True
        if isinstance(required_version, str) != True:
            print('  required_version')
            error_found=True
        if isinstance(program_version, str) != True:
            print('  program_version')
            error_found=True
        if isinstance(drive_letter, str) != True:
            print('  drive_letter')
            error_found=True
        if isinstance(drive_name, str) != True:
            print('  drive_name')
            error_found=True
        if isinstance(system, str) != True:
            print('  system')
            error_found=True
        if isinstance(profanity_filter, bool) != True:
            print('  profanity_filter')
            error_found=True
        if isinstance(disable_filter_admin, bool) != True:
            print('  disable_filter_admin')
            error_found=True
        if isinstance(global_password, bool) != True:
            print('  global_password')
            error_found=True
        if isinstance(dont_load_save, bool) != True:
            print('  dont_load_save')
            error_found=True
        if isinstance(optimize_on_startup, bool) != True:
            print('  optimize_on_startup')
            error_found=True
        if isinstance(auto_history_record, bool) != True:
            print('  auto_history_record')
            error_found=True
        if isinstance(app_version_control, bool) != True:
            print('  app_version_control')
            error_found=True
        if isinstance(set_operating_system, bool) != True:
            print('  set_operating_system')
            error_found=True
        if isinstance(allow_windows_version, str) != True:
            print('  allow_windows_version')
            error_found=True
        if isinstance(skip_history_copy, bool) != True:
            print('  skip_history_copy')
            error_found=True
        if isinstance(auto_error_record, bool) != True:
            print('  auto_error_record')
            error_found=True
        if isinstance(assign_digit_forHistory, bool) != True:
            print('  assign_digit_forHistory')
            error_found=True
        if isinstance(allowed_digists_forHistory, int) != True:
            print('  allowed_digists_forHistory')
            error_found=True
        if isinstance(multi_process, bool) != True:
            print('  multi_process')
            error_found=True
        if isinstance(auto_filter_profanity, bool) != True:
            print('  auto_filter_profanity')
            error_found=True
        if isinstance(auto_filter_profanity_speedBoost, bool) != True:
            print('  auto_filter_profanity_speedBoost')
            error_found=True
        if isinstance(quit_ifIncorrect, bool) != True:
            print('  quit_ifIncorrect')
            error_found=True
        if error_found==False:
            print('  None')
        error_found1=False
        print('\nOthers:')
        list2=['7', '8','10','11']
        found=True
        for i in range(len(list2)):
            if allow_windows_version != list2[i]:
                found=False
            if allow_windows_version == list2[i]:
                found=True
                break
        if found==False:
            print('  allow_windows_version must be set to 7, 8, 10, or 11')
            error_found1=True
        if len(drive_letter)>1 or len(drive_letter)<1:
            print('  drive_letter must be 1 character')
            error_found1=True
        if allowed_digists_forHistory>30 or allowed_digists_forHistory<1:
            print('  allowed_digists_forHistory can only be upto 30 and no less than 1.')
            error_found1=True
        if error_found1==False:
            print('  None')
        if quit_ifIncorrect == True:
            if error_found==True or error_found1==True:
                exit()
    class profanityFilter:
        def disable():
            #Redirect
            profanityFilter.deactivate()
        def enable():
            #Redirect
            profanityFilter.activate()
        def activate():
            #Enables profanity filter
            global profanity_filter
            profanity_filter=True
        def deactivate():
            #Disables profanity filter
            global profanity_filter
            profanity_filter=False
        def setup():
            #Called on startup if enabled to setup the filter.
            global profanity_filter, auto_filter_profanity_speedBoost, list1
            #Check profanity.txt to see if input matches.
            if profanity_filter==True and auto_filter_profanity_speedBoost==False:
                with open("profanity.txt", encoding="ascii") as file_in:
                    for line in file_in:
                        list1.append(line.replace('\n',''))
            if profanity_filter==True and auto_filter_profanity_speedBoost==True:
                with open("shorter_profanity.txt") as file_in:
                    for line in file_in:
                        list1.append(line.replace('\n',''))
        def filter(var):
            #Give this function a string to check.
            #If a match is found 1 is returned. If none, 0 is returned.
            global list1
            if isinstance(var, str) == True:
                for i in range(len(list1)):
                    if str(var) == list1[i]:
                        return 1
                return 0
            else:
                for i in range(90):
                    print()
                print('(Error) Unknown Class. This will not be recorded. Input must be a string.')
    def encrypt_check():
        #Check to see if save file is encrypted.
        #Return 1 if encrypted, if not return 0.
        try:
            open('data_save.aes', 'r')
            return 1
        except:
            return 0
    class history:
        def add_description(code=None, description=None):
            if code != None and description != None:
                if isinstance(code, str)==True and isinstance(description, str)==True:
                    pass
        def check_forDuplicate(user, usage):
            #Prevents duplicate items to be recorded.
            global debug
            file=open('history.txt').read()
            a=len(file)
            a3=len(user)+len(usage)+2
            last_object=(file[a-a3: a])
            current_object=(usage+': '+user)
            if debug==True:
                print('Current:', current_object)
                print('Last:', last_object)
            if str(current_object)==str(last_object):
                if debug==True:
                    print('Match Found. Skipping write to history file.')
                return 1
            else:
                if debug==True:
                    print('No match found. Writing to history file.')
                return 0
        def assign_letter():
            #Not in use yet.
            global allowed_digists_forHistory
            count=int(count)
            a=''
            for i in range(allowed_digists_forHistory-len(str(count))):
                a+='0'
            a+=str(count)
            count+=1
            return a
        def clear():
            #Clears history file
            history.delete()
            history.create()
        def delete():
            #Removes history file
            os.remove('history.txt')
        def create():
            #Creates history file
            global d1
            ah=open('history.txt','w')
            ah.write('File created: '+d1)
            ah.close()
        def create_history(user, usage, manual_record=False):
            #Adds items to history file
            if auto_history_record==True or manual_record==True:
                if user==None:
                    user='Null'
                global d1
                try:
                    open('history.txt','r')
                except:
                    history.create()
                allow=True
                if skip_history_copy==True:
                    if history.check_forDuplicate(user=user, usage=usage) == 1:
                        allow=False
                if allow==True:
                    ah=open('history.txt','a')
                    ah.write('\n('+d1+')'+' '+str(usage)+': '+str(user))
                    ah.close()
    class optimize():
        def determ(letter=None, set=None, test=False):
            for i in range(26):
                if letter == alphabet[i]:
                    if test == False:
                        return 0
                    if test == True:
                        a=globals()[set]
                        a=a[i]
                        return a
        def run(save_optimizations=True):
            global data_bases, opto_data, opto_row, row, opto_lists, lists, debug, user_permission, user_logged
            history.create_history(None, 'Optimize')
            try:
                user_logged=None
                user_permission=None
                opto_data=optimize.count(var='data_bases')
                data_bases=optimize.list_org(var='data_bases')
                opto_row=optimize.count(var='row')
                row=optimize.list_org(var='row')
                opto_lists=optimize.count(var='lists')
                lists=optimize.list_org(var='lists')
                if debug == True:
                    print('Save file optimized.')
            except:
                if debug == True:
                    print('An error occured.')
            if save_optimizations==True:
                print('All data saved.')
                save.all()
        def count(var):
            opto=[]
            alphabet='abcdefghijklmnopqrstuvwxyz '
            for i in range(26):
                opto.append(0)
            count=0
            letter=''
            rcount=len(globals()[var])
            while letter != " ":
                letter = alphabet[count]
                for i in range(rcount):
                    if (((globals()[var])[i])[0])[0] == letter:
                        opto[count]+=1
                count+=1
            return opto
        def list_org(var):
            org=[]
            max=len(globals()[var])
            current=0
            alphabet='abcdefghijklmnopqrstuvwxyz '
            count=0
            while current < max:
                for i in range(max):
                    if (((globals()[var])[i])[0])[0] == alphabet[count]:
                        org.append((globals()[var])[i])
                        current+=1
                count+=1
            return org
    def check_data():
        #Also remove data sets that are not apart of a database.
        print('\n')
        global import_type
        check=[False, False]
        #Check data_bases var
        for i in range(len(data_bases)):
            try:
                if (data_bases[i])[0] != None:
                    if (data_bases[i])[1] != None:
                        if (data_bases[i])[2] != None:
                            if (data_bases[i])[3] == "column_row":
                                if isinstance((data_bases[i])[4], list) == True:
                                    check[0]=True
                            if (data_bases[i])[3] == "list":
                                check[0]=True
            except:
                check[0]=False
                break
        #Write down all current databases.
        known_databases=[]
        for i in range(len(data_bases)):
            known_databases.append((data_bases[i])[0])
        #Row check. Check to see if database and list are present for each, and if set databases doesn't exist.
        for i in range(len(row)):
            try:
                if (row[i])[0] != None:
                    if (row[i])[0] in known_databases:
                        if isinstance((row[i])[1], list) == True:
                            check[1]=True
            except:
                check[1]=False
                break
        print('True = Working | False = Broken')
        print('Database Check:',check[0])
        print('Rows Check:',check[1])
    def list_count(data_base):
        for i in range(len(data_bases)):
            if (data_bases[i])[0]==data_base:
                return len((data_bases[i])[4])
    def check(var):
        global denied_inputs
        for i in range(len(denied_inputs)):
            if var==denied_inputs[i]:
                return True
        if var not in denied_inputs:
            return False
    def exit():
        print('Application Closed')
        sys.exit()
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
        def try_password(password):
            if system=='windows':
                global drive_letter
                try:
                    pyAesCrypt.decryptFile(drive_letter+':/hash.aes',drive_letter+':/hash.txt',password)
                    pyAesCrypt.encryptFile(drive_letter+':/hash.txt',drive_letter+':/hash.aes',password)
                    return 1
                except:
                    return 0
            else:
                try:
                    pyAesCrypt.decryptFile('hash.aes','hash.txt',password)
                    pyAesCrypt.encryptFile('hash.txt','hash.aes',password)
                    return 1
                except:
                    return 0
        def get_other_hash(password):
            if system=="windows":
                try:
                    decrypt.hash(password)
                    global drive_letter
                    file=open(drive_letter+':/hash_other.txt','r').read()
                    os.remove(drive_letter+':/hash_other.txt')
                    return file
                except ValueError:
                    print('Incorrect Password!')
            else:
                try:
                    decrypt.hash(password)
                    file=open('hash_other.txt','r').read()
                    os.remove('hash_other.txt')
                except ValueError:
                    print('Incorrect Password')
        def get_hash():
            try:
                password = get.password()
                decrypt.hash(password)
                global drive_letter
                if system=='windows':
                    file=open(drive_letter+':/hash.txt','r').read()
                    os.remove(drive_letter+':/hash.txt')
                else:
                    file=open('hash.txt','r')
                    os.remove('hash.txt')
                return file
            except ValueError:
                global global_password
                if global_password==True:
                    get.get_other_hash(password)
        def new_hash(passw=None):
            get.random_hash()
            get.encrypt_hash(passw)
            password=None
        def encrypt_hash(passw=None, other=False):
            global drive_letter, global_password
            if passw != None:
                password=passw
            if passw == None:
                password=get.password()
            if other == False:
                if system=='windows':
                    pyAesCrypt.encryptFile(drive_letter+':/hash.txt', drive_letter+':/hash.aes', password)
                    os.remove(drive_letter+':/hash.txt')
                else:
                    pyAesCrypt.encryptFile('hash.txt','hash.aes',password)
                    os.remove('hash.txt')
            if other == True:
                if global_password==True:
                    if system=="windows":
                        pyAesCrypt.encryptFile(drive_letter+':/hash_other.txt', drive_letter+':/hash_other.aes', password)
                        os.remove(drive_letter+':/hash_other.txt')
                    else:
                        pyAesCrypt.encryptFile('hash_other.txt', 'hash_other.aes', password)
                        os.remove('hash_other.txt')
        def password():
            return input('Password: ')
        def random_hash(length=100, normal=True):
            if isinstance(length, int) == False:
                print(errors.not_int())
            if isinstance(length, int) == True:
                ah=''
                for i in range(length): 
                    ah+=random.choice('ajfygweuoichwgbuieucr73rwecb638781417983b 623v9923 r t72344y 23uc3u2b4n9832 4b2c794y 237bc2423nc482b3c427 rfgshdfuw38263872guihfef86w4t878whryfeg48tg34hf7w')
                if normal==True: 
                    global drive_letter
                    if system=="windows": file=open(drive_letter+':/hash.txt','w')
                    else: file=open('hash.txt', 'w')
                    file.write(ah)
                    file.close()
                    if system=="windows": file=open(drive_letter+':/hash_other.txt','w')
                    else: file=open('hash_other.txt','w')
                    file.write(ah)
                    file.close()
                if normal==False:
                    return ah
    class decrypt:
        def hash(password):
            global drive_letter
            try:
                if system=='windows':
                    pyAesCrypt.decryptFile(drive_letter+':/hash.aes',drive_letter+':/hash.txt',password)
                    return open(drive_letter+':/hash.txt','r').read()
                else:
                    pyAesCrypt.decryptFile('hash.aes','hash.txt',password)
                    return open('hash.txt','r').read()
            except:
                if system=="windows":
                    pyAesCrypt.decryptFile(drive_letter+':/hash_other.aes',drive_letter+':/hash_other.txt',password)
                    return open(drive_letter+':/hash_other.txt','r').read()
                else:
                    pyAesCrypt.decryptFile('hash_other.aes','hash_other.txt',password)
                    return open('hash_other.txt','r').read()
        def history(password):
            try:
                pyAesCrypt.decryptFile('history.aes','history.txt',password)
                os.remove('history.aes')
            except:
                pass
        def data(password):
            try:
                pyAesCrypt.decryptFile('data_save.aes','data_save.py',password)
                os.remove('data_save.aes')
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
                decrypt.history(d_password)
            except ValueError:
                print('Wrong password.')
                return 1
            try:
                global drive_letter
                if system=="windows": os.remove(drive_letter+':/hash.txt')
                else: os.remove('hash.txt')
            except:
                pass
            try:
                if system=="windows": os.remove(drive_letter+':/hash_other.txt')
                else: os.remove('hash_other.txt')
            except:
                pass
            #decrypt.cache(d_password)
            #decrypt.opt(d_password)
    class encrypt:
        def history(password):
            global fail_safe
            failed=False
            if fail_safe==True:
                try:
                    open('history.aes','r')
                    print('Existing file found. Cannot encrypt.')
                    failed=True
                except:
                    pass
                try:
                    open('history.txt','r')
                except:
                    failed=True
            if failed == False:
                global do_not_remove
                pyAesCrypt.encryptFile('history.txt','history.aes',password)
                if do_not_remove==False:
                    os.remove('history.txt')
        def data(password):
            global fail_safe
            failed=False
            if fail_safe==True:
                try:
                    open('data_save.aes','r')
                    print('Existing file found. Cannot encrypt.')
                    failed=True
                except:
                    pass
                try:
                    open('data_save.py','r')
                except:
                    failed=True
            if failed == False:
                global do_not_remove
                pyAesCrypt.encryptFile('data_save.py','data_save.aes',password)
                if do_not_remove==False:
                    os.remove('data_save.py')
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
            try:
                d_password=decrypt.hash(password)
                #encrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
                encrypt.data(d_password)
                encrypt.history(d_password)
                #encrypt.cache(d_password)
                #encrypt.opt(d_password)
                global drive_letter
                try:
                    os.remove(drive_letter+':/hash.txt')
                except:
                    pass
                try:
                    os.remove(drive_letter+':/hash_other.txt')
                except:
                    pass
            except ValueError:
                print('Wrong Password.')
                return 1
    class save:
        def all():
            history.create_history(None, 'Save')
            from vars_to_save import list
            file=open('data_save.py','w')
            for i in range(len(list)):
                file.write(list[i]+'='+str(globals()[list[i]])+'\n')
            file.write('\n')
            file.close()
            if advanced_history==True:
                file=open('history_desc.py', 'w')
                file.write('history_id='+str(history_id))
                file.write('\nhistory_description='+str(history_description))
                file.write('\ncount='+str(count))
    class clear:
        def normal():
            for i in range(100):
                print('')
    class check_type:
        def data_format(data_base=None):
            num=check(data_base)
            #Call to return data_base type.
            if num == False:
                global data_bases
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        return (data_bases[i])[3]
            if num == True:
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
            num=check(user)
            #Disables a user
            if num == False:
                global known_users, active_users
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Disable user')
                        active_users[i]=False
            if num == True:
                print(errors.cannot_call_func('users.disable()'))
        def enable(user=None):
            num=check(user)
            #Enables a user
            if num == False:
                global known_users, active_users
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Enable user')
                        active_users[i]=True
            if num == True:
                print(errors.cannot_call_func('users.disable()'))
        def create(new_user=None, new_password=None, new_permission=None):
            global known_users, passwords, permissions
            num1=check(new_user)
            num2=check(new_password)
            try:
                new_user=new_user.lower()
                new_permission=new_permission.lower()
            except:
                pass
            if new_permission not in allowed_users:
                print(errors.incorrect_perm())
            if num1 == False and num2 == False and new_permission in allowed_users:
                skip=False
                for i in range(len(known_users)):
                    if known_users[i]==new_user:
                        skip=True
                        print(errors.user_exists())
                if skip == False:
                    if isinstance(new_user, str) == True:
                        if isinstance(new_password, str) == True:
                            if isinstance(new_permission, str) == True or new_permission==None:
                                history.create_history(new_user, 'Created user')
                                known_users.append(new_user)
                                passwords.append(new_password)
                                permissions.append(new_permission)
                                active_users.append(True)
                    if isinstance(new_user, str) == False:
                        print('new_user must be str')
                    if isinstance(new_permission, str) == False:
                        print('new_permission must be str')
                    if isinstance(new_permission, str) == False and new_permission != None:
                        print('new_password must be str or None') 
            if num1 == True or num2 == True:
                print(errors.cannot_call_func('users.create()'))
        def remove(user=None):
            num=check(user)
            if num == False:
                user=user.lower()
                found=False
                global known_users, passwords, permissions
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Removed user')
                        known_users.pop(i)
                        passwords.pop(i)
                        permissions.pop(i)
                        active_users.pop(i)
                        found=True
                        break
                if found==False:
                    print(errors.user_not_found())
            if num == True:
                print(errors.cannot_call_func('users.remove()'))
        def show_all():
            global known_users
            for i in range(len(known_users)):
                print('User: '+known_users[i])
                print('Permission: '+permissions[i])
        def change_permissions(user=None, new_permission=None):
            num1=check(user)
            num2=check(new_permission)
            if num1 == False and num2 == False:
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Change permission')
                        permissions[i]=new_permission
            if num1 == True or num2 == True:
                print(errors.cannot_call_func('users.change_permissions()'))
        def change_name(user=None, new_name=None):
            num1=check(user)
            num2=check(new_name)
            if num1 == False and num2 == False:
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user+' to '+new_name, 'Change name')
                        known_users[i]=new_name
            if num1 == True or num2 == True:
                print(errors.cannot_call_func('users.change_name()'))
        def change_password(user=None, new_password=None):
            global passwords
            num=check(user)
            if num == False:
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Change password')
                        passwords[i]=new_password
            if num == True:
                print(errors.cannot_call_func('users.change_password()'))
        def return_users():
            global known_users
            return known_users
        def login_request(user=None, password=None):
            #Will return True if credentials are correct, if not will return False
            user=str(user)
            password=str(password)
            if user != None and password != None or password==None:
                global known_users, passwords, user_logged, user_permission, profanity_filter, disable_filter_admin
                if isinstance(user, str)==True and isinstance(password, str)==True or password == None:
                    if user in known_users:
                        for i in range(len(known_users)):
                            if known_users[i]==user:
                                if passwords[i] != password:
                                    print('Password is incorrect.')
                                if passwords[i]==password:
                                    if active_users[i]==True:
                                        user_logged=known_users[i]
                                        user_permission=permissions[i]
                                        if user_permission=="admin":
                                            if disable_filter_admin==True:
                                                profanity_filter=False
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
            global user_logged, user_permission, profanity_filter, disable_filter_admin
            if user_permission=="admin":
                if disable_filter_admin==True:
                    profanity_filter=True
            user_permission=None
            user_logged=None
        def return_login_cred():
            global user_logged, user_permission
            return user_logged, user_permission
    class data_base:
        class edit:
            def search_rows(data_base=None, id=None):
                if isinstance(data_base, str) == True and isinstance(id, str) == True:
                    for i in range(len(row)):
                        if (row[i])[0] == data_base:
                            if ((row[i])[1])[1]==id:
                                return 1
                    return 0
            def check_owner(data_base=None, user_perm=None):
                #Returns 1 is owner matches the database.
                if isinstance(data_base, str) == True and isinstance(user_perm, str) == True:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[2] == user_perm:
                            return 1
                    return 0
            def add_row_term():
                data=input('Database: ')
                bra=False
                try:
                    for i in range(len(data_bases)):
                        if bra == True:
                            break
                        if (data_bases[i])[0]==data:
                            aa=input('Enter row/list with spaces between each: ')
                    data_base.edit.add_row(data_base=data, new_row=aa)
                except:
                    pass
            def add_item(data_base=None, item_to_add=None, create_if_notExist=True):
                history.create_history(item_to_add, 'Add item')
                #Used for the list types.
                global data_bases, lists
                num1=check(data_base)
                num2=check(item_to_add)
                letter_spot=optimize.determ(letter=data_base[0])
                if num1 == False and num2 == False:
                    if create_if_notExist == True:
                        failed=True
                        for i in range(len(lists)):
                            if (lists[i])[0] == data_base:
                                failed=False
                                break
                            failed=True
                        if failed==True:
                            lists.append([data_base,[]])
                    data_base=data_base.lower()
                    for i in range(len(data_bases)):
                        if (data_bases[i+letter_spot])[0] == data_base:
                            print(1)
                            if (data_bases[i+letter_spot])[3]=="list":
                                print(2)
                                for x in range(len(lists)):
                                    if (lists[x])[0]==data_base:
                                        print(3)
                                        (lists[x])[1].append(item_to_add)
                                        print(lists)
                                        break
                if num1==True or num2==True:
                    print(errors.cannot_call_func('data_base.edit.add_item()'))
            def remove_item(data_base=None, item_to_remove=None):
                history.create_history(item_to_remove, 'Remove item')
                #Used for the list types.
                num1=check(data_base)
                num2=check(item_to_remove)
                global data_bases, lists
                letter_spot=optimize.determ(letter=data_base[0], set='opto_data')
                if num1 == False and num2 == False:
                    data_base=data_base.lower()
                    for i in range(len(data_bases)):
                        if (data_bases[i+letter_spot])[0]==data_base:
                            if (data_bases[i+letter_spot])[3]=="list":
                                for x in range(len(lists)):
                                    if (lists[x])[0]==data_base:
                                        try:
                                            (lists[x])[1].remove(item_to_remove)
                                            print(lists)
                                        except:
                                           pass
                                        break
                if num1 == True or num2 == True:
                    print(errors.cannot_call_func('data_base.edit.remove_item()'))
            def add_row(data_base=None, new_row=None, split=True):
                history.create_history(new_row, 'Add row')
                #You can add as many objects to a row as you please, but it may not fit in your assinged constraints. No problems will occur though.
                if split==True:
                    new_row=new_row.split()
                #print(new_row)
                num1=check(data_base)
                num2=check(new_row)
                if num1 == False and num2 == False:
                    data_base=data_base.lower()
                    if isinstance(new_row, list) == True:
                        row.append([data_base,new_row])
                        #print("Added new row!")
                    if isinstance(new_row, list) == False:
                        print(errors.not_list())
                if num1 == True or num2 == True:
                    print(errors.cannot_call_func('data_base.edit.add_row()'))
            def remove_row(data_base=None):
                num1=check(data_base)
                if num1 == False:
                    data_base=data_base.lower()
                    history.create_history(data_base, 'Remove row')
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
                if num1 == True:
                    print(errors.cannot_call_func('data_base.edit.remove_row()'))
                #Must be column_row
            def add_column(data_base=None, column_name=None):
                history.create_history(column_name, 'Add column')
                letter_spot=optimize.determ(letter=data_base[0], set='opto_data')
                num1=check(data_base)
                num2=check(column_name)
                global debug, data_bases
                found=False
                for i in range(len(data_bases)):
                    if (data_bases[i])[0] == data_base:
                        found=True
                        break
                if found==False:
                    print(errors.database_does_not_exist())
                if num1 == False and num2 == False and found==True:
                    data_base=data_base.lower()
                    if debug==True:
                        print("Adding column at",data_base,"with name",column_name.lower())
                    for i in range(len(data_bases)):
                        if (data_bases[i+letter_spot])[0] == data_base:
                            if (data_bases[i+letter_spot])[3]=="column_row":
                                (data_bases[i+letter_spot])[4].append(column_name.lower())
                if num1 == True or num2 == True:
                    print(errors.cannot_call_func('data_base.edit.add_column()'))
            def remove_column(data_base=None, column=None, remove_row=False):
                try:
                    history.create_history(column, 'Remove Column')
                    num1=check(data_base)
                    num2=check(column)
                    found=False
                    letter_spot=optimize.determ(letter=data_base[0])
                    if num1 == False and num2 == False:
                        data_base=data_base.lower()
                        global data_bases, debug, row
                        for i in range(len(data_bases)):
                            if (data_bases[i+letter_spot])[0]==data_base:
                                if debug==True:
                                    print('Database Found!')
                                found=True
                                if (data_bases[i+letter_spot])[3] == "column_row":
                                    if debug==True:
                                        print("Correct data_base type!")
                                    if column in (data_bases[i+letter_spot])[4]:
                                        print("Removed: "+str(column))
                                        a=len((data_bases[i+letter_spot])[4])
                                        for e in range(a):
                                            if ((data_bases[i+letter_spot])[4])[e] == column:
                                                print(e)
                                                break
                                        (data_bases[i+letter_spot])[4].remove(column)
                                        print(data_bases[i+letter_spot])
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
                    if num1 == True or num2 == True:
                        print(errors.cannot_call_func('data_base.edit.remove_column()'))
                    if found==False and data_base != None:
                        print(errors.database_does_not_exist())
                except:
                    pass
                #Goes through all lists for the column and changes it to equal None.
                #Must be column_row
            #Used for my auto_motive app.
            class app:
                def remove_row(data_base=None, name=None):
                    if isinstance(name, str) == True and isinstance(data_base, str) == True:
                        global row
                        for i in range(len(row)):
                            if (row[i])[0] == data_base:
                                if ((row[i])[1])[0] == name:
                                    row.pop(i)
                                    break
                    else:
                        print(errors.not_str())
                def remove_item(data_base=None, barcode=None):
                    if isinstance(data_base, str) == True and isinstance(barcode, str) == True:
                        print('Got here')
                        global lists
                        for i in range(len(lists)):
                            if (lists[i])[0]==data_base:
                                for x in range(len((lists[i])[1])):
                                    if (((lists[i])[1])[x])[0]==barcode:
                                        ((lists[i])[1]).pop(x)
                    else:
                        print(errors.not_str())
                def show_tools(data_base=None):
                    if isinstance(data_base, str) == True:
                        for i in range(len(row)):
                            print('Item:',((row[i])[1])[0],' | Serial:',((row[i])[1])[1])
        class empty:
            def fast_one(database):
                if multi_process==True:
                    a= p(target=data_base.empty.one(database, recall=True))
                    a.start()
                    a.join()
                    freeze_support()
            #Clear all info in 1 or more databases.
            def all():
                history.create_history(None, 'Reset all databases')
                global lists, row
                lists=[]
                row=[]
            def one(data_base=None, recall=False):
                if multi_process==True:
                    data_base.empty.fast_one(data_base)
                else:
                    recall=False
                if recall==False:
                    num1=check(data_base)
                    if num1 == False:
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
                    if num1 == True:
                        print(errors.cannot_call_func('data_base.empty.one()'))
        class show:
            def show_column(data_base=None):
                num=check(data_base)
                if num == False:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            if (data_bases[i])[3]=="column_row":
                                print((data_bases[i])[4])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_column()'))
            def show_row(data_base=None):
                num=check(data_base)
                #Must be column_row type
                global row
                if num == False:
                    for x in range(len(row)):
                        if (row[x])[0]==data_base:
                            print((row[x])[1])
                print('Complete')
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_row()'))
            def show_lists(data_base=None):
                num=check(data_base)
                global lists
                if num == False:
                    for x in range(len(lists)):
                        if (lists[x])[0]==data_base:
                            print(lists[x])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_lists'))
            def all_in_database(database=None):
                num=check(database)
                global data_bases, row, debug, sets, rows, type
                sets=[]
                rows=[]
                type=None
                if num == False:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == database:
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
                        if multi_process==True:
                            a= p(target=data_base.show.show_row(data_base=database))
                            a.start()
                            a.join()
                            freeze_support()
                        if multi_process==False:
                            for x in range(len((data_bases[i])[4])):
                                sets.append(((data_bases[i])[4])[x])
                            for n in range(len(row)):
                                if (row[n])[0] == database:
                                    rows.append((row[n])[1])
                            print(sets)
                            for i in range(len(rows)):
                                print(rows[i])
                    if type == "list":
                        for i in range(len(lists)):
                            if (lists[i])[0]==database:
                                print((lists[i])[1])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.all()'))
            def all_data_bases():
                global data_bases
                print('Known databases:')
                for i in range(len(data_bases)):
                    print('  ',(data_bases[i])[0])
            def info(data_base=None):
                num=check(data_base)
                global data_bases, type
                if num == False:
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
                if num == True:
                    print(errors.cannot_call_func('data_base.show.info()'))
        class remove:
            def all():
                history.create_history(None, 'Remove All')
                global data_bases, row, lists
                data_bases=[]
                lists=[]
                row=[]
            def one_set(data_base=None):
                history.create_history(None, 'Remove One Set')
                num=check(data_base)
                global data_bases, row, lists
                if num == False:
                    found=False
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0] == data_base:
                            data_bases.pop(i)
                            found=True
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
                if found == False and num == False:
                    print(errors.database_does_not_exist())
                if num == True:
                    print(errors.cannot_call_func('data_base.remove.one()'))
            def reset_to_standard():
                history.create_history(None, 'Reset to Standard')
                try:
                    os.remove('data_save.py')
                except:
                    pass
        class create:
            def database(data_base=None, status=True, type=None, owner='all', columns=None):
                history.create_history(data_base, 'Create Database')
                found1=False
                found2=False
                found3=False
                print(data_base)
                #Check to see if database already exists.
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        print('That database already exists.')
                        found1=True
                        break
                if type not in allowed_types:
                    print('An incorrect data type has been entered.')
                    found2=False
                if type in allowed_types:
                    found2=True
                for i in range(len(data_base)):
                    if data_base[i] in alphabet:
                        found3=True
                    if data_base[i] not in alphabet:
                        found3=False
                        print('Database name can only consist of lowercase letters.')
                        break
                #If database doesn't exist continue on creating it.
                if found3 == True and found2 == True and found1 == False:
                    print('Database created!')
                    num1=check(data_base)
                    num2=check(type)
                    if num1 == False and num2 == False:
                        if isinstance(owner, str) == True and isinstance(type, str) == True and isinstance(owner, str) == True and isinstance(status, bool) :
                            if columns==None or isinstance(columns, list) == True:
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
                    if num1 == True and num2 == True:
                        print(errors.cannot_call_func('data_base.create.datebase()'))
    class password_restrictions:
        def set_min_length(value=None):
            history.create_history(str(value), 'Set min length')
            global min_length
            num=check(value)
            if num==False and isinstance(value, int) == True:
                min_length=value
            if isinstance(value, int) == False:
                print(errors.not_int(item='value'))
            if num == True:
                print(errors.cannot_call_func('password_restrictions.set_min_length()'))
        def set_max_length(value=None):
            history.create_history(str(value), 'Set max length')
            global max_length
            num=check(value)
            if num == False and isinstance(value, int) == True:
                max_length=value
            if num == True:
                print(errors.cannot_call_func('password_restrictions.set_max_length()'))
    class errors:
        def database_does_not_exist():
            history.create_history('database_does_not_exist', 'Error', manual_record=auto_error_record)
            return '(Error) Database requested could not be found.'
        def cannot_call_func(var):
            history.create_history('cannot_call_func', 'Error', manual_record=auto_error_record)
            return '(Error) The function '+var+' that was called is missing 1 or more required variables.'
        def not_list(item=None):
            history.create_history('not_list', 'Error', manual_record=auto_error_record)
            if item==None:
                return '(Error) A list was expected, but was not given.'
            if item != None:
                return '(Error) A list was expected, but was not given. Item: '+str(item)
        def user_not_found():
            history.create_history('user_not_found', 'Error', manual_record=auto_error_record)
            return '(Error) The user specified was not found.'
        def not_str(item=None):
            history.create_history('not_str', 'Error', manual_record=auto_error_record)
            if item==None:
                return '(Error) A string was expected, but was not given.'
            if item != None:
                return '(Error) A string was excepted, but was not given. Item: '+str(item)
        def user_exists():
            history.create_history('user_exists', 'Error', manual_record=auto_error_record)
            return('(Error) This user already exists.')
        def not_bool(item=None):
            history.create_history('not_bool', 'Error', manual_record=auto_error_record)
            if item==None:
                return '(Error) A bool was expected, but was not given.'
            if item != None:
                return '(Error) A bool was expected, but was not given. Item: '+str(item)
        def not_int(item=None):
            history.create_history('not_int', 'Error', manual_record=auto_error_record)
            if item==None:
                return '(Error) A int was expected, but was not given.'
            if item != None:
                return '(Error) A int was expected, but was not given. Item: '+str(item)
        def incorrect_perm():
            history.create_history('incorrect_perm','Error', manual_record=auto_error_record)
            return '(Error) The permission requested is not allowed.'
    if profanity_filter==True:
        profanityFilter.setup()
    if allow_windows_version == "11":
        allow_windows_version="10"
        #Windows 11 still thinks it's windows 10. I know it's weird.
    if optimize_on_startup==True:
        optimize.run()
        #Optmize on startup if setting is set to True.
    if app_version_control==True:
        #Checks what version the app was setup at.
        from version import setup_version
        if program_version != setup_version:
            try:
                open('history.txt','r')
            except:
                history.create()
            ah=open('history.txt','a')
            ah.write('\n('+d1+')'+' Program Version Control: Incorrect Version')
            ah.close()
            print('(Error) This program was setup on a different version.\nTo disable this prompt goto settings and set app_version_control to False.')
            exit()
    if system != 'windows' and system != "macos" and system != "linux":
        print('Invalid setting. system=')
        history.create_history(usage='Invalid Setting', user='system=Error()')
    if set_operating_system==True:
        from sys import platform
        if platform == "linux" or platform == "linux2":
            print('OS: Linux Distro.')
            #Linux
            if system != "linux":
                print('Incorrect OS')
                history.create_history(usage='Operating System Exception', user='linux')
                exit()
        elif platform == "darwin":
            print('OS: Mac OS')
            # OS X
            if system != "macos":
                print('Incorrect OS')
                history.create_history(usage='Operating System Exception', user='macos')
                exit()
        elif platform == "win32":
            print('OS: Windows')
            # Windows...
            if system != "windows":
                print('Incorrect OS')
                history.create_history(usage='Operating System Exception', user='windows')
                exit() 
    check_settings()
    print('System Started Correctly!')
    #You must set a Normal level password
    #You can set a global password if need be. Basically a backup.
    #Test bench
    #<--Indent to here
    save.all()

    #Do not remove this!!!!!!
    if __name__ == '__main__':
        if multi_process==True:
            freeze_support()
