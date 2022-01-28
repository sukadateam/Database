data_bases=[]
#Name, Active status, owner, type, columns(if type == column_row)
row=[]
#Side to side
#Data_base, items in row
lists=[]
#Lists
#Data_base, items in list

#Authentication
known_users=[]
passwords=[]
#Passwords can be none. Restrictions can also be set.
permissions=[]
active_users=[True, True, True, True, True, True]

#Current user logged in
user_logged=None
user_permission=None

#Others
allowed_types=['column_row', 'list']
allowed_users=['admin', 'student', 'teacher', 'secret'] #Allowed Permissions
denied_inputs=['',' ',None]
denied_names=[]
debug=True
students=['brandon', 'jeff']
opto_data=[]
opto_row=[]
opto_lists=[]
