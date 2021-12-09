data_bases=[['basic', True, 'all', 'column_row', ['name','id','gender']],['chance', True, 'all', 'list']]
#Name, Active status, owner, type, columns
row=[['basic',['Brandon','123456','Male']],['basic', ['Gertie','124551','Male']]]
#Side to side
#Data_base, items in row
lists=[['basic', ['money','today']]]
#Lists
#Data_base, items in list

#Authentication
known_users=['Admin']
passwords=[None]
#Passwords can be none. Restrictions can also be set.
permissions=['admin']

global_password=None #A password that can be used on anything. If none, then no global_password is allowed.
allowed_types=['column_row', 'list', 'grid']
allowed_users=['all', 'admin']
debug=True







#Reset ----(DO NOT TOUCH)----
data_bases_reset=[['basic', True, 'all', 'column_row', ['name','id','gender']],['chance', True, 'all', 'list']]
row_reset=[['basic',['Brandon','123456','Male']],['basic', ['Gertie','124551','Male']]]
lists_reset=[['basic', ['money','today']]]
allowed_types_reset=['column_row', 'list', 'grid']
allowed_users_reset=['all', 'admin']
known_users_reset=['Admin']
passwords_reset=[None]
permissions_reset=['admin']