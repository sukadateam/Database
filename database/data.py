data_bases=[['tools', True, 'all', 'column_row', ['name','id']], ['logs', True, 'all', 'list']]
#Name, Active status, owner, type, columns(if type == column_row)
row=[]
#Side to side
#Data_base, items in row
lists=[]
#Lists
#Data_base, items in list

#Authentication
known_users=['admin','brandon','abdullahi','tripp','teacher', 'student']
passwords=['admin','Hello','snake','solid','teacher','student']
#Passwords can be none. Restrictions can also be set.
permissions=['admin','admin','admin','admin','teacher', 'student']
active_users=[True, True, True, True, True, True]

#Current user logged in
user_logged=None
user_permission=None

#Others
allowed_types=['column_row', 'list']
allowed_users=['admin', 'student', 'teacher']
denied_inputs=['',' ',None]
denied_names=[]
min_length=5 #Min password length
max_length=8 #Max password length
debug=False
students=['brandon', 'jeff']
opto_data=[]
opto_row=[]
opto_lists=[]
