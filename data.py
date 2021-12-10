data_bases=[['basic', True, 'all', 'column_row', ['name','id','gender']],['chance', True, 'all', 'list']]
#Name, Active status, owner, type, columns
row=[['basic',['Brandon','123456','Male']],['basic', ['Gertie','124551','Male']], ['basic', ['Fluffy','124411','Trans']]]
#Side to side
#Data_base, items in row
lists=[['chance', ['money','today']]]
#Lists
#Data_base, items in list

#Authentication
known_users=['Admin','Mr.Plummer','Gertie']
passwords=[None,None,None]
#Passwords can be none. Restrictions can also be set.
permissions=['admin','all','tacobell']

#Current user logged in
user_logged=None
user_permission=None

global_password=None #A password that can be used on anything. If none, then no global_password is allowed.
allowed_types=['column_row', 'list', 'grid']
allowed_users=['all', 'admin']
min_length=5 #Min password length
max_length=8 #Max password length
debug=True
