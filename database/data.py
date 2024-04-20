# Encryption does not occur inside this file. Only data stored in data_save.py is encrypted.

data_bases=[]
#Name, Active status, owner, type, columns(if type == column_row)
row=[]
#Side to side
#Data_base, items in row
lists=[]
#Lists
#Data_base, items in list

#Authentication
known_users=['admin', 'teacher', 'student']
passwords=['admin', 'teacher', 'student']
#Look at line 32 for allowed permissions. allowed_users=[]
permissions=['admin', 'teacher', 'student']
ids=[]
'''Please avoid labeling any vars as permissions, i've had issues with this. Isolated functions are okay.
\nSet Permissions by default:
- admin
- teacher
- student
'''
#True = Enabled, False = Disabled.
active_users=[True, True, True]

#Current user logged in
user_logged=None
user_permission=None

#Others
allowed_types=['column_row', 'list']
allowed_users=['admin', 'student', 'teacher', 'secret'] #Allowed Permissions
denied_inputs=['',' ',None]
denied_names=[]
debug=False
students=[['Mike', 123456, False], ['Turtle', 123456, False]]
#Name, 4-6 digit passcode, active_student. Might change var name to studentsLogincreds(list)
opto_data=[]
opto_row=[]
opto_lists=[]
side_tilt=200
#students=[['Mike', 123456, True]]
