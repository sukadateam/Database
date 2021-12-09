import sys
required_version='3.10.0'
if sys.version[0:len(required_version)] != required_version:
    print('Required python version:', required_version)
    print('Current python version:',sys.version[0:len(required_version)])
if sys.version[0:len(required_version)] == required_version:
    print('Program Version: 0.0.1')
    from data import *
    from cache import *
    class users:
        def create():
            pass
        def remove():
            pass
        def show_all():
            pass
        def change_permissions():
            pass
        def change_name():
            pass
        def change_password():
            pass
    class data_base:
        class edit:
            def add_item(column=None,data_base=None, item_to_add=None):
                if column != None and data_base != None and item_to_add != None:
                    pass
                if column == None or data_base == None or item_to_add == None:
                    print(errors.cannot_call_func('data_base.edit.add_item()'))
            def remove_item():
                pass
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
                    try:
                        for i in range(len(row)):
                            print(row[i])
                            if (row[i])[0]==data_base:
                                rows.append(row[i])
                                row.pop(i)
                    except:
                        pass
                    #for i in range(len(rows)):
                        #print('#'+str(i)+' : '+str(rows[i]))
                    print(row)

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
            def remove_column():
                pass
                #Goes through all lists for the column and changes it to equal None.
                #Must be column_row
        class empty:
            #Clear all info in 1 or more databases.
            def all():
                pass
            def one():
                pass
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
            def all_data_bases(help=False):
                global data_bases
                if help==True:
                    print('Shows all databases that are known.\n')
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
            def database(data_base=None):
                pass
            def data_base(data_base=None):
                data_base.create.database(data_base=None)
                #Redirects to correct def
    class password_restrictions:
        def set_min_length():
            pass
        def set_max_length():
            pass
        def cannot_contian():
            #Password cannot contain these
            pass
    class errors:
        def cannot_call_func(var):
            return '(Error) The function '+var+' that was called is missing 1 or more required variables.'
        def not_list():
            return '(Error) A list was expected, but was not given.'
    data_base.edit.remove_row(data_base='basic')