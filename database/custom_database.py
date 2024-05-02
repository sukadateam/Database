# Importing standard libraries
import sys, os, zipfile, json, time, ctypes
from platform import python_version
from os import stat, remove, walk
from typing import Set
from venv import create
from io import StringIO, BytesIO
from ast import Bytes
from dis import show_code
from email.encoders import encode_7or8bit
from ftplib import error_reply
#from xmlrpc.client import FastMarshaller
from json import tool
from re import L
#from numpy import True_, int32
from pandas import *
from screeninfo import get_monitors
from zipfile import ZipFile
import platform
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from base64 import urlsafe_b64encode, urlsafe_b64decode

# Importing cryptographic libraries
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# Importing optional libraries
try:
    from html5lib import serialize
    from barcode import EAN13
    from barcode.writer import ImageWriter
    import qrcode
    import win32api
    import win32print
    from multiprocessing import Process
    from pyAesCrypt import decryptFile, encryptFile
except ImportError:
    pass

# Importing application-specific modules
try:
    from settings import *
except ImportError:
    print('Cannot find settings.py. This file is required for startup.')
    sys.exit()

try:
    import get_directory
except ImportError:
    print('Cannot find get_directory.py. This file is required for startup.')
    sys.exit()

try:
    import version_config
except ImportError:
    print('Cannot find version_config.py. This file is required for startup.')
    sys.exit()

try:
    from history_desc import *
except ImportError:
    print('Cannot find history_desc.py. This file is required for startup.')
    sys.exit()
# End of Importing application-specific modules

# Initializing variables
password=None
systemDetectedOperatingSystem=None
list1=[]
startupCount=time.time()
n = list(sys.argv)

# MEMORY BANKS ___ DO NOT ALTER!!
'''Used for functions that can't retain their own vars.'''
memory_hash=None
memory_Bank1=None
memory_Bank2=None
memory_Bank3=None # users.passwordCryption() For encrypting user data.
'''Primary/Global password'''
memory_Bank4=[] # Used on data_base data encryption. Stores [nonce, tag, key, db_identifier]
'''Database encryption'''
memory_Bank5=None # Used on hash storage.
'''Hash Storage'''
memory_Bank6=None # Shown at the end of the program. It's displayed to the user. The user must store this password safely.
"""Used inpart of hash verification."""
'''[nonce, tag, key, db_identifier]. Data is stored inside database. This is used to soley encrypt and decrypt data.'''
attemptsCounting=0 # Counts the amount of attemps to login. If it reaches a certain amount, the system will wipe.
# EO MEMORY BANKS (*)


# Print startup messages
if quiteStartup == False:
    print('This Project is hosted on github. github.com/sukadateam')
    print('If problems occur, try to check if a new version exists.')
    print('-or- Create/Mark An Issue On GitHub!\n\n')


# Get the current Python version
current_version = platform.python_version()

# Check if the current version is in the list of required versions
if current_version not in required_version:
    # If skip_pythonCheck is True or "-skipPythonCheck" is in the command line arguments, print a warning and continue
    if skip_pythonCheck or "-skipPythonCheck" in sys.argv:
        print(f"Warning: Untested Python version {current_version} identified.")
    # Otherwise, print an error message and exit
    else:
        print(f"Error: Python version {current_version} is not supported. Supported versions are as follows:")
        print("Current Recommended Verison:",required_version[len(required_version)-1]) # Prints last version in list.
        print('\n'.join(required_version))
        print('\nTo Disable this prompt you can either use:',
            '\n   1. Set Argument (-skipPythonCheck) On start up',
            '\n   2. Or Change Setting skip_pythonCheck to True')
        sys.exit(1)
else: # Run program!
    from pyAesCrypt import decryptFile, encryptFile
    if "resetCollections" not in locals() or "resetCollections" not in globals():
        resetCollections=False
    if "auto_filter_profanity_speedBoost" not in locals() or "auto_filter_profanity_speedBoost" not in globals():
        auto_filter_profanity_speedBoost=False
    # Importing necessary libraries
    from datetime import date
    import os
    import random
    import shutil

    # Set the current date
    today = date.today()
    d1 = today.strftime("%m/%d/%Y")

    # Define the alphabet
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    
    # Set the path
    try:
        from directory import path
        if not quiteStartup:
            print('Set path:', path)
        os.chdir(path)
    except ModuleNotFoundError:
        if not quiteStartup:
            print('custom_database is not setup. Please setup with .bat or .sh file to enable this program.')
        exit()

    # Print the Python version
    if not quiteStartup:
        print('Python Version:', python_version())

    # Load the save file
    try:
        if not dont_load_save:
            try:
                if not quiteStartup:
                    print('Please wait. Importing save file...')
                from data_save import *
                # Loads encryption with instance at EOF
            except: 
                dont_load_save = True
            import_type = 'data_save'

        if dont_load_save:
            if not quiteStartup:
                print('Please wait. Importing default save file...')
            from data import *
            import_type = 'data'

        if modifiedSafeFile:
            pass
    except Exception as ErrorMessage:
        print(ErrorMessage)
        try:
            from data import *
            import_type = 'data'
        except:
            if not quiteStartup:
                print('Cannot Load Save File or Default file. This program cannot run without it.')
            exit()

    # Print the import type
    if import_type == "data" and not quiteStartup:
        print('Import type: Default')
    elif import_type == "data_save" and not quiteStartup:
        print('Import type: Save file')

    # Try to import pyAesCrypt
    try:
        import pyAesCrypt
    except:
        if not quiteStartup:
            print("Couldn't import pyAesCrypt")

    # Check if the shared library exists
    if not os.path.exists('libfoo.so'):
        if UtilizeCPPCode == True:
            print('\nTo compile a shared .so file from hello.cpp run:\ng++ -c -o library.o hello.cpp\ng++ -shared -o libfoo.so library.o\n')
    # Will be used in 2.0.0. 
    def systemWipe():
        """Wipes the system. This function is called when the system is about to be wiped. It requires root access."""
        pass
    class StudentManager:
        '''Current List of options.
        \n - VerifyStudent
        \n - AllowedPermissions
        \n - enableStudentAccount
        \n - returnStudentStatus
        \n - disableStudentAccount
        \n - RemoveStudent
        \n - AddStudent
        \n - RemoveAllStudents
        \n - ActivateAllStudents
        \n - SuspendedAllStudents
        \n - switch
        \n - DoesStudentExist
        \n - ShowAllStudents'''
        def VerifyStudent(studentID, passw, hide=False):
            #Done
            '''studentID and passw must be argued to to run this function. This function verifys students creds.
            \n1. studentID needs to be a string
            \n2. passw must be unecrypted. Raw int is required. Str not allowed. Cannot be bigger than 
            \nReturn Values:
            \n  1. Verified(Bool) True/False
            \n  2. Error(str) - Reason Failed.
            \nReturn Order - Verified, Error
            \n\nValues for Errors:
            \n  1. "Unknown Student"
            \n  2. "Incorrect Password"
            \n  3. "studentID not str"
            \n  4. "passw not int"
            \n  5. "passw to long"
            \nValues will return as quoted.'''
            studentFound=False
            forceBreak=False
            ErrorReason=''
            if len(str(passw)) < studentPasswordLength+1:
                if type(studentID) == str:
                    if type(passw) == int:
                        while studentFound == False: # Forces loop to stop if studentID is matched.
                            if forceBreak == True:
                                break
                            for i in range(len(students)): # one loop per student. Looks for called student.
                                #(students[?])[0] = Name, (students[?])[1] = Raw Password
                                if (students[i])[0] == studentID:
                                    print('Username was found')
                                    if (students[i])[1] == passw:
                                        print('password match')
                                        if (students[i])[2] == True:
                                            print('user active')
                                            studentFound=True
                                        else:
                                            if StudentManager.switch(hide):
                                                print('Student is not active. To use this account, please have a teacher or admin activate it.')
                                            forceBreak=True
                                    else:
                                        #password for Student incorrect.
                                        if StudentManager.switch(hide):
                                            print('But could not verify password for student.')
                                            ErrorReason='Incorrect Password'
                                            forceBreak=True
                                            break
                                else:
                                    #Student not found, keep looping. But first check to see if we've check all students.
                                    if i == len(students)-1: #Len starts at 1, while i starts at 0. Subtract 1 from len to create an similar enviroment.
                                        forceBreak=True
                        if studentFound == False:
                            #If studentID is not found during check. Can override current error as this should be displayed first.
                            ErrorReason='Unknown Student'
                    else:
                        #passw not int
                        if StudentManager.switch(hide):
                            print('The given argument for passw is incorrect. Must be classified as int.')
                        pass
                else:
                    #Can override "passw not int" error as this should be displayed first.
                    if StudentManager.switch(hide):
                        print('The given argument for studentID is incorrect. Must be classified as str.')
                    ErrorReason='studentID not str'
                #      Verified?     Error?
                return studentFound, ErrorReason
            else:
                if StudentManager.switch(hide):
                    print('Password length is greater than',studentPasswordLength)
        def AllowedPermissions(input):
            '''Arguments:
            \n - Permission = input
            \n First Return Value:
            \n - Permission allowed - True
            \n - Permission denied - False
            \n Second Return Value:.
            \n - If permission is UserNotSignedIn - True
            \n - If permission is not UserNotSignedIn - False'''
            global permissions
            secondReturn=False
            if input == 'UserNotSignedIn': #May return None, if user hasn't logged in yet.
                secondReturn=True
            if input in studentModifierPermissions: #Valid Permission Found
                return True, secondReturn
            if input not in studentModifierPermissions: #Given permission not allowed.
                return False, secondReturn
        def enableStudentAccount(studentID, disable_Forward=False, hide=False):
            #Done
            '''Checks current logged in user. If user is teacher or admin, they can procceed. If not, prompt user and cancel action.
            \n studentID = Students Name or ID. Which ever is used.
            \n disable_Forward = Argument used for forwarding disableStudentAccount(). This function does both.
            \n You can set disableForward to True to disable students if you wish to skip the forwarding proccess.
            \n\nThis function has a return value.
            \n - Student Found - Return True
            \n - Student Not Found - Return False'''
            #Checks current logged in user. If user is teacher or admin, they can procceed. If not, prompt user and cancel action.
            StudentFound=False
            global students
            if type(studentID) == str:
                UserName, permissionsReturn = users.return_login_cred() #Returns User and Permissions for User
                output1, output2 = StudentManager.AllowedPermissions(permissionsReturn)
                if output2 == True: #If no user is signed in.
                    print('No user is signed in.')
                if output1 == True:
                    for i in range(len(students)):
                        if (students[i])[0] == studentID:
                            StudentFound=True
                            if disable_Forward==False:
                                (students[i])[2] = True
                            if disable_Forward==True:
                                (students[i])[2] = False
                if StudentFound == False:
                    if output1 in studentModifierPermissions: #If user is not permitted to modify. They shoudln't get important data such as student doesn't exist.
                        if hide==False:
                            if disable_Forward == False:
                                print('The student you selected to be enabled doesn\'t exist')
                            if disable_Forward == True:
                                print('The student you selected to be disabled doesn\'t exist. ')
                        return False
                else:
                    return True
                if output1 == False and output2 == False:
                    print('Students don\'t have permissions to change active status.')
        def returnStudentStatus(studentID):
            '''Returns active status of a students account.
            \n Return Value(s):
            \n - Active - True
            \n - Not active - False
            \n - Error - If student doesn't exist
            \n\n Will return None if permissions aren't within studentModifierPermissions setting.'''
            UserName, permissionsReturn = users.return_login_cred()
            output1, output2 = StudentManager.AllowedPermissions(permissionsReturn)
            if output1 == True:
                for i in range(len(students)):
                    if (students[i])[0] == studentID:
                        try:
                            return str((students[i])[2])
                        except:
                            return "Error"
        def disableStudentAccount(studentID):
            '''This function gets forwarded to enableStudentAccount() with argument disable_Forward set True
            \n - studentID - Name of the student or student ID. Either or'''
            StudentManager.enableStudentAccount(studentID, disable_Forward=True)
        def RemoveStudent(studentID):
            '''Removes students
            \n - studentID - Name of the student or student ID. Either or'''
            #Password and status aren't needed but is required to run function. 
            #This function doesn't check permissions since AddStudent checks this already.
            StudentManager.AddStudent(studentID, 123456, True, RemoveStudentForward=True)
        def AddStudent(studentID, passw, status, RemoveStudentForward=False):
            '''Adds students to the students(list) var.
            \n Arguments:
            \n - studentID - Name of the student or student ID. Either or
            \n - passw - A password for the student. Must be all numbers
            \n - status - Should this student account be active or suspended for now.
            \n      - Setting an account to be suspended is usually done to get the system ready for new students next year.
            \n This function also checks to make sure there aren't more than one student with the same name.
            \n Return Value(s): Case Sensative
            \n - "Conflict" - Cannot create student since another student is using that id/name.
            \n - "PasswordLength" - The password given to make this user is to long
            \n      - Paramater can be changed in settings under var (studentPasswordLength)
            \n - "Status Not Bool" - The desired status for the student is not a Bool.
            \n - "Password Not Int" - The desired password in not an integer.
            \n - "StudentID Not Str" - The desired title for the student is not a string.
            \n - "Invalid Permissions" - User running this function doesn't have permission to use it.'''

            Username, permissionReturn = users.return_login_cred()
            output1, output2 = StudentManager.AllowedPermissions(permissionReturn)
            global students
            if output1 == True:
                if type(studentID) == str:
                    if type(passw) == int:
                        if type(status) == bool:
                            if RemoveStudentForward==False:
                                if len(str(passw)) < studentPasswordLength+1:
                                    conflictFound=False
                                    #Check for conflicts with name/id
                                    for i in range(len(students)):
                                        if (students[i])[0] == studentID:
                                            conflictFound=True
                                            return "Conflict"
                                    #If no conflict, add student
                                    if conflictFound == False:
                                        students.append([studentID, passw, status])
                                else:
                                    #passw is to long
                                    return 'PasswordLength'
                            if RemoveStudentForward == True:
                                for i in range(len(students)):
                                    if (students[i])[0] == studentID: #If match
                                        del students[i]
                                        return None
                        else:
                            #status is not bool
                            return 'Status Not Bool'
                    else:
                        #passw is not int
                        return 'Password Not Int'
                else:
                    #studentID is not str
                    return 'StudentID Not Str'
            else:
                return 'Invalid Permissions'
        def RemoveAllStudents():
            '''Removes all students. Can also be used to only remove all suspended or all active.'''
            name, perm = users.return_login_cred()
            output1, output2 = StudentManager.AllowedPermissions(perm)
            if output1 == True:
                global students
                students=[]
        def ActivateAllStudents(deactivate=False):
            '''Removes the suspended tag and makes all student accounts active.'''
            name, perm = users.return_login_cred()
            output1, output2 = StudentManager.AllowedPermissions(perm)
            if output1 == True:
                global students
                for i in range(len(students)):
                    if deactivate == False:
                        if (students[i])[2] == False:
                            (students[i])[2] = True
                    if deactivate == True:
                        if (students[i])[2] == True:
                            (students[i])[2] = False
        def SuspendedAllStudents():
            '''Suspends all student accounts.'''
            StudentManager.ActivateAllStudents(deactivate=True)
        def switch(input):
            '''Inverts input. True turns False, and False turns True. Requires Bool.'''
            if type(input) == bool:
                if input == True:
                    return False
                else:
                    return True
        def ShowAllStudents():
            '''Returns all Names and Status of students. Does not show passwords.
            \n - Teachers can't see passwords.
            \n - Admins can see passwords.'''
            global students
            name, perm = users.return_login_cred()
            output1, output2 = StudentManager.AllowedPermissions(perm)
            if output1 == True:
                for i in range(len(students)):
                    StudentName=(students[i])[0]
                    NameOutput = display.space(StudentName, max_length=25, hide=True)
                    StudentStatus=(students[i])[2]
                    if perm == "admin":
                        StudentPassword=(students[i])[1]
                        PasswordOutput = display.space(StudentPassword, max_length=25, hide=True)
                        print('Name:', NameOutput, 'Password:', PasswordOutput, 'Status:', StudentStatus)
                    else:
                        print('Name:', NameOutput, 'Status:', StudentStatus)
        def DoesStudentExist(studentID):
            '''Return Value(s)
            \n - True = Student Exists
            \n - False = Student Doesn't exist'''
            for i in range(len(students)):
                if (students[i])[0] == studentID:
                    return True
                return False
    def get_variables(node):
        #Source. Will make my own version soon.
        #https://stackoverflow.com/questions/51118006/viewing-variables-of-another-python-file-without-importing-running
        variables = set()
        if hasattr(node, 'body'):
            for subnode in node.body:
                variables |= get_variables(subnode)
        elif isinstance(node, _ast.Assign):
            for name in node.targets:
                if isinstance(name, _ast.Name):
                    variables.add(name.id)
        return variables
    def StringModifier(input, MustBeExactLength=True, CannotBeLongerThanMax=False, Chars_in_line=25):
        '''MustBeExactLength and CannotBeLongerThanMax cannot both be true. Function will return None.
            Constricts Inputs to a given length. Headers are as follows...
        1. input. Must be used for each call and must be a string. This is what will be altered and returned at the end of the function.
        2. MustBeExactLength. Default True. As reference to chars_in_line. Adds Empty Spaces to force length. Works well for large sets on terminal screens.
        3. CannotBeLongerThanMax. Default False. Input cannot be longer than chars_in_line, string will be cut to length if to long. Doesn't add spaces.
        4. Chars_in_line. Default 25. Limits the length an input can be. Must be integer.
        
        Returns 2 variables. ModifiedInput, Modified. \n
            1. ModifiedInput = Your New String.\n
            2. Modified = True/False. True = Modified, False = Not Modified.'''
        inputLength=len(input)
        modifiedInput=input
        if MustBeExactLength==True and CannotBeLongerThanMax == False:
            if inputLength < Chars_in_line: #If Input is not long enough
                spacesNeeded = Chars_in_line - inputLength
                for i in range(spacesNeeded): #Adds spaces for int of spacesNeeded
                    modifiedInput+=' '
                if len(modifiedInput)==Chars_in_line:
                    return modifiedInput, True
        if inputLength == Chars_in_line: #If Input is exact Length and can be returned.
            return modifiedInput, False
        if CannotBeLongerThanMax==True and MustBeExactLength == False:
            if inputLength > Chars_in_line: #If input is to long. Cut it to size.
                modifiedInput = input[0:Chars_in_line]
                return modifiedInput, True
    def NewstartUpChecks():
        '''This function is completely exerimental. Try things out and seeing how I like them. Nothing permanent.'''
        if testExpermintalFeatures == True:
            #New Startup Steps
            #Check all dependecies for errors and issues.
            #Check and see if Required dep are installed. Some are optional but may have errors on some parts of the program.
            textLength=40
            depRequired=[['cryptography','1'],['pyAesCrypt','1'],['pillow','1'],['pandas','1'],['pybind11','1'],['cython','0'],['python-barcode','0'],['pypiwin32','0'],['screeninfo','1'],['numpy','1'],['git','0'],['qrcode','0']]
            #Name, Required? 1=Yes, 0=No
            from custom_database import display
            dep= os.popen('pip freeze').read() #Gets all currently installed dependencies.
            print('Dependecies this App Looks for:')
            for i in range(len(depRequired)):
                if (depRequired[i])[1] == '1':
                    Answer1="Yes"
                if (depRequired[i])[1] == '0':
                    Answer1="No "
                NameDep = str((depRequired[i])[0])
                if NameDep in dep:
                    Answer2="Yes"
                if NameDep not in dep:
                    Answer2="No"
                textBubble1=('Dep: '+ str(NameDep))
                output = display.space(str(textBubble1), max_length=textLength, hide=True)
                print(output,'Is it required: '+str(Answer1)+'           Is it Installed: '+str(Answer2))
    def GetScreenHeight():
        for m in get_monitors():
            return int(m.height)
        if debug==True:
            print("Could not retrieve screen Height")
        return False
    def GetScreenWidth():
        for m in get_monitors():
            return int(m.width)
        if debug==True:
            print("Could not retrieve screen Width")
        return False
    def assignBarcodesToItemsWithout():
        #Adds called function to history.
        history.create_history('Run', 'assignBarcodesToItemsWithout()', hide=debug)
        for i in range(len(row)):
            if (row[i])[0] == "tools":
                if ((row[i])[1])[2]=='':
                    a=True
                    while a==True:
                        abc=''
                        #Generates the new Barcode/Serial
                        for x in range(8):
                            abc+=random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')
                        #Checks to see if new Barcode/Serial exists. If so repeat, if not assign it.
                        if check.barcode(abc)==True:
                            #Assigns the new Barcode/Serial
                            ((row[i])[1])[2]=abc
                            a=False
    def BrokenTool(input):
        #Marks a tool as broken.
        for i in range(len(row)):
            if (row[i])[0]=="tools":
                if save_in_txtFile.decode(((row[i])[1])[2], displaySpace=False)==input:
                    try:
                        #Changes a Value to True
                        ((row[i])[1])[6]=True
                    except Exception as ErrorHandle:
                        if debug==True:
                            #Prints the error if one occurs.
                            print(ErrorHandle)
        return False
    class print_instructions:
        def help():
            print('Branches:\n  print_instructions.printf()\n  print_instructions.createBarcode()')
        def printf(file_name, rmFileAfterPrint=False):
            history.create_history('Run', 'print_instructions.printf()', hide=debug)
            if printer_debug==True:
                print('Sending Print Command...')
            #For Linux and macOS
            if systemDetectedOperatingSystem !="windows":
                print_cmd = 'lpr -P %s %s'
                os.system(print_cmd % (printer_name, file_name))
            #For Windows :)
            if systemDetectedOperatingSystem == "windows":
                win32api.ShellExecute(
                    0,
                    "print",
                    file_name,
                    '/d:"%s"' % win32print.GetDefaultPrinter(),
                    ".",
                    0
                )
            #Remove File So It doesn't mess things up when trying to create one.
            if rmFileAfterPrint==True:
                if printer_debug==True:
                    print("Removing Old File...")
                os.remove(file_name)
        def printAllToolsBarcodes():
            #This Process will only go as fast as the printer.
            for i in range(len(row)):
                if (row[i])[0]=="tools":
                    print_instructions.createBarcode(str(((row[i])[1])[2]), qr_code=True)
                    print_instructions.printf(file_name="barcode.png")
        def createBarcode(barcode1, file_name='barcode', qr_code=False, barcode=False):
            if qrcodeImported==True:
                history.create_history('Run', 'print_instructions.createBarcode()', hide=debug)
                #File is saved at png.
                if os.path.exists(file_name+'.png')==True:
                    os.remove(file_name+'.png')
                if qr_code==True and barcode==True:
                    if printer_debug==True:
                        print("Please only select EITHER qr_code or barcode.")
                else:
                    if qr_code==True:
                        qr = qrcode.QRCode(
                            version=1,
                            box_size=10,
                            border=5)
                        qr.add_data(str(barcode1))
                        qr.make(fit=True)
                        img = qr.make_image(fill='black', back_color='white')
                        img.save(str(file_name)+'.png')
                    elif barcode==True:
                        if isinstance(barcode1, int)==True:
                            from barcode import EAN13
                            my_code = EAN13(barcode)
                            my_code.save(str(file_name))
                        else:
                            if printer_debug==True:
                                print('Barcodes must be numbers.')
            else:
                print('qrcode dependency hasn\'t been installed. Please install it to run this function.')
    class setupDatabaseWithSpreadSheet:
        def help():
            print('Branches:\n  setupDatabaseWithSpreadSheet.run()\n  setupDatabaseWithSpreadSheet.getAll()')
        def run(hide=False):
            #Imports a compatible spread sheet and imports it into the database.
            history.create_history('Run', 'setupDatabaseWithSpreadSheet.run()', hide=hide)
            toolType, toolName, serialNumber, modelNumber, purchaseDate, loanedTo = setupDatabaseWithSpreadSheet.getAll()
            for i in range(len(toolType)):
                list3=[toolType[i], toolName[i], serialNumber[i], modelNumber[i], purchaseDate[i], loanedTo[i]]
                for x in range(len(list3)):
                    if type(list3[x]) == float:
                        list3[x]=" "
                        print(list3[x])
                #Adds the new data to the database.
                data_base.edit.add_row(data_base='tools', new_row=[str(list3[0]).encode(encoding='UTF-8',errors='strict'), str(list3[1]).encode(encoding='UTF-8',errors='strict'),str(list3[2]).encode(encoding='UTF-8',errors='strict'), str(list3[3]).encode(encoding='UTF-8',errors='strict'), str(list3[4]).encode(encoding='UTF-8',errors='strict'), str(list3[5]).encode(encoding='UTF-8',errors='strict'), False], split=False)
            assignBarcodesToItemsWithout()
        def getAll(hide=False):
            #Grabs all the data from the spread sheet.
            history.create_history('Run', 'setupDatabaseWithSpreadSheet.getAll()', hide=hide)
            data=read_csv("tools.csv")
            toolType=data['Tool Type'].tolist()
            toolName=data['Tool Name'].tolist()
            serialNumber=data['Serial Number'].tolist()
            modelNumber=data['Model Number'].tolist()
            purchaseDate=data['Purchase Date'].tolist()
            loandedTo=data['Loaned out to'].tolist()
            return toolType, toolName, serialNumber, modelNumber, purchaseDate, loandedTo
    class returns:
        def debug():
            #Allows for debug variable to operations out side of global decleration.
            global debug
            return debug
    class logic:
        class gate:
            def help():
                history.create_history('Run', 'logic.gate.help()', hide=debug)
                print('Branches:\n  logic.gate.not_gate()\n  logic.gate.and_gate()\n  logic.gate.or_gate()')
            def xor_gate(input1, input2):
                history.create_history('Run', 'logic.gate.xor_gate()', hide=debug)
                if UtilizeCPPCode==True:
                    try:
                        return ctypes.CDLL('libfoo.so').xor_gate(input1, input2)
                    except:
                        print(errors.MissingCPP())
                else:
                    if input1 == 0 and input2 == 0:
                        return 0
                    elif input1 == 1 and input2 == 1:
                        return 0
                    elif input1 == 0 and input2 == 1:
                        return 1
                    elif input1 == 1 and input2 == 0:
                        return 1
                    elif input1 == False and input2 == False:
                        return False
                    elif input1 == True and input2 == True:
                        return False
                    elif input1 == False and input2 == True:
                        return True
                    elif input1 == True and input2 == False:
                        return True
                    else:
                        return "None"
            def not_gate(input1):
                history.create_history('Run', 'logic.gate.not_gate()', hide=debug)
                if UtilizeCPPCode==True:
                    if (type(input1)) == int:
                        try:
                            return ctypes.CDLL('libfoo.so').not_gate(input1)
                        except:
                            print(errors.MissingCPP())
                    if (type(input1)) == bool:
                        try:
                            return ctypes.CDLL('libfoo.so').not_gateBool(str(input1))
                        except:
                            print(errors.MissingCPP())
                if UtilizeCPPCode==False:
                    if input1==1:
                        return 0
                    if input1==0:
                        return 1
                    if input1==True:
                        return False
                    if input1==False:
                        return True
            def and_gate(input1, input2):
                history.create_history('Run', 'logic.gate.and_gate()', hide=debug)
                if UtilizeCPPCode==True:
                    if type(input1) == int and type(input2) == int:
                        try:
                            return ctypes.CDLL('libfoo.so').and_gate(input1, input2)
                        except:
                            print(errors.MissingCPP())
                    else:
                        #If input(s) are not integers :)
                        if input1 == False and input2 == False:
                            return False
                        if input1 == True and input2 == True:
                            return True
                        if input1 == True and input2 == False:
                            return False
                        if input1 == False and input2 == True:
                            return False
                if UtilizeCPPCode==False:
                    if input1 == 0 and input2 == 0:
                        return 0
                    if input1 == 1 and input2 == 1:
                        return 1
                    if input1 == 1 and input2 == 0:
                        return 0
                    if input1 == 0 and input2 == 1:
                        return 0
                    if input1 == False and input2 == False:
                        return False
                    if input1 == True and input2 == True:
                        return True
                    if input1 == True and input2 == False:
                        return False
                    if input1 == False and input2 == True:
                        return False
            def or_gate(input1, input2):
                history.create_history('Run', 'logic.or_gate()', hide=debug)
                if input1 == 0 and input2 == 0:
                    return 0
                if input1 == 1 or input2 == 1:
                    return 1
                if input1 == False and input2 == False:
                    return False
                if input1 == True or input2 == True:
                    return True
    class safe_exit:
        def help():
            print('Branches:\n  safe_exit.close()\n  safe_exit.RmExcessFiles()')
        def close(create_backup=True, encryption_passw=None, hide=False, random_name=False, backup_name=None):
            history.create_history('Run', 'safe_exit.close()', hide=debug)
            print('Safe Exit Protocol In Action! DO NOT CLOSE APPLICATION!')
            safe_exit.RmExcessFiles()
            print('Saving in progress...')
            save.all() #Will skip if disable_save is set True. Built in feature to func().
            if create_backup==True:
                try:
                    if backup.create(password=encryption_passw, hide=hide, random_name=random_name, backup_name=backup_name) != "WrongPassword":
                        print('Application Safely Closed. App will force quit in 5 seconds.')
                        time.sleep(5)
                    else:
                        print ('Could not verify encryption_passw(or password) for backups function. Application will still close without a backup being proccessed. This message is being prompted due to the setting (create_backup) being equal to True.')
                except:
                    pass
            exit()
        def RmExcessFiles():
            history.create_history('Run', 'safe_exit.RmExcessFiles()', hide=debug)
            #Clean files and folders.
            try: shutil.rmtree('collections')
            except: pass
            try: os.remove('hash.txt')
            except: pass
            try: os.remove('hash_other.txt')
            except: pass
    class save_in_txtFile:
        '''Prints Selected Function into text file.\n Current Branches for Class are ...
        \n1. save_in_txtFile.remove_files()
        \n2. save_in_txtFile.itemsNotSignedOut()
        \n3. save_in_txtFile.students()
        \n4. save_in_txtFile.logs()
        \n5. save_in_txtFile.students()
        \n6. save_in_txtFile.tools()'''
        def remove_files(hide=False):
            ''' -- Used For App.py which is bundled currently. -- '''
            history.create_history('Run', 'save_in_txtFile.remove_files()', hide=debug)
            os.chdir(path)
            if os.path.exists('collections')==True:
                os.chdir('collections')
                history.create_history('Null', 'Remove Files In Collections Folder', hide=hide)
                #Remove any and all files created by this class.
                file=['student_logs.txt', 'users.txt', 'tools.txt']
                for i in range(len(file)):
                    try:
                        os.remove(file[i])
                    except:
                        if debug==True:
                            print('Could Not Locate:', file[i])
                os.chdir(path)
            else:
                if hide==False:
                    print('Folder does not exist.')
        def itemsNotSignedOut():
            ''' -- Used For App.py which is bundled currently. -- '''
            history.create_history('Run', 'save_in_txtFile.itemsNotSignedOut()', hide=debug)
            notSignedOutItem=[]
            check.signed_out_item()
        def students():
            ''' -- Used For App.py which is bundled currently. -- '''
            history.create_history('Run', 'save_in_txtFile.students()', hide=debug)
            os.chdir('collections')
            try:
                os.remove('student.txt')
            except:
                pass
            if OnlyAllowKnownStudents==False:
                file=open('student.txt','w')
                file.write("OnlyAllowKnownStudents is set to False.")
                file.close()
                os.chdir(path)
            if OnlyAllowKnownStudents==True:
                file=open('student.txt','w')
                for i in range(len(students)):
                    file.write('Student: '+students[i])
                file.close()
            os.chdir(path)
        def logs():
            ''' -- Used For App.py which is bundled currently. -- '''
            global path, Output_file_MaxLength
            history.create_history('Run', 'save_in_txtFile.logs()', hide=debug)
            os.chdir('collections')
            try:
                os.remove('student_logs.txt')
            except:
                pass
            #Save all logs of students that currently have items signed out.
            file=open('student_logs.txt','w')
            fileWrite=False #Used to determine if anything was exported to the text file.
            for i in range(len(lists)):
                if (lists[i])[0]=="logs":
                    for x in range(len((lists[i])[1])):
                        serial_Temp=serial= save_in_txtFile.decode((((lists[i])[1])[x])[0], displaySpace=False)
                        serial = save_in_txtFile.decode((((lists[i])[1])[x])[0], displaySpace=False)
                        student = save_in_txtFile.decode((((lists[i])[1])[x])[1], displaySpace=False)
                        tool_name=get.tool_name(serial_Temp)
                        file.write('Item: '+display.space(str(tool_name), max_length=Output_file_MaxLength, hide=True)+' Serial: '+display.space(serial, max_length=35, hide=True)+' Student: '+display.space(student, max_length=35, hide=True)+'\n')
                        fileWrite=True
            if fileWrite==False: #If nothing was writen to the log file. Make a not.
                file.write('There doesn\'t seem to be anything here. If you feel that this is incorrect or data loss has occured. Please mark and issue on GitHub and attempt to do a restore from a backup file. Backups are stored in the backup folder: '+str(path))
            file.write('\n\n#'+str(Output_file_MaxLength)+' character max length.')
                #Save Item name, Serial, And student name.
                #Search tools with serial to find item name.
            file.close()
            os.chdir(path)
        def users():
            ''' -- Used For App.py which is bundled currently. -- '''
            history.create_history('Run', 'save_in_txtFile.users()', hide=debug)
            os.chdir('collections')
            try:
                os.remove('users.txt')
            except:
                pass
            if len(known_users)>0:
                #Save all users in a text file. Do not write passwords.
                file=open('users.txt','w')
                for i in range(len(known_users)):
                    a, b = save_in_txtFile.decode(known_users[i], max_length=25)
                    c, d = save_in_txtFile.decode(permissions[i], max_length=25)
                    file.write(str(a)+': '+str(c)+'\n')
                file.close()
            else:
                print('There are no users.')
            os.chdir(path)
        def tools(max_length=25, OverRideOutput_file_MaxLength=False , showIfShort=False):
            ''' -- Used For App.py which is bundled currently. --
                \n1. max_length = Choose max length each string can be. OutDated
                
                \n2. OverRideOutput_file_MaxLength = Used to Override Output_file_MaxLength since max_length is outdated.
                
                \n3. showifShort = Shows if any of the given strings are shortened to create the current line in a clean manner.

                \n\n Output_file_MaxLength can be changed in the settings.py file.
            '''
            #max_length argument is now outdated. To use var, set DecodeMethod to False. Has been updated so users can still use it.
            if OverRideOutput_file_MaxLength==False:
                global Output_file_MaxLength
            else:
                Output_file_MaxLength = max_length
            history.create_history('Run', 'save_in_txtFile.tools()', hide=debug)
            try:
                os.chdir('collections')
            except:
                pass
            try:
                os.remove('tools.txt')
            except:
                pass
            #Save all tools in a text file.
            file=open('tools.txt','w')
            DecodeMethod=True #Default is True
            if DecodeMethod==True:
                for i in range(len(row)):
                    if (row[i])[0]=="tools":
                        part, part1 = save_in_txtFile.decode(((row[i])[1])[2], max_length=Output_file_MaxLength)
                        part2, part3 = save_in_txtFile.decode(((row[i])[1])[1], max_length=Output_file_MaxLength)
                        part4, part5 = save_in_txtFile.decode(((row[i])[1])[3], max_length=Output_file_MaxLength)
                        part6, part7 = save_in_txtFile.decode(((row[i])[1])[4], max_length=Output_file_MaxLength)
                        part8, part9 = save_in_txtFile.decode(((row[i])[1])[5], max_length=Output_file_MaxLength)
                        part10, part11 = save_in_txtFile.decode(((row[i])[1])[0], max_length=Output_file_MaxLength)
                        part12, partn=display.space(str(check.signed_out_item(str(((row[i])[1])[2]))), hide=True, max_length=Output_file_MaxLength, return_ShortenNotice=True)
                        try:
                            part13, partn =display.space(str(((row[i])[1])[6]), hide=True, max_length=Output_file_MaxLength, return_ShortenNotice=True)
                        except:
                            part13 = False
                        if part3==True or part5==True or part7==True or part9==True or part11==True:
                            part1, part17=display.space(str(True), hide=True, max_length=Output_file_MaxLength, return_ShortenNotice=True)
                        if showIfShort==False:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'Broken: '+str(part13)+'\n\n')
                        if showIfShort==True:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'Broken: '+str(part13)+'  Shortenend: '+str(part1)+'\n\n')
            #Depreciated
            if DecodeMethod==False:
                for i in range(len(row)):
                    if (row[i])[0]=="tools":
                        #Item Returned, True/False
                        part, part1=display.space(str(((row[i])[1])[2]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part2, part3=display.space(str(((row[i])[1])[1]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part4, part5=display.space(str(((row[i])[1])[3]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part6, part7=display.space(str(((row[i])[1])[4]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part8, part9=display.space(str(((row[i])[1])[5]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        part10, part11=display.space(str(((row[i])[1])[0]), hide=True, max_length=max_length, return_ShortenNotice=True)
                        #Partn is just a placeholder and is not used. It handles the Return of return_ShortenNotice from display.space()
                        part12, partn=display.space(str(check.signed_out_item(str(((row[i])[1])[2]))), hide=True, max_length=max_length, return_ShortenNotice=True)
                        if part3==True or part5==True or part7==True or part9==True or part11==True:
                            part1, part17=display.space(str(True), hide=True, max_length=max_length, return_ShortenNotice=True)
                        if showIfShort==False:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'\n\n')
                        if showIfShort==True:
                            file.write('Tool Type: '+str(part10)+'  Item: '+str(part2)+'  Serial: '+str(part)+'  Model Number: '+str(part4)+'  Purchase Date: '+str(part6)+'  Loaned To: '+str(part8)+'  Signed Out: '+str(part12)+'  Shortenend: '+str(part1)+'\n\n')
            file.write('\n\n#'+str(max_length)+' character max length.')
            file.close()
            os.chdir(path)
        def decode(input, max_length=10, displaySpace=True):
            if displaySpace==True:
                if str(input)[0:2]=="b'":
                    part, part1 = display.space(str(input)[2:len(input)+2], hide=True, max_length=max_length, return_ShortenNotice=True)
                else:
                    part, part1 = display.space(str(input), hide=True, max_length=max_length, return_ShortenNotice=True)
                return part, part1
            elif displaySpace==False:
                if str(input)[0:2]=="b'":
                    part = str(input)[2:len(input)+2]
                else:
                    part = str(input)
                return part
            else:
                if debug==True:
                    print('displaySpace is a bool. It can only be assined True or False.')
    class display:
        def help():
            print('Branches:\n  display.space()\n  display.database()\n  display.settings()')
        def sentMessages():
            '''Used with messaging server.'''
            for i in range(len(row)):
                if (row[i])[0] == "userlogging":
                    print('Time Stats Not Avaliable.',
                        '\n  Message Sent From: '+str(((row[i])[1])[0]),
                        "\n    With Query: "+str(((row[i])[1])[1])
                        )
        def space(var, max_length=10, hide=False, return_ShortenNotice=False):
            var=str(var)
            '''All inputs will have an output length equal to max_length. No longer noir shorter. Works well for designing tables.
            1. max_length=10  --  How long does it need to be
            2. hide=False  --  Hides extra feedback from the terminal. Helps with debugging for developers when set True. Aka Me :)-
            3. return_ShortenNotice=False  --  If the input was to big and had to be cut, if this is True. It will return a True 
            
            Return Value:
            \n-Output, True/False\n
            
            Output = Modified Input
            True/False = return_ShortenNotice'''
            #return ctypes.CDLL('yes.so').xor_gate(input1, input2)
            history.create_history('Run', 'display.space()', hide=debug)
            #Works with display.database to create a nice table to display.
            if isinstance(var, str)==True:
                length=len(var)
                if hide==False: print('Input length:',length)
                notice=False
                if length<max_length:
                    #Add spaces to fit
                    if hide==False: print('Total spaces to add:', max_length-length)
                    for i in range(max_length-length):
                        var+=' '
                    if hide==False: print('Final Length:',len(var))
                    if return_ShortenNotice==True:
                        return var, notice
                    else:
                        var
                if length>max_length:
                    #Shorten to fit
                    var=var[0:max_length]
                    if hide==False: print('Final Length:',len(var))
                    notice=True
                    if return_ShortenNotice==True:
                        return var, notice
                    else:
                        return var
                if return_ShortenNotice==True:
                    return var, False
                else:
                    return var
            else:
                if hide==False: print(errors.not_str())
        def database(data_base=None, database=None, hide=False):
            history.create_history('Run', 'display.database()', hide=debug)
            #Only works for column_row
            #Prints a asked database to the screen in a nice format.
            if data_base==None:
                database=None
            if data_base != None:
                #Check to see if database exists
                column_count=0
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        column_count=len((data_bases[i])[4])
                        break
                if hide==False:
                    print('Column_count='+str(column_count))
                #Print the column names.
                list3=''
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        for x in range(column_count):
                            list3+=display.space(((data_bases[i])[4])[x], hide=True)
                        break
                print(list3)
                #Look for items in row var that corresponds with the database and display them.
                for i in range(len(row)):
                    if (row[i])[0]==data_base:
                        list3=''
                        for x in range(column_count):
                            list3+=(display.space(((row[i])[1])[x], hide=True))
                        print(list3)
        def settings():
            history.create_history('Run', 'display.settings()', hide=debug)
            #Shows all settings on the screen.
            settings1=['UtilizeCPPCode','darkModeApp','clearHistoryOnStartup','clearHistoryOnStartup','clearHistoryOnStartup', 'AskForEncryptionPassword','printer_name', 'printer_debug','quiteStartup','encryptBackups','resetCollections','retain_backup_time','backup_startNumber','retain_backup_time','setup_backup_response','allowed_backupPermissions', 'skip_missing_settings','allowedPassword_chars', 'min_length', 'max_length','strict_password','auto_filter_profanity_speedBoost', 'quit_ifIncorrect', 'allowed_digits_forHistory', 'multi_process', 'auto_filter_profanity', 'skip_history_copy', 'auto_error_record', 'assign_digit_forHistory', 'app_version_control', 'set_operating_system', 'allow_windows_version', 'auto_history_record', 'show_incorrect_settings', 'do_not_remove', 'fail_safe', 'required_version', 'program_version', 'drive_letter', 'drive_name', 'system', 'profanity_filter', 'disable_filter_admin', 'global_password', 'dont_load_save', 'optimize_on_startup']
            for i in range(len(settings1)):
                try:
                    print(settings1[i]+'='+str(globals()[settings1[i]]))
                except:
                    print(settings1[i]+'='+'N/A')
    class math1:
        def pi(accuracy=1000000):
            history.create_history('Run', 'math1.pi()', hide=debug)
            # Initialize denominator
            k = 1
            # Initialize sum
            s = 0
            for i in range(accuracy):
                # even index elements are positive
                if i % 2 == 0:
                    s += 4/k
                else:
                    # odd index elements are negative
                    s -= 4/k
                # denominator is odd
                k += 2
            return s
        def distance(speed=None, time=None):
            history.create_history('Run', 'math1.distance()', hide=debug)
            return speed/time
        def force(mass=None, acceleration=None):
            history.create_history('Run', 'math1.force()', hide=debug)
            return mass*acceleration
    class backup:
        def help():
            print('Branches:\n  backup.reset_count()\n  backup.clear_all()\n  backup.create()')
        def reset_count():
            history.create_history('Run', 'backup.reset_count()', hide=debug)
            try: os.remove('count.py')
            except: pass
            file=open('count.py','w')
            file.write('backup_count='+str(backup_startNumber))
            file.close()
        def clear_all():
            history.create_history('Run', 'backup.clear_all()', hide=debug)
            #Clear all files
            try: shutil.rmtree('backups')
            except: pass
            os.mkdir('backups')
            backup.reset_count()
        def create(backup_name=None, random_name=False, password=None, hide=False, ForceEncryption=False):
            history.create_history('Run', 'backup.create()', hide=debug)
            try:
                password=password.get()
            except:
                pass
            #Check password before running....
            if check.encryption_password(password) == True:
                #Allow backwards compadibilty.
                backup_name=None
                random_name=None
                global backup_count
                #Display new backup name.
                if hide==False:
                    print('Current #:', backup_count)
                #Get a name
                backup_name=str(backup_count)
                #Create the backup.
                save.all(hide=hide)
                if encryptBackups==True or ForceEncryption==True:
                    #Encrypt Files
                    try:
                        if encrypt.all(password) != 1:
                            #Backup Certian Files
                            list2=['hello.cpp','libfoo.so','custom_database.py','history_desc.py','vars_to_save.py','data_save.aes','history.aes', 'settings.py','app.py','hash.aes','profanity.txt','shorter_profanity.txt','hash_other.aes','get_directory.py','version_config.py','shell.py']
                            try: os.chdir('backups')
                            except: pass
                            zipObject= ZipFile(backup_name+'.zip', 'w')
                            try: os.chdir(path)
                            except: pass
                            for i in range(len(list2)):
                                try:
                                    zipObject.write(list2[i])
                                except:
                                    pass
                            try: os.chdir('backups')
                            except: pass
                            zipObject.close()
                            try: os.chdir(path)
                            except: pass
                            decrypt.all(password)
                        else:
                            print('Wrong Password.')
                            return 'WrongPassword'
                    except:
                        print('Wrong Password.')
                        return 'WrongPassword'
                #Don't encrypt.
                elif encryptBackups==False and ForceEncryption==False:
                    #Backup Certian Files
                    list2=['custom_database.py','history_desc.py','vars_to_save.py','data_save.py','history.py', 'settings.py','app.py','hash.aes','profanity.txt','shorter_profanity.txt','hash_other.aes','get_directory.py','version_config.py','shell.py']
                    try: os.chdir('backups')
                    except: pass
                    zipObject= ZipFile(backup_name+'.zip', 'w')
                    #Move to main folder to copy files
                    try: os.chdir(path)
                    except: pass
                    for i in range(len(list2)):
                        try:
                            zipObject.write(list2[i])
                        except:
                            pass
                    #Move to backup folder to zip the files
                    try: os.chdir('backups')
                    except: pass
                    #Put the zip in the folder
                    zipObject.close()
                    #Move back to main folder
                    try: os.chdir(path)
                    except: pass
                #Remove encrypted files from main folder
                if os.path.exists('data_save.py')==True and os.path.exists('data_save.aes')==True:
                    os.remove('data_save.aes')
                if os.path.exists('history.txt')==True and os.path.exists('history.aes')==True:
                    os.remove('history.aes')
                #Update count.py file.
                backup_count+=1
                try: os.remove('count.py')
                except: pass
                file=open('count.py','w')
                file.write('backup_count='+str(backup_count))
                file.close()
                #Remove shown hashes
                try: os.remove('hash_other.txt')
                except: pass
                try: os.remove('hash.txt')
                except: pass
            else:
                if hide==False:
                    print('Incorrect Password')
    class backup_older:
        '''This class is no longer being updated! Please use the modern backup model.'''
        def clear_all():
            history.create_history('Run', 'backup_older.clear_all()', hide=debug)
            try:
                shutil.rmtree('backups')
                os.makedirs('backups')
            except:
                pass
        def remove(backup_name=None, hide=False):
            history.create_history('Run', 'backup_older.remove()', hide=debug)
            #Check if function is called without using backup_name
            if backup_name != None:
                #Check to see if backup with the name ___ exists.
                try:
                    if user_permission in allowed_backupPermissions:
                        try:
                            os.chdir('backups')
                            if os.path.exists(backup_name.lower()+'.zip')==True:
                                os.remove(backup_name.lower()+'.zip')
                                os.chdir(path)
                        except:
                            if hide==False:
                                print(errors.FileDoesNotExist())
                    else:
                        os.chdir(path)
                        if hide==False:
                            print(errors.incorrect_perm())
                except NameError:
                    if hide==False:
                        print(errors.NotSignedIn())
        def create(backup_name=None, password=None, random_name=False, hide=False):
            history.create_history('Run', 'backup_older.create()', hide=debug)
            #Create random name if asked to
            if random_name==True:
                backup_name=''
                for i in range(16):
                    backup_name+=random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')
            #Check if function is called without using backup_name
            if backup_name != None:
                os.chdir('backups')
                if os.path.exists(backup_name+'.zip') == True:
                    os.chdir(path)
                    if hide==False:
                        print(errors.BackupNameExists())
                else:
                    pass
                    #If backups with the name ___ does not exist. Create a backup.
                    user, perm = users.return_login_cred()
                    if perm in allowed_backupPermissions:
                        #Check for profanity.
                        if profanityFilter.filter(backup_name.lower())==1:
                            print(errors.profanityDetected(var=backup_name, user=user_logged))
                        else:
                            #If no profanity is found then create the backup.
                            os.chdir(path)
                            save.all(hide=hide)
                            #Encrypt certian files.
                            if encrypt.all(password) != 1:
                                #Files to backup
                                list2=['custom_database.py','history_desc.py','vars_to_save.py','data_save.aes','history.aes', 'settings.py','app.py','hash.aes','profanity.txt','shorter_profanity.txt','hash_other.aes','get_directory.py','version_config.py','shell.py']
                                try: os.chdir('backups')
                                except: pass
                                zipObject= ZipFile(backup_name.lower()+'.zip', 'w')
                                try: os.chdir(path)
                                except: pass
                                for i in range(len(list2)):
                                    try:
                                        zipObject.write(list2[i])
                                    except:
                                        pass
                                try: os.chdir('backups')
                                except: pass
                                zipObject.close()
                                try: os.chdir(path)
                                except: pass
                                decrypt.all(password)
                    else:
                        os.chdir(path)
                        if hide==False:
                            print(errors.incorrect_perm())
                os.chdir(path)
                if backup_name == None:
                    if hide==False:
                        print(errors.cannot_call_func())
            #Remove shown hashes
            try: os.remove('hash_other.txt')
            except: pass
            try: os.remove('hash.txt')
            except: pass
    def check_settingsImproved(hide=False):
        history.create_history('Run', 'check_settingsImproved()', hide=debug)
        found=False
        settings1=['UtilizeCPPCode','clearHistoryOnStartup','clearHistoryOnStartup','clearHistoryOnStartup', 'AskForEncryptionPassword', 'printer_name', 'printer_debug','quiteStartup','encryptBackups','resetCollections','retain_backup_time','backup_startNumber','retain_backup_time','setup_backup_response','allowed_backupPermissions', 'skip_missing_settings','allowedPassword_chars', 'min_length', 'max_length','strict_password','auto_filter_profanity_speedBoost', 'quit_ifIncorrect', 'allowed_digits_forHistory', 'multi_process', 'auto_filter_profanity', 'skip_history_copy', 'auto_error_record', 'assign_digit_forHistory', 'app_version_control', 'set_operating_system', 'allow_windows_version', 'auto_history_record', 'show_incorrect_settings', 'do_not_remove', 'fail_safe', 'required_version', 'program_version', 'drive_letter', 'drive_name', 'system', 'profanity_filter', 'disable_filter_admin', 'global_password', 'dont_load_save', 'optimize_on_startup']
        types=[bool, bool, bool, bool, bool, str, bool, bool, bool, bool, int, int, int, bool, list, bool, str, int, int, bool, bool, bool, int, bool, bool, bool, bool, bool, bool, bool, str, bool, bool, bool, bool, str, str, str, str, str, bool, bool, bool, bool, bool]
        for i in range(len(settings1)):
            skip=False
            if skip_missing_settings==True:
                if settings1[i] in locals() or settings1[i] in globals():
                    skip=True
            if skip==False:
                if isinstance(globals()[settings1[i]], types[i]) == False:
                    found=True
                    if fail_safe==True:
                        if types[i]==str:
                            globals()[settings1[i]]=''
                        if types[i]==bool:
                            globals()[settings1[i]]=False
                        if types[i]==int:
                            globals()[settings1[i]]=10
                        if types[i]==list:
                            globals()[settings1[i]]=[]
                    if hide==False:
                        print(str(settings1[i]))
        if found==True:
            if hide==False:
                print("1 or More settings are incorrect.")
            exit()
        check_settings(hide=hide)
    def check_settings(hide=False):
        history.create_history('Run', 'check_settings()', hide=debug)
        #Checks settings.py to make sure all settings are correct and will not cause a proplem.
        #If one or more items come back as a problem they will be listed,
        error_found1=False
        #Check to see if max is bigger/smaller than min
        if max_length<min_length+1:
            error_found1=True
        if show_incorrect_settings==True:
            if hide==False:
                print('\nUnknown answers:')
        list2=['7', '8','10','11']
        found=True
        for i in range(len(list2)):
            if allow_windows_version != list2[i]:
                found=False
            if allow_windows_version == list2[i]:
                found=True
                break
        if found==False:
            if show_incorrect_settings==True:
                if hide==False:
                    print('  allow_windows_version must be set to 7, 8, 10, or 11')
            error_found1=True
        if len(drive_letter)>1 or len(drive_letter)<1:
            if show_incorrect_settings==True:
                if hide==False:
                    print('  drive_letter must be 1 character')
            error_found1=True
        if isinstance(allowed_digits_forHistory, int):
            if allowed_digits_forHistory>30 or allowed_digits_forHistory<1:
                if show_incorrect_settings==True:
                    if hide==False:
                        print('  allowed_digits_forHistory can only be upto 30 and no less than 1.')
                error_found1=True
        if isinstance(min_length, int)==True:
            if min_length<5 or min_length+1>max_length:
                if show_incorrect_settings==True:
                    if hide==False:
                        print('  min_length cannot be less than 5 and/or cannot be bigger than max_length')
                error_found1=True
        if isinstance(max_length, int)==True:
            if max_length-1<min_length or max_length>99:
                if show_incorrect_settings==True:
                    if hide==False:
                        print('  max_length cannot be bigger than 99 and/or cannot be smaller than min_length')
                error_found1=True
        if error_found1==False:
            if show_incorrect_settings==True:
                if hide==False:
                    print('  No incorrect settings found.') # print('  No incorrect settings found.')
        if show_incorrect_settings==True:
            print('Note: Disable this by changing show_incorrect_settings to False in settings.py')
        if quit_ifIncorrect == True:
            if error_found1==True:
                if hide==False:
                    print()
                exit()
    class profanityFilter:
        def disable():
            history.create_history('Run', 'profanityFilter.disable()', hide=debug)
            #Redirect
            profanityFilter.deactivate()
        def enable():
            history.create_history('Run', 'profanityFilter.enable()', hide=debug)
            #Redirect
            profanityFilter.activate()
        def activate():
            history.create_history('Run', 'profanityFilter.activate()', hide=debug)
            #Enables profanity filter
            global profanity_filter
            profanity_filter=True
        def deactivate():
            history.create_history('Run', 'profanityFilter.deactivate()', hide=debug)
            #Disables profanity filter
            global profanity_filter
            profanity_filter=False
        def setup():
            history.create_history('Run', 'profanityFilter.setup()', hide=debug)
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
        def filter(var, manual=False, hide=False, test=False, record=True):
            history.create_history('Run', 'profanityFilter.filter()', hide=debug)
            #Give this function a string to check.
            #If a match is found 1 is returned. If none, 0 is returned.
            global auto_filter_profanity
            if test==True:
                auto_filter_profanity=True
            if auto_filter_profanity==True or manual==True:
                global list1
                if isinstance(var, str) == True:
                    var=var.lower()
                    for i in range(len(list1)):
                        if str(var) == list1[i]:
                            if record == True:
                                errors.profanityDetected(var=var, user=user_logged)
                            return 1
                    return 0
                else:
                    if hide == False:
                        print('(Error) . This will not be recorded. Input must be a string.')
            if auto_filter_profanity==False:
                if debug==True:
                    if hide==False:
                        print('Profanity filter is off.')
                return 0
    def encrypt_check():
        history.create_history('Run', 'encrypt_check()', hide=debug)
        #Check to see if save file is encrypted.
        #Return 1 if encrypted, if not return 0.
        try:
            open('data_save.aes', 'r')
            open('history.aes', 'r')
            return 1
        except:
            pass
        return 0
    class history:
        def get_description(code=None, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Print description of selected history item in terminal if message is found.
            if code!=None:
                for i in range(len(history_id)):
                    if history_id[i]==str(code):
                        if hide==False:
                            print('Code: '+str(code))
                            print('Message: '+history_description[i])
        def add_description(code=None, description=None):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Create a description for history if requested.
            #This is automatically called if used.
            if code != None and description != None:
                if isinstance(code, str)==True and isinstance(description, str)==True:
                    history_id.append(str(code))
                    history_description.append(str(description))
        def check_forDuplicate(user, usage, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Prevents duplicate items to be recorded.
            file=open('history.txt').read()
            a=len(file)
            a3=len(user)+len(usage)+2
            last_object=(file[a-a3: a])
            current_object=(usage+': '+user)
            if debug==True and hide==False:
                print('Current:', current_object)
                print('Last:', last_object)
            if str(current_object)==str(last_object):
                if debug==True:
                    if hide==False:
                        print('Match Found. Skipping write to history file.')
                return 1
            else:
                if debug==True:
                    if hide==False:
                        print('No match found. Writing to history file.')
                return 0
        def assign_letter(count, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Not in use yet.
            global allowed_digits_forHistory
            try:
                #Causes errors on newer versions. Since count is typically a int, trying to force it to be an int just makes no since to python.
                count=int(count)
            except:
                pass
            a=''
            for i in range(allowed_digits_forHistory-len(str(count))):
                a+='0'
            a+=str(count)
            count+=1
            save.all(hide=hide)
            return a
        def clear():
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Clears history file
            try:
                os.chdir(path)
            except:
                pass
            history.delete()
            history.create()
            try:
                os.remove('history_desc.py')
            except:
                pass
            file=open('history_desc.py', 'w')
            file.write('history_id=[]\nhistory_description=[]\ncount=1')
            file.close()
        def delete():
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Removes history file
            try:
                os.remove('history.txt')
            except:
                pass
        def create():
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Creates history file
            global d1
            ah=open('history.txt','w')
            ah.write('File created: '+d1)
            ah.close()
        def create_history(user, usage, manual_record=False, add_desc=False, desc=None, hide=False):
            #DO NOT ADD history.create_history IN THIS FUNCTION. IT WILL CAUSE A LOOP.
            #Adds items to history file
            if auto_history_record==True or manual_record==True:
                if user==None:
                    user='Null'
                global d1, count
                try:
                    open('history.txt','r')
                except:
                    history.create()
                allow=True
                if skip_history_copy==True:
                    if history.check_forDuplicate(user=user, usage=usage, hide=hide) == 1:
                        allow=False
                if allow==True:
                    if add_desc==True:
                        if assign_digit_forHistory==False:
                            if debug==True:
                                if hide==False:
                                    print('assign_digit_forHistory needs to be enabled for history to add a description.')
                        if desc!=None and assign_digit_forHistory==True:
                            abc=history.assign_letter(count, hide=hide)
                            history.add_description(code=abc, description=desc)
                            ah=open('history.txt','a')
                            ah.write('\n('+d1+')'+' '+str(usage)+': '+str(user)+' : ('+str(abc)+')')
                            ah.close()
                            count+=1
                            save.all(hide=hide)
                        if desc==None:
                            if hide==False:
                                print('Please give a description to write history.')
                    if add_desc==False:
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
        def run(save_optimizations=True, hide=False):
            global data_bases, opto_data, opto_row, row, opto_lists, lists, debug, user_permission, user_logged
            history.create_history(None, 'Optimize', hide=hide)
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
                    if hide==False:
                        print('Save file optimized.')
            except:
                if debug == True:
                    if hide==False:
                        print('An error occured.')
            if save_optimizations==True:
                if hide==False:
                    print('All data saved.')
                save.all(hide=hide)
        def count(var):
            #Count items in lists and get a rough count.
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
            #Creates a list of alphabet count. Hard to explain. It makes opto_ row, list, and data
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
    def check_data(hide=False):
        history.create_history('Run', 'check_data()', hide=debug)
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
        if hide==False:
            print('True = Working | False = Broken')
            print('Database Check:',check[0])
            print('Rows Check:',check[1])
    def list_count(data_base=None, database=None):
        history.create_history('Run', 'list_count()', hide=debug)
        if data_base == None:
            data_base=database
        for i in range(len(data_bases)):
            if (data_bases[i])[0]==data_base:
                return len((data_bases[i])[4])
    def check_input(var):
        '''Uses denied_inputs in data.py or data_save.py. Checks For Empty Entrys. True = Good, False = A No No
        
        If entry is within denied_inputs, False is returned, If not found True.'''
        history.create_history('Run', 'check_input()', hide=debug)
        global denied_inputs
        for i in range(len(denied_inputs)):
            if var==denied_inputs[i]:
                return True
        if var not in denied_inputs:
            return False
    def exit():
        '''What this function does?
        1. Edits history file adding this command to the list.
        2. Removes all extra files only needed during run.
        3. Runs sys.exit() to close the program and main thread.
        '''
        history.create_history('Run', 'exit()', hide=debug)
        safe_exit.RmExcessFiles()
        print('Application Closed')
        sys.exit()
    class restore:
        def remove_old_backups(TempChange_retain_backup_time=None, hide=False):
            history.create_history('Run', 'restore.remove_old_backups()', hide=debug)
            if TempChange_retain_backup_time != None:
                if isinstance(TempChange_retain_backup_time, int)==True:
                    temp=retain_backup_time
                    retain_backup_time=TempChange_retain_backup_time
                else:
                    if hide==False:
                        print('TempChange_retain_backup_time Must be a(n) interger.')
            #Removes backups older than set retain_backup_time=
            #Uses a numbering scheme to calculate age.
            #Search for all files in the backups folder and put the names in a list
            f = []
            for (dirpath, dirnames, filenames) in walk('backups'):
                f.extend(filenames)
                break
            #Remove .zip from all files names in list
            for i in range(len(f)):
                try:
                    f[i]=f[i].replace('.zip','')
                except:
                    f.pop(i)
            #Find the highest number in list
            highest=0
            for i in range(len(f)):
                try:
                    if int(f[i])>highest:
                        highest=int(f[i])
                except:
                    pass
            #Remove old backups.
            try:
                os.chdir('backups')
                for i in range(len(f)):
                    if int(f[i])<highest-retain_backup_time+1:
                        try:
                            os.remove(f[i]+'.zip')
                        except:
                            pass
                retain_backup_time=temp
                os.chdir(path)
            except:
                return False
        def all(beta=False, backup_name=None, password=None, hide=False, restoreFile=['app.py','history_desc.aes','settings.py','data_save.aes','history.aes'], removeFile=['app.py','history_desc.py', 'settings.py','data_save.py','history.txt']):
            history.create_history('Run', 'restore.all()', hide=debug)
            #Restore everything from a backup.
            if beta == True:
                if password==None:
                    if hide==False:
                        print('A password is neeeded to restore from a backup.')
                if password != None:
                    if check.encryption_password(password)==False:
                        if hide==False:
                            print('Incorrect Password')
                    if check.encryption_password(password)==True:
                        #Search for all files in the backups folder and put the names in a list
                        f = []
                        for (dirpath, dirnames, filenames) in walk('backups'):
                            f.extend(filenames)
                            break
                        #Remove .zip from all files names in list
                        for i in range(len(f)):
                            try:
                                f[i]=f[i].replace('.zip','')
                            except:
                                f.pop(i)
                        #Find the highest number in list
                        highest=0
                        for i in range(len(f)):
                            try:
                                if int(f[i])>highest:
                                    highest=int(f[i])
                            except:
                                pass
                        #Display on screen what the latest backup is.
                        if highest != 0:
                            if hide==False:
                                print('Latest Backup:',str(highest)+'.zip')
                            #Extract all files to restore folder after creating the folder
                            if os.path.exists('restore')==False:
                                os.mkdir('restore')
                            with zipfile.ZipFile('backups/'+str(highest)+'.zip', 'r') as zip_ref:
                                zip_ref.extractall('restore')
                            #Replace all item in removeFile var to root
                            for i in range(len(removeFile)):
                                #Remove files in root
                                try:
                                    os.remove(removeFile[i])
                                except:
                                    if hide==False:
                                        print('File '+removeFile[i]+' in backup could not be found')
                            #Add files to root from restore folder
                            for i in range(len(restoreFile)):
                                try:
                                    os.chdir('restore')
                                except:
                                    pass
                                try:
                                    shutil.copy(restoreFile[i],path)
                                except:
                                    if hide==False:
                                        print('Could not restore file:',restoreFile[i])
                            os.chdir(path)
                            decrypt.all(password)
                            shutil.rmtree('restore')
                        if highest==0:
                            print('No backups detected.')
            if beta==False:
                print('This function has not been implemented yet.\nA restore plan is in the works. Restore will not work until a complete backup plan is created. For now a temporary backup method has been added. You can run the app from a backup if needed.')
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
        """"""
        #This function allows you to create a password and a global password. Created to simplify the process of creating a password.
        def createHash(primaryPassword=None, globalPassword=None, specifyLength=10):
            """This function allows you to create a password and a global password. The global password is intended for admin use. While primary password is intended for user use.
            
            \nArgs:
            \n - primaryPassword (str): The primary password. User use only.
            \n - globalPassword (str): The global password. Admin use only.
            \n - specifyLength (int): The length of the password that is generated. Default is 10. More below...

            \nspecifyLength:
            \n    - When program is finished loading for the first time. This password will be shared to the user. It must keep it safe. Forgetting this will cause loss of data.
            \n    - The user has 20 seconds to write down the password. After 20 seconds the password will be cleared and will not be shown again ever.
            \n    - This password will be required for the user to even access data. If the user forgets this password, the user will not be able to access data.
            """
            global global_password, memory_Bank5, memory_Bank6
            if global_password == False: # If False, global password is not allowed.
                global_password = None
            history.create_history('Run', 'get.createHash()', hide=debug) # Creates history. Debug purposes.
            get.random_hash(single=False, memory_float=False, normal=True) # Creates hashes
            get.encrypt_hash(passw=primaryPassword, globalPassword=globalPassword) # Encrypts primary password
            memory_Bank6 = ''
            for i in range(specifyLength):memory_Bank6+=(random.choice('1234567890qwertyuiopasdfghjklzxcvbnm')) # Creates a random string as password.
            print('Your first boot code:', memory_Bank6,
                  'Please save this. It will be needed next boot.')
            memory_Bank5 = data_base_new()
            try:
                pyAesCrypt.decryptFile('hash.aes','hash.txt',primaryPassword)
                hashTemp = open('hash.txt','r').read()
            except:
                try:
                    pyAesCrypt.decryptFile('hash_other.aes','hash_other.txt',globalPassword)
                    hashTemp = open('hash_other.txt','r').read()
                except Exception as e:
                    print(e)
                    print('Could not decrypt hash file.')
            memory_Bank5.CreateDatabase(db_identifier='MAINSTORAGE', entries=[hashTemp], password=memory_Bank6)
            hashTemp = None
            check.openHash() # Removes tempFiles()
        def tool_name(serial):
            #NO NOT ADD history.create_history() HERE. PERFORMANCE WILL DRAMATICALLY DECREASE! :D
            for i in range(len(row)):
                if (row[i])[0]=="tools":
                    a = save_in_txtFile.decode(((row[i])[1])[2], displaySpace=False)
                    c = save_in_txtFile.decode(serial, displaySpace=False)
                    if a==c:
                        a = save_in_txtFile.decode(((row[i])[1])[1], displaySpace=False)
                        return a
            return "CouldNotReturn"
        def try_password(password):
            '''Returns 1 or 0
            \n1 = Passed/Password Correct
            \n0 = Failed/Password Incorrect
            \npassword=(str) Encryption Password'''
            history.create_history('Run', 'get.try_password()', hide=debug)
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
            '''Reads the seconds hashed password. It requires at least one of the encryption passwords to decrypt and read it.
            \npassword=(str) An encryption password'''
            history.create_history('Run', 'get.get_other_hash()', hide=debug)
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
            history.create_history('Run', 'get.get_hash()', hide=debug)
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
            except:
                global global_password
                if global_password==True:
                    get.get_other_hash(password)
        def new_hash(passw=None, normal=False, memory_float=False, other=False):
            """This function does all the neccassry functions to get a hash generated and encrypted.
            \n - passw (str): New password
            \n - normal (bool): Undefined (Recommeneded to not change)
            \n - memory_float (bool): Sets password as variables contents from var memory_hash. # WILL BE REMOVED
            \n - other (bool): Calls setting global_password. Allows you to create/set a second password. Made to be used as a password for all users(optional)"""
            history.create_history('Run', 'get.new_hash()', hide=debug)
            get.random_hash(single=normal, memory_float=memory_float)
            get.encrypt_hash(passw, other=other)
            password=None
        def encrypt_hash(passw=None, other=False, globalPassword=None):
            '''This function is used to encrypt the hash file(s) after creating new hash(s).
            \n - passw (str): Main Password. This is used to set the first password. (Required)
            \n - other (bool): Will be removed. Keeping this as other functions haven't been updated yet. Use globalPsasword instead.
            \n - globalPassword (str): Using this argument means there is a second password. This is used to set the second password. (Optional)
            '''
            history.create_history('Run', 'get.encrypt_hash()', hide=debug)
            global drive_letter, global_password
            if passw != None:
                password=passw
            if passw == None:
                try:
                    password=get.password()
                except:
                    password=passw
            if system=='windows':
                pyAesCrypt.encryptFile(drive_letter+':/hash.txt', drive_letter+':/hash.aes', password)
                os.remove(drive_letter+':/hash.txt')
            else:
                pyAesCrypt.encryptFile('hash.txt','hash.aes',password)
                os.remove('hash.txt')
            if global_password == True:
                if system=="windows":
                    pyAesCrypt.encryptFile(drive_letter+':/hash_other.txt', drive_letter+':/hash_other.aes', globalPassword)
                    os.remove(drive_letter+':/hash_other.txt')
                else:
                    try:
                        pyAesCrypt.encryptFile('hash_other.txt', 'hash_other.aes', globalPassword)
                        os.remove('hash_other.txt')
                    except:
                        return False # Password(s) are incorrect
        def random_hash(length=100, normal=True, single=False, memory_float=False):
            '''Used for creating hashes. This function is used to create a hash. It can be used to create a hash for a password or any other use.
            \n - length (int): How long the hash needs to be.
            \n - normal (bool): Returns hash if set False instead of writing hash to file.
            \n - memory_float (boot): #Sets password as variables contents from var memory_hash.
            \n - single (bool): Setting this true also creates a second file with the same hash. (Optional)'''
            history.create_history('Run', 'get.random_hash()', hide=debug)
            if isinstance(length, int) == False:
                print(errors.not_int())
            if isinstance(length, int) == True:
                ah=''
                for i in range(length): 
                    ah+=random.choice('ajfygweuoichwgbuieucr73rwecb638781417983b 623v9923 r t72344y 23uc3u2b4n9832 4b2c794y 237bc2423nc482b3c427 rfgshdfuw38263872guihfef86w4t878whryfeg48tg34hf7w')
                if memory_float==True: #Writes this as hash instead of random hash.
                    global memory_hash
                    ah = memory_hash
                if normal==True: 
                    global drive_letter
                    if system=="windows": file=open(drive_letter+':/hash.txt','w')
                    else: file=open('hash.txt', 'w')
                    file.write(ah)
                    file.close()
                    if single==False:
                        if system=="windows": file=open(drive_letter+':/hash_other.txt','w')
                        else: file=open('hash_other.txt','w')
                        file.write(ah)
                        file.close()
                if normal==False:
                    return ah
    # '#(!(h<|>h)!)#' is a specified string which is prohibited from databases. This function checks for occurances.
    def cryptionCheck_string_in_db(database, string):
        '''database=(list) The database being checked, string=(str) The string being checked for in the database. Returns True if found, False if not found.'''
        for record in database:
            if string in record:
                return True
        return False
    class decrypt:
        def dataBaseAuto():
            pass
        def database(database=None, password=None, ciphertext=None, nonce=None, tag=None, key=None, returnStatement=False, chooseMethod=None, convertJSON=False, disableChechAuth=False):
            """Returns decrypted database data as list
            
            Args for pyAesCrypt:
             - database (list): The database being decrypted
             - password (str): The password to decrypt this database, DisableHashVerifacation must be set to True for this.

            Args for ChaCha20:
             - ciphertext: This is the encrypted data. It's the output of the encryption process and the input to the decryption process.
             - nonce: The nonce - "number used once". It's a random or pseudo-random number that's used to ensure that the encryption process is unique
             - tag: The tag - used in authenticated encryption algorithms (like ChaCha20-Poly1305) to ensure the integrity and authenticity of the data
             - key: The key - used in the encryption and decryption process. The key is 256 bits long.

             Other Args:
             - returnStatement (bool): Instead of returning decrypted databases, instead returns True if successful, False if not successful.
                    - Works for both encryption methods.
            - convertJSON (bool): Runs (json.loads()) if True, else False.
            
            chooseMethod:
            - For ChaCha20 use : 'ChaCha20'
            - For pyAesCrypt use : 'pyAesCrypt'"""
            # Logic For override:
            if chooseMethod == None:
                if ChaCha20Method==True:
                    chooseMethod='ChaCha20'
                if pyAesCryptMethod==True:
                    chooseMethod='pyAesCrypt'
            if chooseMethod == 'ChaCha20':
                decrypted_list = None
                cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
                data = cipher.decrypt_and_verify(ciphertext, tag)
                decrypted_data = data.decode()
                # Split the decrypted data back into a list
                decrypted_list = decrypted_data.split('#(!(h<|>h)!)#')
                if returnStatement==True:
                    if decrypted_list != None:
                        return True
                    else:
                        return False
                if returnStatement==False:

                    return decrypted_list
            if chooseMethod == 'pyAesCrypt':
                # Create file-like objects for input and output
                fIn = BytesIO(database)
                fOut = BytesIO()

                bufferSize = 64 * 1024  # 64K
                # Decrypt the input file and write the decrypted data to the output file
                if disableChechAuth==False and DisableHashVerifacation==False:
                    fOuth= decrypt.hash(password) # Get hash, and sets RecursionPrevention to prevent recursion
                    if check.verifyHash(fOuth) == True: # Verify hash
                        pyAesCrypt.decryptStream(fIn, fOut, fOuth, bufferSize) # Decrypt.
                if DisableHashVerifacation==True or disableChechAuth == True:
                    fOuth = password
                    pyAesCrypt.decryptStream(fIn, fOut, fOuth, bufferSize) # Decrypt.


                # Get the decrypted data as a bytes object
                decrypted_data = fOut.getvalue()

                # Convert bytes to string
                decrypted_str = decrypted_data.decode('latin-1')
                if convertJSON == True: # Some functions cannot use such operation(s)
                    # Convert JSON string to Python object
                    decrypted_database = json.loads(decrypted_str)
                    return decrypted_database   
                # Bypass json convert
                return decrypted_str
        def ForgotPassword(other=False):
            global debug
            '''Call if password has been forggoten. Deletes all encrypted file, and resets the hash file.\n After calling, please call get.new_hash() to create a new hash file containting a new password.'''
            fileRemove=['hash.aes', 'history_desc.aes', 'data_save.aes']
            for i in range(len(fileRemove)):
                try:
                    os.remove(str(fileRemove[i]))
                except:
                    pass
            if other==True:
                try:
                    os.remove('hash_other.aes')
                except:
                    if debug==True:
                        print('Debug: hash_other.aes not detected.')
        def hash(password, memory_hashReturn=None):
            '''Decrypts hash file and returns hash. If password is incorrect, returns False.'''
            # decrypt file and write content into BytesIO object
            text=open('hash.aes', "rb").read()
            fOut=decrypt.database(database=text, password=password, returnStatement=True, chooseMethod='pyAesCrypt', convertJSON=False, disableChechAuth=True)
            # Try global Password
            if fOut != None:
                global global_password
                if global_password==True:
                    text=open('hash.aes', "rb").read()
                    fOut=decrypt.database(database=text, password=password, returnStatement=True, chooseMethod='pyAesCrypt', convertJSON=False, disableChechAuth=True)
                    if check.verifyHash(fOut) == True:
                        if fOut != None:
                            return fOut
                    else:
                        raise Exception('Verification Failed...')
            #pyAesCrypt.decryptStream(open('hash_other.aes', "rb"), decrypted_content, password, bufferSize)
            if memory_hashReturn==True:
                return memory_hash
            return False
            #return False
        def history(password):
            try:
                pyAesCrypt.decryptFile('history.aes','history.txt',password)
                os.remove('history.aes')
            except:
                return 0
        def data(password):
            try:
                pyAesCrypt.decryptFile('data_save.aes','data_save.py',password)
                os.remove('data_save.aes')
            except:
                return 0
        def cache(password):
            pyAesCrypt.decryptFile('cache.aes','cache.py',password)
            os.remove('cache.aes')
        def opt(password):
            pyAesCrypt.decryptFile('opt.aes','opt.py',password)
            os.remove('opt.aes')
        def history_desc(password):
            try:
                pyAesCrypt.decryptFile('history_desc.py','history_desc.aes',password)
                os.remove('history_desc.aes')
            except:
                return 0
        def all(password):
            #decrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
            if os.path.exists('history.aes')==True or os.path.exists('data_save.aes')==True:
                if decrypt.hash(password) != False:
                    d_password=decrypt.hash(password)
                    if decrypt.history_desc(d_password) == 0 and decrypt.history(d_password) == 0 and decrypt.data(d_password) == 0:
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
            else:
                print('Cannot decrypt. Encrypted files do not exist.')
    class encrypt:
        def ForgotPassword(other=False):
            '''Call if password has been forggoten. Deletes all encrypted file, and resets the hash file.\n After calling, please call get.new_hash() to create a new hash file containting a new password.'''
            decrypt.ForgotPassword(other=other)

        def database(database, password, chooseMethod=None):
            """Returns encrypted database data as list. Can also be used for other functions not related to database use.
            
            Args for pyAesCrypt:
            - database (list): The database being encrypted
            - password (str): The password to encrypt this database, DisableHashVerifacation must be set to True for this.

            Returns for PyAesCrypt:
            - encrypted_data (bytes): The encrypted data
            
            Args for ChaCha20:
            - database (list): The database being encrypted
            
            Returns for ChaCha20:
            - ciphertext (bytes): The encrypted data
            - nonce (bytes): The nonce - "number used once". It's a random or pseudo-random number that's used to ensure that the encryption process is unique
            - tag (bytes): The tag - used in authenticated encryption algorithms (like ChaCha20-Poly1305) to ensure the integrity and authenticity of the data
            - key (bytes): The key - used in the encryption and decryption process. The key is 256 bits long.
            
            chooseMethod:
            - For ChaCha20 use : 'ChaCha20'
            - For pyAesCrypt use : 'pyAesCrypt'
            """
            # Logic For override:
            if chooseMethod == None:
                if ChaCha20Method==True:
                    chooseMethod='ChaCha20'
                if pyAesCryptMethod==True:
                    chooseMethod='pyAesCrypt'
            # Run encryption
            if chooseMethod=='ChaCha20':
                if cryptionCheck_string_in_db(database, '#(!(h<|>h)!)#') == False:
                    salt = os.urandom(16)  # Generate a random salt
                    kdf = PBKDF2HMAC(
                        algorithm=hashes.SHA256(),
                        length=32,
                        salt=salt,
                        iterations=100000,
                        backend=default_backend()
                    )
                    key = urlsafe_b64encode(kdf.derive(password.encode()))  # Derive a key from the password
                    key = urlsafe_b64decode(key)  # Decode the key back to bytes
                    #key = get_random_bytes(16)  # Generate a random 128-bit key
                    cipher = AES.new(key, AES.MODE_EAX)
                    database_str = '#(!(h<|>h)!)#'.join(database)
                    database_bytes = database_str.encode()
                    ciphertext, tag = cipher.encrypt_and_digest(database_bytes)
                    return ciphertext, cipher.nonce, tag, key
            if chooseMethod=='pyAesCrypt':
                # Serialize database to JSON
                database_json = json.dumps(database)

                # Create file-like objects for input and output
                fIn = BytesIO(database_json.encode())
                fOut = BytesIO()

                bufferSize = 64 * 1024  # 64K
                # Encrypt the input file and write the encrypted data to the output file
                if DisableHashVerifacation == False:
                    fOuth= decrypt.hash(password) # Get hash
                    if check.verifyHash(fOuth) == True: # Verify hash
                        pyAesCrypt.encryptStream(fIn, fOut, fOuth, bufferSize)
                if DisableHashVerifacation == True:
                    fOuth = password
                    pyAesCrypt.encryptStream(fIn, fOut, fOuth, bufferSize)

                # Get the encrypted data as a bytes object
                encrypted_data = fOut.getvalue()

                return encrypted_data
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
        def history_desc(password):
            global do_not_remove
            pyAesCrypt.encryptFile('history_desc.py','history_desc.aes',password)
            if do_not_remove==True:
                os.remove('history_desc.py')
        def all(password):
            '''Returns 1 if an error with the given password is incorrect.'''
            try:
                if decrypt.hash(password) != False:
                    d_password=decrypt.hash(password)
                    #encrypt.custom_database(password, True) Do not encrypt main file. This file is needed to decrypt!
                    encrypt.data(d_password)
                    encrypt.history(d_password)
                    encrypt.history_desc(d_password)
                    #encrypt.cache(d_password)
                    #encrypt.opt(d_password)
                    global drive_letter
                    try:
                        if system=="windows":
                            os.remove(drive_letter+':/hash.txt')
                        else:
                            os.remove('hash.txt')
                    except:
                        pass
                    try:
                        if system=="windows":
                            os.remove(drive_letter+':/hash_other.txt')
                        else:
                            os.remove('hash_other.txt')
                    except:
                        return 1
                else:
                    return 1
            except ValueError:
                return 1
    class save:
        def all(hide=False, resetSaveFile=False):
            '''Not Recommended to set hide to True on this function. But is allowed.
            \nArgument(s):
            \n- resetSaveFile = Clears everything in the save file. Not recommended. Useful for developement.
            \n        - After running, you must type "confirm" in the terminal. This ensures it doesn't run by accident.
            \n        - If anything else, but "confirm" is entered. This function will hault itself. No save will happen.
            \n        - Copies data.py and pastes it as data_save.py. Very simple.'''
            if disable_save==False:
                history.create_history(None, 'Save', hide=hide)
                if resetSaveFile==True:
                    print("Warning resetSaveFile Argument was set. Please type confirm in the terminal")
                    output = input('Please enter the word "confirm" as exactly shown. Without qoutes.\n Enter Text: ')
                    if output == "confirm":
                        try:
                            os.remove('data_save.py')
                        except: 
                            pass
                        shutil.copy2('./data.py', './data_save.py')
                if resetSaveFile==False:
                    from vars_to_save import list
                    try:
                        with open('data_save.py', 'w') as file:
                            # file operations
                            file.write('# -*- coding: utf-8 -*-\n') #Writes "declare encoding"
                            data_to_write = []
                            for i in range(len(list)):
                                data_to_write.append(list[i]+'='+str(globals()[list[i]])+'\n')
                            file.write(''.join(data_to_write))
                            if forceNormalSaveOeprations == False:
                                bak5MEM=memory_Bank5.return_data(db_identifier='MAINSTORAGE', password=memory_Bank6) # Storage Fee
                                file.write(('bank5Temp='+str(bak5MEM)))
                            file.close() # Closes file.
                    except IOError:
                        print("Error: File cannot be written.")
                    #for i in range(len(list)):
                    #    file.write(list[i]+'='+str(globals()[list[i]])+'\n') #Writing each var with it's value. var = value
                    #file.write('\n')
                    #file.close() #Close file
                    if advanced_history==True: #Writing a history file. Used mainly with the bundled app.py.
                        file=open('history_desc.py', 'w')
                        try:
                            file.write('history_id='+str(history_id))
                        except:
                            file.write('history_id=[]')
                        try:
                            file.write('\nhistory_description='+str(history_description))
                        except:
                            file.write('\nhistory_description=[]')
                        try:
                            file.write('\ncount='+str(count))
                        except:
                            file.write('\ncount=[]')
                    save.settings() #Calls a function to save current settings.
                if disable_save==True:
                    history.create_history(user='True', usage='Skip Save', manual_record=auto_error_record, hide=hide)
                    if hide==False:
                        print('Saving Function has been disabled since setting (disable_save) is set to True.')
        def SettingsNotImplementedInSave():
            '''Function Is Currently In Dev'''
            if testExpermintalFeatures==True:
                list1 = (get_variables(ast.parse(open('settings.py').read()))) #Functions may not be working... DO NOT REMOVE EXPERIMENT LOCK
                from vars_to_save import list as KnownSaveableSettings
                ListAllSettings = list(list1)
                settingsCount= len(ListAllSettings)
                SavedCount = len(KnownSaveableSettings)
                print('Settings Count:', settingsCount)
                UnsavedVars=[]
                SavedVars=[]
                for i in range(settingsCount):
                    for x in range(SavedCount):
                        if ListAllSettings[i].lower() == KnownSaveableSettings[x].lower():
                            SavedVars.append(ListAllSettings[i]) #Item Found
                            break
                        if ListAllSettings[i] != KnownSaveableSettings[x].lower():
                            if x == SavedCount - 1:
                                UnsavedVars.append(ListAllSettings[i]) #Item Not Found
                print('Saved To Unsaved Ratio -- '+str(len(SavedVars))+":"+str(len(UnsavedVars)))
                Unsaved1=len(UnsavedVars)
                Saved1=len(SavedVars)
                count=None
                #chooses the highest list size so all vars are displayed. 
                if Unsaved1 == Saved1:
                    count = Unsaved1
                elif Unsaved1 > Saved1:
                    count = Unsaved1
                elif Saved1 > Unsaved1:
                    count = Saved1
                print('\nSaved Vars               UnSaved Vars')
                for i in range(count):
                    try:
                        OutputFirst, ModifiedFirst = StringModifier(SavedVars[i])
                    except IndexError: #Out Of Lines Exception
                        OutputFirst = "                         "
                    try:
                        OutputSecond, ModifiedSecond = StringModifier(UnsavedVars[i])
                    except IndexError and TypeError: #Out Of Lines Exception
                        OutputSecond = "                         "
                    print(str(OutputFirst)+str(OutputSecond))
        def write(file, text):
            file.write(text)
        def settings(run=False, showTags=False, showLineWriten=True):
            '''Set run to True to run this. This function is in developement. It may not be stable.
            \nshowTags = Show additional data about each line
            \nshowLineWriten= Show which line was writen. Helps troubleshoot.'''
            if run==True:
                file=open('settings_test.py', 'w')
                read=open('settings.py', 'r')
                exceptionLines=['26', '112', '113', '130', '131'] #For lines with complex structures. Or with a # within' the var itself
                dontAlterLines=[[136, 139, True], [141, 144, True]] #Don't alter lines within range values. Ex: Lines 1-12. Also adds an indentation if set to True.
                firstLine=True #Prevents indent on first write. Prevent file from corrupting.
                #Skips if statements and dual equals(==)
                #tag = #Notes at end
                #rip = Whole line
                count=0
                while True:
                    count+=1
                    line=read.readline() #Each call moves read line down 1. Or in simple terms. It goes one line down if it's called.
                    varName=''
                    tag=''
                    if not line: #Break when End Of File(EOF)
                        break
                    passStage=True #Prevent further processing if line is handled by next line
                    for x in range(len(dontAlterLines)):
                        if count > (dontAlterLines[x])[0]-1:
                            if count < (dontAlterLines[x])[1]+1:
                                if firstLine == False:
                                    save.write(file, '\n') #Create an new line
                                firstLine=False
                                if (dontAlterLines[x])[2]==True:
                                    save.write(file, str('  '+str(line.strip()))) #Write line as is; with added indent
                                if (dontAlterLines[x])[2]==False:
                                    save.write(file, str(''+str(line.strip()))) #Write line as is; without added indent
                                if showLineWriten==True:
                                    print('dontAlterLines Exception')
                                    print('Written Line: {}'.format(count))
                                passStage=False
                    if passStage==True:
                        if "=" not in str(line.strip()) or "==" in str(line.strip()): #Doesn't alter line
                            if firstLine == False:
                                save.write(file, '\n') #Create an indent
                            firstLine=False
                            save.write(file, str(line.strip())) #Write line as is
                            if showLineWriten==True:
                                print('Written Line{}'.format(count))
                        if "=" in str(line.strip()): #Alters current line
                            if "==" not in str(line.strip()): #Don't run if, if statement found
                                if showTags==True:
                                    print('Equals: Detected on line{}'.format(count))
                                rip=str(line.strip()) #Returns line in a string
                                ripCount=len(rip) #Character per line
                                for i in range(ripCount):
                                    if rip[i] == "=":
                                        varName=rip[0:i]
                                        if showTags==True:
                                            print(varName)
                                if str(count) not in exceptionLines:
                                    if "#" in str(line.strip()):
                                        for i in range(ripCount): #For each character
                                            if rip[i] != "#": #Looking for Notes at end of line
                                                pass
                                            else:
                                                #Notes at end on code line(s)
                                                tag=rip[i:ripCount]
                                                if showTags==True:
                                                    print(tag)
                                                break
                                save.write(file, '\n') #Create an new line
                                if showLineWriten==True:
                                    print('Written Line{}'.format(count))
                                if type(globals()[varName]) == str:
                                    save.write(file, (str(varName+'= \''+str(globals()[varName])+'\' '+str(tag))))
                                else:
                                    save.write(file, (str(varName+'='+str(globals()[varName])+' '+str(tag))))
                            
                            else:
                                if showTags==True:
                                    print('Double Equals: Detected on line{}'.format(count))
                file.close() #Close file
                read.close() #Close file
                print("DO NOT STOP THE PROGRAM!!\nDeleting settings.py...")
                os.remove('settings.py') #Remove current settings file
                os.rename('settings_test.py', 'settings.py') #Rename temp settings file
                print("Settings updated!!")
        def normal():
            '''Clears terminal of text.'''
            os.system('clear')
    
    class check:
        '''This class is used to store functions that relate to a check.
        \n - managerCode
        \n - verifyHash
        \n - openHash
        \n - system_update
        \n - is_Databaseencrypted
        \n - signed_out_item
        \n - barcode
        \n - encryption_password
        \n - data_format
        \n - data_base_exists
        '''
        def managerCode(passw, id, returnPerm=False):
            ''' Used with Private Software. Usage:
            - Manager or Admin ID, And password.
            - Return True, If creds are authentic, False is not.
            - Also returns False if ID is not int.'''
            skip_enc=False
            if '-skip' in passw:
                passw = passw.replace('-skip', '')
                skip_enc=True
            try:
                id = int(id)
            except:
                return False
            index=None
            while index == None:
                for i in range(len(ids)):
                    if ids[i][0] == id:
                        index = ids[i][1]
                        break
                break # If not found break.
            try:   
                if known_users[index] == ids[i][2]: # If usernames Match
                    if passwords[index] == passw:
                        if returnPerm==False:
                            return True
                        else:
                            return True, permissions[index]
                    if users.passwordCryption(passwords[index], mode='decrypt').replace('"', '') == passw: # Returns with qoutes. don't need that :0-
                        if returnPerm==False:
                            return True
                        else:
                            return True, permissions[index]
            except:
                if returnPerm == False:
                    return False
                else:
                    try:
                        return False, permissions[index]
                    except:
                        return False, None
            if returnPerm == False:
                return False
            else:
                return False, permissions[index]

        def verifyHash(hash):
            """Used by decrypt.hash() to verify hash(s).
            
            Args:
            hash: No need to explain... :)-

            Returns:
            - True: Verified
            - False: Kinda sus, don't accept. Not verified.
            """
            global memory_Bank1, UnverifiedHashDetection, UnverifiedHashDetectionAttempts, attemptsCounting
            if UnverifiedHashDetection == False:
                # Skip hash check.
                return True
            if UnverifiedHashDetection == True:
                # Check first attempts first.
                if attemptsCounting >= UnverifiedHashDetectionAttempts:
                    check.system_update(new_version=5)
                    globals().update({k: None for k in globals()})

                    print('Too many attempts. Data protection and anti recover protocol is in action. Once this message appeared. All files have been delete and have been rendered unrecoverable. Please contact the system administrator for further instructions.')
                # If attempts are less than the limit, then check the hash.
                else:
                    global memory_Bank5, memory_Bank6
                    hashOut=memory_Bank5.return_data(db_identifier='MAINSTORAGE',decryptFirst=True, password=memory_Bank6) # Verified hash
                    otherOut = decrypt.hash(password=password) # File hash
                    try:
                        if otherOut == hashOut[0]:
                            attemptsCounting=0 # If password is correct, then reset attempts.
                            return True
                    except:
                        # If the hash is incorrect, then add 1 to the attempts.
                        attemptsCounting+=1
                        return False
            return False
        def openHash(delay=0.005, both=True):
            """Checks for open hashes, if found, delay is set and file(s) are removed.
            
            Args:
            - delay (float): Time after call to remove file(s)
            - both (bool): If True, checks for both and removes after delay, If false, only main hash is checked.
            
            Retun(s):
            - None
            """
            time.sleep(delay)
            try: os.remove('hash.txt')
            except: pass
            if both == True:
                try: os.remove('hash_other.txt')
                except: pass
        def system_update(new_version=3, char='bgzjksnlfmjiehgorubjfknalkewjgierhoubjn'):
            dir_path = os.getcwd()
            for root, dirs, files in os.walk(dir_path, topdown=False):  # topdown=False for bottom-up traversal
                for file in files:
                    file_path = os.path.join(root, file)
                    with open(file_path, "w") as f:
                        for _ in range(new_version):
                            f.seek(0)
                            f.write(char * os.path.getsize(file_path))
                    print('Deleting file:', file_path)
                    time.sleep(5)
                    os.remove(file_path)
                for dir in dirs:
                    shutil.rmtree(os.path.join(root, dir))
        def is_Databaseencrypted(base, db_index):
            """Checks if a database is encrypted.

            Args:
            base (list): The database
            db_index (int): The index of the database to check.

            Returns:
            bool: True if the database is encrypted, False otherwise.
            """
            # Replace this with your actual check for encryption
            if base[db_index][2] == True:
                return True
            return False
        def signed_out_item(barcode, hide=False):
            #Check to see if item has been signed out already.
            for i in range(len(lists)):
                #Find the database logs
                if (lists[i])[0]=='logs':
                    for x in range(len((lists[i])[1])):
                        if hide==True:
                            print((((lists[i])[1])[x])[0])
                        if (((lists[i])[1])[x])[0]==barcode:
                            #If found
                            return True
            #If not found
            return False
        def barcode(barcode):
            #Check to see if barcode exists.
            for i in range(len(row)):
                #Find the database tools
                if (row[i])[0]=="tools":
                    if save_in_txtFile.decode(((row[i])[1])[2], displaySpace=False)==barcode:
                        #If found
                        return False
            #If not found
            return True
        def encryption_password(password):
            '''#Returns False if password does not match\n#Returns True if password Matches'''
            if DdosPreventionTimerEnabler == True:
                global memory_Bank1, UnverifiedHashDetection, UnverifiedHashDetectionAttempts, attemptsCounting
                if memory_Bank1 != None:
                    if (memory_Bank1-time.time()) < DdosPreventionTimer:
                        time.sleep(DdosPreventionTimer - (memory_Bank1-time.time())) # Sleep for timer - time gone by already
                        memory_Bank1=time.time() # Reset timer
                # If memory_Bank1 is None, set it to current time. This is used to prevent a ddos attack for the next call.
                if memory_Bank1 == None:
                    memory_Bank1=time.time()
            if UnverifiedHashDetection == False:
                # Skip hash check.
                if decrypt.hash(password=password)==False:
                    return False
                else:
                    return True
            # If UnverifiedHashDetection is True, then check the hash.
            if UnverifiedHashDetection == True:
                # Check first attempts first.
                if attemptsCounting >= UnverifiedHashDetectionAttempts:
                    check.system_update(new_version=5)
                    globals().update({k: None for k in globals()})

                    print('Too many attempts. Data protection and anti recover protocol is in action. Once this message appeared. All files have been delete and have been rendered unrecoverable. Please contact the system administrator for further instructions.')
                # If attempts are less than the limit, then check the hash.
                else:
                    global memory_Bank5, memory_Bank6
                    hashOut=memory_Bank5.return_data(db_identifier='MAINSTORAGE',decryptFirst=True, password=memory_Bank6)
                    otherOut = decrypt.hash(password=password)
                    try:
                        if otherOut == hashOut[0]:
                            attemptsCounting=0 # If password is correct, then reset attempts.
                            return True
                    except:
                        # If the hash is incorrect, then add 1 to the attempts.
                        attemptsCounting+=1
                        return False
                return False
        def data_format(data_base=None):
            '''depreciated function'''
            #Returns database type.
            num=check_data(data_base)
            #Call to return data_base type.
            if num == False:
                global data_bases
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        return (data_bases[i])[3]
            if num == True:
                print(errors.cannot_call_func('check.data_format()'))
        def data_base_exists(data_base=None):
            """Checks to see if a database exists.
            Args:
            data_base (str): database name. Not for new database handler."""
            #Check to see if database exists,
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
                    print(errors.cannot_call_func('check.data_base_exists()'))
    class users:
        '''This class is used to manage users. It can be used to create, remove, and modify users. It can also be used to manage user permissions.
        \n- activeStatus
        \n- disable
        \n- enable
        \n- create
        \n- remove
        \n- show_all
        \n- change_permissions
        \n- change_name
        \n- change_password
        \n- return_users
        \n- login_request
        \n- logout
        \n- return_login_cred
        \n- changeID (*)
        \n- setID_to_user_without (*)
        \n- removeID (*)
        \n(*) = Functions in progress. Not Finished.
        '''
        def setBank3(input):
            '''Should be called on startup to allow User accounts to be accessed. Input password used to encrypt data.'''
            global memory_Bank3
            memory_Bank3 = input
        def passwordCryption(input, mode):
            """Input suggested password, returns encrypted password using global password. Uses pyAesCrypt for simplicity.

            Ensure you check output. It may return looking like a list when it's really a string. Ex: ["12314"], but thats actually a string
            
            Args:
            - Modes: 'encrypt' or 'decrypt'
            """

            global memory_Bank3
            if mode == "encrypt":
                return encrypt.database(database=input, password=memory_Bank3, chooseMethod='pyAesCrypt')
            if mode == "decrypt":
                return decrypt.database(database=input, password=memory_Bank3, chooseMethod='pyAesCrypt')
        def changeID():
            '''Changes the ID for a specific user. New ID cannot be already used. Old ID will be available for reassignment after removal.'''
            pass
        def setID_to_user_without():
            '''Gives and ID to a user that has already been made, but without an ID assigned.'''
            pass
        def removeID():
            '''Removes an ID from an account. User still can be used, but cannot be found by and ID anymore.'''
            pass
        def activeStatus(user, hide=False):
            """Returns active status of user. If enabled or not.
            
             - True = Enabled
             - False = Disabled"""
            for i in range(len(known_users)):
                if known_users[i]==user:
                    return active_users[i]
        def disable(user=None, hide=False):
            history.create_history('Run', 'users.disable()', hide=debug)
            num=check_input(user)
            #Disables a user
            if num == False:
                global known_users, active_users
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Disable user', hide=hide)
                        active_users[i]=False
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.disable()'))
        def enable(user=None, hide=False):
            history.create_history('Run', 'users.enable()', hide=debug)
            num=check_input(user)
            #Enables a user
            if num == False:
                global known_users, active_users
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Enable user', hide=hide)
                        active_users[i]=True
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.disable()'))
        def create(new_user=None, new_password=None, new_permission=None, id=None, hide=False):
            '''Creates new users. These users can be used to modify databases and other custom functions.
            \n Arguments:
            \n - new_user (str)= Name of user. Name will be set to .lower()
            \n - new_password (str)= Password of this new user.
            \n - new_permission (str)= Set the permission level. Must be within allowed_users(list) types.
            \n - id (int)= ID for user. Depending on use, this may be easier to work with instead of names.
            
            \nReturns:
            \n - IncorrectPerm - Permission Requested is not in allowed_users within save file.
            \n - PasswordDoesNotMeetReq - Password Doesn\'t meet requirements.
            \n - UserExists - A User with the same name already exists.
            \n - IDMustContainNumbers - A User id must only contain numbers.
            \n - IDExists - A User already has that ID.
            
            \nPassword Requirements:
            \n - 1) Password Min Lnegth: Default 5, min_length
            \n - 2) Password Max Length: Default 25, max_length
            \n - 3) Password can only contain: allowedPassword_chars #To long to list here
            \n - These Vars can be changed and are found in settings.py
            '''
            history.create_history('Run', 'users.create()', hide=debug)
            global known_users, passwords, permissions
            num1=check_input(new_user)
            num2=check_input(new_password)
            try:
                new_user=new_user.lower()
                new_permission=new_permission.lower()
            except:
                pass
            
            # Permission Check
            if new_permission not in allowed_users:
                if hide==False:
                    print(errors.incorrect_perm())
                    return 'IncorrectPerm'
            # Profanifanity filter check
            if profanityFilter.filter(new_user)==1:
                if hide==False:
                    print(errors.profanityDetected(new_user, user=user_logged))
            if profanityFilter.filter(new_password.lower())==1:
                if hide==False:
                    print(errors.profanityDetected(new_password, user=user_logged))
            # Move to create user and more checks.
            if num1 == False and num2 == False and new_permission in allowed_users and profanityFilter.filter(new_user)==0 and profanityFilter.filter(new_password.lower())==0:
                if password_restrictions.check_password(new_password) == 1 or strict_password==False:
                    skip=False
                    for i in range(len(known_users)):
                        if known_users[i]==new_user:
                            skip=True
                            print(errors.user_exists())
                            return 'UserExists'
                    if skip == False:
                        if isinstance(new_user, str) == True:
                            if isinstance(new_password, str) == True:
                                if isinstance(new_permission, str) == True or new_permission==None:
                                    history.create_history(new_user, 'Created user', hide=hide)
                                    known_users.append(new_user)
                                    passw=users.passwordCryption(new_password, mode='encrypt')
                                    passwords.append(passw)
                                    permissions.append(new_permission)
                                    active_users.append(True)
                                    if id != None:
                                        found=False
                                        while found==False:
                                            for i in range(len(ids)):
                                                if ids[i][0] == id:
                                                    found=True
                                            break # If not found, break
                                        if found==True:
                                            if hide==False:
                                                print("User ID already Exists")
                                            return "IDExists"
                                        if found==False: # Id doesn't exist yet
                                            if isinstance(id, int) == True:
                                                ids.append([id, len(known_users)-1, new_user]) # ID, Index for User, Name of User
                                            else:
                                                if hide == False:
                                                    print("ID must only contain Numbers")
                                                return "IDMustContainNumbers"
                                        
                        if isinstance(new_user, str) == False:
                            if hide==False:
                                print('new_user must be str')
                        if isinstance(new_permission, str) == False:
                            if hide==False:
                                print('new_permission must be str')
                        if isinstance(new_permission, str) == False and new_permission != None:
                            if hide==False:
                                print('new_password must be str or None') 
                else:
                    if hide==False:
                        print(errors.doesNotObeyRestrictions())
                        print('Password Min Lnegth:',min_length)
                        print('Password Max Length:',max_length)
                        print('Password can only contain:',allowedPassword_chars)
                        return "PasswordDoesNotMeetReq"
            if num1 == True or num2 == True:
                print(errors.cannot_call_func('users.create()'))
        def remove(user=None, hide=False):
            history.create_history('Run', 'users.remove()', hide=debug)
            print(type(user))
            print('User:'+user+':')
            num=check_input(user)
            if num == False:
                user=user.lower()
                found=False
                global known_users, passwords, permissions
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Removed user', hide=hide)
                        known_users.pop(i)
                        passwords.pop(i)
                        permissions.pop(i)
                        active_users.pop(i)
                        found=True
                        break
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
                    return "UserNotFound"
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.remove()'))
        def show_all():
            history.create_history('Run', 'users.show_all()', hide=debug)
            global known_users
            for i in range(len(known_users)):
                print('User: '+known_users[i])
                print('Permission: '+permissions[i])
        def change_permissions(user=None, new_permission=None, hide=False):
            history.create_history('Run', 'users.change_permission()', hide=debug)
            num1=check_input(user)
            num2=check_input(new_permission)
            if num1 == False and num2 == False:
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Change permission', hide=hide)
                        permissions[i]=new_permission
            if num1 == True or num2 == True:
                if hide==False:
                    print(errors.cannot_call_func('users.change_permissions()'))
        def change_name(user=None, new_name=None, hide=False):
            history.create_history('Run', 'users.change_name()', hide=debug)
            num1=check_input(user)
            num2=check_input(new_name)
            if profanityFilter.filter(new_name)==1:
                if hide==False:
                    print(errors.profanityDetected(var=new_name, user=user_logged))
            if num1 == False and num2 == False and profanityFilter.filter(new_name)==0:
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user+' to '+new_name, 'Change name', hide=hide)
                        known_users[i]=new_name
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num1 == True or num2 == True:
                if hide==False:
                    print(errors.cannot_call_func('users.change_name()'))
        def change_password(user=None, new_password=None, hide=False):
            history.create_history('Run', 'users.change_password()', hide=debug)
            global passwords
            num=check_input(user)
            if profanityFilter.filter(new_password)==1:
                if hide==False:
                    print(errors.profanityDetected(var=new_password, user=user_logged))
            if num == False and profanityFilter.filter(new_password)==0:
                found=False
                for i in range(len(known_users)):
                    if known_users[i]==user:
                        history.create_history(user, 'Change password', hide=hide)
                        passwords[i]=new_password
                        found=True
                if found==False:
                    if hide==False:
                        print(errors.user_not_found())
            if num == True:
                if hide==False:
                    print(errors.cannot_call_func('users.change_password()'))
        def return_users():
            #DO NOT ADD history.create_history() HERE. FOR SECURITY REASONS.
            global known_users
            return known_users
        def login_request(user=None, password=None, hide=False):
            '''All requests are case sensetive
            \n- user - Username
            \n- password - Password for user
            '''
            history.create_history('Run', 'users.login_request()', hide=debug)
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
                                    if hide==False:
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
                                        if hide==False:
                                            print('User is not active.')
                if hide==False:
                    if isinstance(user, str) == False:
                        print(errors.not_str())
                    if isinstance(password, str) == False and password != None:
                        print(errors.not_str())
                    if user not in known_users:
                        print(errors.user_not_found())
                try:
                    if user_logged==False:
                        return False
                except:
                    pass
            if user == None:
                if hide==False:
                    print(errors.cannot_call_func('users.login_request()'))
        def logout(hide=False):
            history.create_history('Run', 'users.logout()', hide=debug)
            global user_logged, user_permission, profanity_filter, disable_filter_admin
            try:
                #If no users is logged in, user_permission will cause an error.
                if user_permission=="admin":
                    if disable_filter_admin==True:
                        profanity_filter=True
                user_permission=None
                user_logged=None
            except:
                #Handles the error and prints a message and/or return(s) it
                if debug==True or hide==False:
                    print("No user signed in.")
                return "UserNotSignedIn"
        def return_login_cred():
            '''Returns 2 vars. No passwords will be shown. This is a secure function.
            \nuser_logged, user_permission'''
            history.create_history('Run', 'users.return_login_cred()', hide=debug)
            try:
                global user_logged, user_permission
                if user_logged==None:
                    return 'UserNotSignedIn', 'UserNotSignedIn'
                else:
                    return user_logged, user_permission
            except:
                return 'UserNotSignedIn', 'UserNotSignedIn'
    class Singleton(type):
        _instances = {}
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
            return cls._instances[cls]

    class data_base_new(metaclass=Singleton):
        """NOTE: THIS CLASS IS IN DEVELOPEMNT PHASE. USE AT RISK. FUNCTIONS MAY CHANGE. 

            \nCurrent Functions:

            \n - return_data
            \n - doesDatabaseExist
            \n - StressTest
            \n - databaseDataDecrypted
            \n - DeleteDatabase
            \n - CreateDatabase
            \n - add_item
            \n - remove_item
            \n - merge_Database
            \n - MergeAllDatabases
            \n - split_databases
            \n - get_database (Testing Only)
            \n - get_sub_database (Testing Only)
            \n - search (Testing Only)
            \n - database_size (Not Finished)
            \n - update_item (Not Finished)
            \n - backup_databases (Not Finished)
            
            \nSpecifications:
            \n- (-p) -Priority(Bank 5) Not Finished
            \n- (-ignorEncryption) Not Finished
            \n- (-B6) -  Saves Bank6 inside instance
            """
        def __init__(self):
            self.databases = []
            self.args = []
            self.banks = []
            self.stress_test = self.StressTest
            self.DatabaseDataDecrypted = self.databaseDataDecrypted
            self.create = self.CreateDatabase
            self.delete = self.DeleteDatabase
            self.edit_add_item = self.add_item
            self.edit_remove_item = self.remove_item
            self.merge = self.merge_Database
            self.__doc__ = self.__class__.__doc__


        def callPriority(self, input=None):
            """Not for normal database use.
            Args:
            
            -input (list): List all args to append"""
            for i in range(len(input)): self.args.append(input[i]) # Creates a list before normal list.

        def load(self, input):
            """Import all data to instance instead of recreating manually.
            
            Args:
            input (str/list): The data to be placed as is inside the handler.
            
            input:
                if str: str is converted to list. Ex: '[Database [data] etc...]' to [Database [data] etc...]
                if list: database uses .append()
            
            Simple Function.
            """
            if type(input) == list:
                self.databases().append(input)
            if type(input) == str:
                self.databases().append(list(input))


        def return_data(self, db_identifier, decryptFirst=False, returnStatement=False, password=None):
            '''Returns all databases within instance.'''
            if isinstance(db_identifier, str):
                db_index = next((index for index, db in enumerate(self.databases) if (db[0]) == db_identifier), None)
                if db_index is None:
                    raise Exception(f"No database named '{db_identifier}' found.")
            elif isinstance(db_identifier, int):
                db_index = db_identifier
                if db_index < 0 or db_index >= len(self.databases):
                    raise Exception(f"No database at index {db_index}.")
            else:
                raise TypeError("db_identifier must be a string (name) or integer (index).")
            if type(db_identifier) == int:
                db_identifier = self.databases[db_index][0]
            if type(db_identifier) == str:
                for i in range(len(memory_Bank4)):
                    if memory_Bank4[i][3] == db_identifier:
                        data = self.databases[db_index][1]
                        return decrypt.database(ciphertext = data, nonce=memory_Bank4[i][0], tag=memory_Bank4[i][1], key=memory_Bank4[i][2], password=password, returnStatement=returnStatement)
        
        def doesDatabaseExist(self, db_identifier):
            '''Returns True if database exists. False if not.'''
            for i in range(len(self.databases)):
                if self.databases[i][0]==db_identifier:
                    return True
            return False
        
        def StressTest(self, n, db_identifier, timeWait=.000, returnTimeTaken=False, displayIterations=False, password=None):
            """Loads a database with tons of useless data to see how it reacts. Indexing is not allowed in this function.
            Args:
             - n (int): How many bogus entries should be added?
             - db_identifier (str): What's the name of this database?
             - timeWait (float): How long between each write? Good for limiting cpu consumption. Fine tuning is needed.
             - returnTimeTaken (bool): Return the time taken from call function to close function. If timeWait: (time.time()-startTime) - (timeWait * n)
             - displayIterations (bool): Display each iteration. Good for debugging. Not reccomended for large n.
            """
            if "-p" not in self.args:
                fOuth= decrypt.hash(password) # Get hash
                if check.verifyHash(fOuth) == True: # Verify hash
                    password=fOuth
            if "-p" in self.args:
                # Allows password
                pass
            if password != None:
                print('Please Note: Encryption heavily slows down iteration speeds. New method, deployed which increases speed. But it\'s still slow.')
            if returnTimeTaken:
                startTime=time.time()
            for i in range(n):
                if displayIterations:
                    print(f"Running iteration {i+1} of {n}")
                self.add_item(db_identifier=db_identifier, item='Tacos! BRO AAHHHH', password=password)
                if timeWait != .000: # Restrictor. To limit usage of the current thread. Or lower resources.
                    time.sleep(timeWait)
            if returnTimeTaken:
                return (time.time()-startTime) - (timeWait * n)
        
        def databaseDataDecrypted(self, db_identifier, password):
            '''Returns decrypted database data.
            
            Args:
            db_identifier (str or int): The name or index of the database.
            password (str): The password to decrypt the database with.
            
            Return Values:
            List: The contents of the decrypted database.
            
            Note: This function only returns entires side of the database. It does not return the name or if it's encrypted.'''
            if "-p" not in self.args:
                fOuth= decrypt.hash(password) # Get hash
                if check.verifyHash(fOuth) == True: # Verify hash
                    password=fOuth
            if "-p" in self.args:
                # Allows password
                pass
            for i in range(len(self.databases)):
                if self.databases[i][2]==True:
                    if isinstance(self.databases[i][1], list) and isinstance(self.databases[i][1][0], list):
                        self.databases[i][1] = sum(self.databases[i][1], [])
                    self.databases[i][1]=decrypt.database(self.databases[i][1], decrypt.hash(password))
        
        def DeleteDatabase(self, db_identifier, password=None):
            """Deletes a database by its name or index.

            Args:
            db_identifier (str or int): The name or index of the database to delete.
            password (str): Password, if required, to delete the database.

            Returns:
            False: If database could not be deleted.
            """
            # Password is needed to delete the database if it's encrypted. Other wise it's not needed.
            if "-p" not in self.args:
                fOuth= decrypt.hash(password) # Get hash
                if check.verifyHash(fOuth) == True: # Verify hash
                    password=fOuth
            if "-p" in self.args:
                # Allows password
                pass
            global memory_Bank4
            if isinstance(db_identifier, str):
                db_index = next((db[3] for db in self.databases if db[0] == db_identifier), None)
                if db_index is None:
                    raise Exception(f"No database named '{db_identifier}' found.")
            elif isinstance(db_identifier, int):
                db_index = next((db[3] for db in self.databases if db[3] == db_identifier), None)
                if db_index is None:
                    raise Exception(f"No database at index {db_identifier}.")
            else:
                raise TypeError("db_identifier must be a string (name) or integer (index).")
            if self.databases[db_index][2]:
                if password == None:
                    raise Exception("Cannot delete an encrypted database without password.")
                else:
                    if self.return_data(db_identifier=db_identifier, decryptFirst=True, password=password, returnStatement=True) == True:
                        # Delete database
                        del self.databases[db_index]
                        # Now remove it from memory_Bank4
                        tpm=0
                        for i in range(len(memory_Bank4)):
                            if memory_Bank4[i-tpm][3] == db_identifier:
                                memory_Bank4.pop(i)
                                tpm=1
                        for i in range(len(self.databases)):
                            self.databases[i][3]-=1
                    else:
                        raise Exception("Password is incorrect. Cannot delete database.")

            else: # No encryption
                del self.databases[db_index]
                for i in range(len(self.databases)):
                    self.databases[i][3]-=1
        
        def CreateDatabase(self, db_identifier, entries, password):
            """Creates a new database with the given name and entries and stores it in data_base.

            Args:
            db_identifier (str): The name of the database.
            entries (list): The entries in the database.
            password (str, optional): Must have the -p argument.
            
            Returns:
            Index (int): Where the database is stored in self.databases.
            """
            if "-p" not in self.args:
                fOuth= decrypt.hash(password) # Get hash
                if check.verifyHash(fOuth) == True: # Verify hash
                    password=fOuth
            if "-p" in self.args:
                # Allows password
                pass
            if password is not None:
                global memory_Bank4
                cypher, nonce, tag, key = encrypt.database(database=entries, password=password)
                memory_Bank4.append([nonce, tag, key, db_identifier]) 
                #entries = encrypt.database(entries, password)
                new_database = [db_identifier, cypher, password is not None, len(self.databases)]
            else:
                new_database = [db_identifier, entries, password is not None, len(self.databases)]
            self.databases.append(new_database)
            return len(self.databases) - 1

        def add_item(self, db_identifier, item, sub_db_index=None, password=None):
            """Adds an item to a sub-database. sub-databases are rejoined when the application is requested to shutdown or save.

            Args:
            db_identifier (str or int): The name or index of the database.
            item (str): The item to add.
            password (str): The password, if required, to use this database.
            sub_db_index (int, optional): The index of the sub-database. If None, the item is added to the last sub-database.
            """
            if "-p" not in self.args:
                fOuth= decrypt.hash(password) # Get hash
                if check.verifyHash(fOuth) == True: # Verify hash
                    password=fOuth
            if "-p" in self.args:
                # Allows password
                pass
            if isinstance(db_identifier, str):
                db_index = next((index for index, db in enumerate(self.databases) if (db[0]) == db_identifier), None)
                if db_index is None:
                    raise Exception(f"No database named '{db_identifier}' found.")
            elif isinstance(db_identifier, int):
                db_index = db_identifier
                if db_index < 0 or db_index >= len(self.databases):
                    raise Exception(f"No database at index {db_index}.")
            else:
                raise TypeError("db_identifier must be a string (name) or integer (index).")

            if sub_db_index is None:
                sub_db_index = len(self.databases[db_index]) - 1
            if isinstance(self.databases[db_index][sub_db_index], list):
                self.databases[db_index][sub_db_index].append(str(item))
            else:
                #print("Error: Target is not a list.", db_index, sub_db_index)
                try:
                    if self.databases[db_index][2] == True: # If encrypted
                        global memory_Bank4
                        if type(db_identifier) == int:
                            db_identifier = self.databases[db_index][0]
                        if type(db_identifier) == str:
                            for i in range(len(memory_Bank4)):
                                if memory_Bank4[i][3] == db_identifier:
                                    data = self.databases[db_index][1]
                                    datadecrypt = decrypt.database(ciphertext= data, nonce=memory_Bank4[i][0], tag=memory_Bank4[i][1], key=memory_Bank4[i][2], password=password)
                                    datadecrypt.append(str(item))
                                    # Now re-encrypt it.
                                    [cypher, nonce, tag, key] = encrypt.database(database=datadecrypt, password=password)
                                    # Edit memory_Bank
                                    memory_Bank4[i] = [nonce, tag, key, db_identifier]
                                    self.databases[db_index][1] = cypher
                        #dataUsable = decrypt.database(database=self.databases[db_index][1], password=password) # Decrypt database, store as temp var
                        #self.databases[db_index][1] = encrypt.database(database=dataUsable, password=password) # Re encrypt and append new encryption with new entry to database,
                    else: # Not encrypted
                        self.databases[db_index][1].append(str(item))
                except Exception as r:
                    print('Error: Could not add item to database. Error', r)

        def remove_item(self, db_identifier, item, sub_db_index=None, password=None):
            """Removes an item from a sub-database. sub-databases are rejoined when the application is requested to shutdown or save.

            Args:
            db_identifier (int or str): The index of the database.
            item: The item to remove.
            sub_db_index (int, optional): The index of the sub-database. If None, the item is removed from the last sub-database.
            """
            if "-p" not in self.args:
                fOuth= decrypt.hash(password) # Get hash
                if check.verifyHash(fOuth) == True: # Verify hash
                    password=fOuth
            if "-p" in self.args:
                # Allows password
                pass
            if isinstance(db_identifier, str):
                db_index = next((db[3] for db in self.databases if db[0] == db_identifier), None)
                if db_index is None:
                    raise Exception(f"No database named '{db_identifier}' found.")
            elif isinstance(db_identifier, int):
                db_index = next((db[3] for db in self.databases if db[3] == db_identifier), None)
                if db_index is None:
                    raise Exception(f"No database at index {db_identifier}.")
            try:
                if sub_db_index is None:
                    sub_db_index = len(self.databases[db_index]) - 1
                self.databases[db_index][sub_db_index].remove(item)
            except:
                # If not sub_db_index
                #self.databases[db_index][1].remove(item)
                if self.databases[db_index][2] == True: # If encrypted
                    if password != None:
                        datadecrypt = self.return_data(db_identifier=db_identifier, decryptFirst=True, password=password)
                        datadecrypt.remove(str(item))
                        # Now re-encrypt it.
                        [cypher, nonce, tag, key] = encrypt.database(database=datadecrypt, password=password)
                        # Edit memory_Bank
                        db_name = self.databases[db_index][0]
                        db_nameIndexbank = next((index for index, db in enumerate(memory_Bank4) if (db[3]) == db_name), None)
                        memory_Bank4[db_nameIndexbank] = [nonce, tag, key, db_identifier]
                        self.databases[db_index][1] = cypher
                    else:
                        raise Exception('Password is required to remove item from encrypted database.')
        
        def merge_Database(self, db_index):
            """Merges a single split database back into a single list.

            Args:
            db_index (int): The index of the database to merge, if none is given, all databases are merged.
            """
            self.databases[db_index] = sum(self.databases[db_index], [])

        def MergeAllDatabases(self):
            '''Merges all databases. Index input not needed.'''
            for i in range(len(self.databases)): # For amount of databases
                data_base_new.merge_Database(db_index=i) # Call with i as index, +1 after each run

        def split_databases(self):
            """Splits all databases that are too large."""
            for i in range(len(self.databases)):
                if len(self.databases[i]) > self.split_size:
                    self.databases[i] = self.split_database(self.databases[i])

        def get_database(self, index):
            """Gets a database by its index."""
            return self.databases[index]

        def get_sub_database(self, db_index, sub_db_index):
            """Gets a sub-database by its index and the index of its parent database."""
            return self.databases[db_index][sub_db_index]

        # Other features that will be created and finalized!

        # Basic Features that need addinital code to work with encryption
        # Check to see if an item/entry exists!
        def search(self, item, db_name=None, caseInsensative=True, password=None):
            """Check db_name if item is in db_name as entry.
            Args:
            item (str): The item your looking for.
            db_name (str or int): The database Index or Name
            caseInsensative (bool): caseInsensative (bool): This means that if you're searching for "item", it should match with "Item", "ITEM", "item", etc.
            password (str): The password, if required, to use this database.

            Return:
            True: Item found
            False: Else, Not found
            """
            
            # If db_name is int
            if type(db_name) == int:
                db=self.databases[db_name]
                if db[2] == True: # If encrypted
                    dataUsable = decrypt.database(db[1], password=password)
                    if item in dataUsable:
                        return True
                else: # If not encrypted
                    if item in db[1]:
                        return True

            # If db_name is str
            elif type(db_name) == str:
                for db in self.databases:
                    if db[0] == db_name:
                        if db[2] == True:
                            dbtemp = decrypt.database(db[1], password=password)
                            print(dbtemp)
                            tempdata=[]
                            for i in range(len(dbtemp)):
                                tempdata.append(dbtemp[i].lower())
                                if caseInsensative==True:
                                    if item.lower() in tempdata:
                                        return True
                                else:
                                    if item in dbtemp:
                                        return True
                        else:
                            if caseInsensative==True:
                                if item.lower() in db[1]:
                                    return True
                            else:
                                if item in db[1]:
                                    return True

            else:
                print('Classifaction not allowed!!')

            return False # Nothing was mathed, so return False

        # Reports the size of the database selected.
        def database_size(self, db_identifier=None):
            if db_identifier is None:
                return sum(len(db) for db in self.databases)
            else:
                db_index = self.get_db_index(db_identifier)
                return len(self.databases[db_index])
        
        # Made a mistake, no problem!
        def update_item(self, db_identifier, old_item, new_item):
            self.remove_item(db_identifier, old_item)
            self.add_item(db_identifier, new_item)

        # Backup current database that's managed by an instance!
        def backup_databases(self, backup_file):
            with open(backup_file, 'w') as f:
                json.dump(self.databases, f)

    class data_base:
        def help():
            print('Branches:\n  data_base.edit\n  data_base.empty\n  data_base.show\n  data_base.remove\n  data_base.create')
        class edit:
            def split_database(database, split_size):
                """Splits a large database into smaller lists.

                Args:
                database (list): The database to split.
                split_size (int): The size of the smaller lists.

                Returns:
                list: A list of smaller lists.
                """
                return [database[i:i + split_size] for i in range(0, len(database), split_size)]
            def help():
                print('Branches:\n  data_base.edit.search_rows()\n  data_base.edit.check_owner()\n  data_base.edit.add_row_term()\n  data_base.edit.add_item()\n  data_base.edit.remove_row()\n  data_base.edit.add_column()\n  data_base.edit.remove_column()')
            def search_rows(data_base=None, id=None, database=None):
                '''Search Rows in database to fine if (id) can be found. Returns 1 if found, 0 if not.'''
                if data_base == None:
                    data_base=database
                if isinstance(data_base, str) == True and isinstance(id, str) == True:
                    for i in range(len(row)):
                        if (row[i])[0] == data_base:
                            if ((row[i])[1])[1]==id:
                                return 1
                    return 0
            def check_owner(data_base=None, user_perm=None, database=None):
                '''Returns 1 is owner matches the database. Returns 0 if not.'''
                if data_base == None:
                    data_base=database
                #Returns 1 is owner matches the database.
                if isinstance(data_base, str) == True and isinstance(user_perm, str) == True:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[2] == user_perm:
                            return 1
                    return 0
            def add_row_term():
                '''Only for terminal use.'''
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
            def add_item(data_base=None, item_to_add=None, create_if_notExist=True, database=None, hide=False):
                if data_base == None:
                    data_base=database
                try:
                    history.create_history(item_to_add, 'Add item', hide=hide)
                except:
                    pass
                #Used for the list types.
                global data_bases, lists
                num1=check_input(data_base)
                num2=check_input(item_to_add)
                pass_it=False
                try:
                    if profanityFilter.filter(item_to_add[0])==1:
                        print(errors.profanityDetected(var=item_to_add[0], user=user_logged))
                        pass_it=True
                        try:
                            if profanityFilter.filter(item_to_add[1])==1:
                                print(errors.profanityDetected(var=item_to_add[1], user=user_logged))
                                pass_it=True
                        except:
                            pass
                except:
                    pass
                if check.data_base_exists(data_base='logs')==True:
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
                                if (data_bases[i+letter_spot])[3]=="list":
                                    for x in range(len(lists)):
                                        if (lists[x])[0]==data_base:
                                            (lists[x])[1].append(item_to_add)
                                            break
                    if num1==True or num2==True and pass_it==False:
                        if hide==False:
                            print(errors.cannot_call_func('data_base.edit.add_item()'))
                else:
                    if hide==False:
                        print(errors.database_does_not_exist())
            def remove_item(data_base=None, item_to_remove=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                history.create_history(item_to_remove, 'Remove item', hide=hide)
                #Used for the list types.
                num1=check_input(data_base)
                num2=check_input(item_to_remove)
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
            def add_row(data_base=None, new_row=None, split=True, database=None, hide=False):
                '''Adds a new Row to a database.
                
                Args:
                - data_base (str): Name of database
                - new_row (list): New Row in list format'''
                if data_base == None:
                    data_base=database
                if isinstance(new_row, str)==True:
                    history.create_history(new_row, 'Add row', hide=hide)
                #You can add as many objects to a row as you please, but it may not fit in your assinged constraints. No problems will occur though.
                if split==True and isinstance(new_row, str):
                    new_row=new_row.split()
                #print(new_row)
                num1=check_input(data_base)
                num2=check_input(new_row)
                if num1 == False and num2 == False:
                    data_base=data_base.lower()
                    if isinstance(new_row, list) == True:
                        row.append([data_base,new_row])
                        #print("Added new row!")
                    if isinstance(new_row, list) == False:
                        print(errors.not_list())
                if num1 == True or num2 == True:
                    print(errors.cannot_call_func('data_base.edit.add_row()'))
            def remove_row(data_base=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                num1=check_input(data_base)
                if num1 == False:
                    data_base=data_base.lower()
                    history.create_history(data_base, 'Remove row', hide=hide)
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
            def add_column(data_base=None, column_name=None, database=None, hide=False):
                '''Add a column to the database.
                
                Args:
                - data_base (str): Name of database
                - column_name (str): Name of new Column'''
                if data_base == None:
                    data_base=database
                history.create_history(column_name, 'Add column', hide=hide)
                letter_spot=optimize.determ(letter=data_base[0], set='opto_data')
                num1=check_input(data_base)
                num2=check_input(column_name)
                global debug, data_bases
                if profanityFilter.filter(column_name) == 1:
                    print(errors.profanityDetected(var=column_name, user=user_logged))
                else:
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
            def remove_column(data_base=None, column=None, remove_row=False, database=None, hide=False):
                if data_base == None:
                    data_base=database
                try:
                    history.create_history(column, 'Remove Column', hide=hide)
                    num1=check_input(data_base)
                    num2=check_input(column)
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
            #Used for my carpentry app.
            class app:
                def rmBrokenTools():
                    a=0
                    for i in range(len(row)):
                        if (row[i-a])[0]=="tools":
                            try:
                                if ((row[i-a])[1])[6]==True:
                                    ((row[i-a])[1]).pop()
                                    a+=1
                            except:
                                pass
                    return "DONE"
                def remove_row(data_base=None, name=None, database=None, hide=False):
                    if data_base == None:
                        data_base=database
                    found=False
                    if isinstance(name, str) == True and isinstance(data_base, str) == True:
                        global row
                        for i in range(len(row)):
                            if (row[i])[0] == data_base:
                                if ((row[i])[1])[2] == name:
                                    row.pop(i)
                                    found=True
                                    break
                    else:
                        if hide==False:
                            print(errors.not_str())
                    return found
                def remove_item(data_base=None, barcode=None, database=None):
                    if data_base == None:
                        data_base=database
                    if isinstance(data_base, str) == True and isinstance(barcode, str) == True:
                        global lists
                        for i in range(len(lists)):
                            if (lists[i])[0]==data_base:
                                for x in range(len((lists[i])[1])):
                                    if (((lists[i])[1])[x])[0]==barcode:
                                        ((lists[i])[1]).pop(x)
                                        return True
                        return False
                    else:
                        print(errors.not_str())
                def show_tools(data_base=None, database=None):
                    if data_base == None:
                        data_base=database
                    if isinstance(data_base, str) == True:
                        for i in range(len(row)):
                            print('Item:',((row[i])[1])[0],' | Serial:',((row[i])[1])[1])
        class empty:
            def help():
                print('Branches:\n  data_base.empty.all()\n  data_base.empty.one()')
            #Clear all info in 1 or more databases.
            def all(hide=False):
                '''Reset all data compiled for all databases.'''
                history.create_history(None, 'Reset all databases', hide=hide)
                global lists, row
                lists=[]
                row=[]
            def one(data_base=None, recall=False, database=None):
                '''Reset all data compiled for a single database.'''
                if data_base == None:
                    data_base=database
                #Empty all data compiled for one database.
                if recall==False:
                    num1=check_input(data_base)
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
        class retrieve:
            def databases():
                '''Returns names of all known databases.'''
                list = []
                for i in range(len(data_bases)):
                    list.append((data_bases[i])[0])
                return list
        class look_up:
            def row(database, column, value):
                '''Returns row depending on input factors. Look inside a database for a specific row, with the row having the column and value. The row found is returned in list format.'''
                global row
                for i in range(len(row)):
                    if (row[i])[0]==database:
                        if (row[i])[1][column]==value:
                            return (row[i])[1]

        class show:
            def help():
                print('Branches:\n  data_base.show.show_column()\n  data_base.show.show_row()\n  data_base.show.show_lists()\n  data_base.show.all_in_database()\n  data_base.show.all_data_bases()\n  data_base.show.info()')
            def show_column(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                if num == False:
                    for i in range(len(data_bases)):
                        if (data_bases[i])[0]==data_base:
                            if (data_bases[i])[3]=="column_row":
                                print((data_bases[i])[4])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_column()'))
            def show_row(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                #Must be column_row type
                global row
                if num == False:
                    for x in range(len(row)):
                        if (row[x])[0]==data_base:
                            print((row[x])[1])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_row()'))
            def show_lists(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                global lists
                if num == False:
                    for x in range(len(lists)):
                        if (lists[x])[0]==data_base:
                            print(lists[x])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.show_lists'))
            def all_in_database(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
                global data_bases, row, debug, sets, rows, type
                sets=[]
                rows=[]
                type=None
                if num == False:
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
                        if multi_process==False:
                            for x in range(len((data_bases[i])[4])):
                                sets.append(((data_bases[i])[4])[x])
                            for n in range(len(row)):
                                if (row[n])[0] == data_base:
                                    rows.append((row[n])[1])
                            print(sets)
                            for i in range(len(rows)):
                                print(rows[i])
                    if type == "list":
                        for i in range(len(lists)):
                            if (lists[i])[0]==data_base:
                                print((lists[i])[1])
                if num == True:
                    print(errors.cannot_call_func('data_base.show.all()'))
            def all_data_bases():
                global data_bases
                print('Known databases:')
                for i in range(len(data_bases)):
                    print('  ',(data_bases[i])[0])
            def info(data_base=None, database=None):
                if data_base == None:
                    data_base=database
                num=check_input(data_base)
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
            def help():
                print('Branches:\n  data_base.remove.all()\n  data_base.remove.one_set()\n  data_base.remove.reset_to_standard()')
            def all(hide=False):
                history.create_history(None, 'Remove All', hide=hide)
                global data_bases, row, lists
                data_bases=[]
                lists=[]
                row=[]
            def one_set(data_base=None, database=None, hide=False):
                if data_base == None:
                    data_base=database
                history.create_history(None, 'Remove One Set', hide=hide)
                num=check_input(data_base)
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
            def reset_to_standard(hide=False):
                history.create_history(None, 'Reset to Standard', hide=hide)
                try:
                    os.remove('data_save.py')
                except:
                    pass
        class create:
            def help():
                print('Branches:\n  data_base.create.database()')
            def database(data_base=None, database=None, status=True, type=None, owner='all', columns=None, hide=False):
                '''Create a new database.
                
                Args:
                - database (str): Name of Database
                - status (bool): Should it be active? True=Yes
                - type (str): Type of database: list or column_row
                - owner (str): all=Everyone, Else Name required.
                - columns (list): Give it Data to hold after creation.
                '''
                if data_base == None:
                    data_base=database
                history.create_history(data_base, 'Create Database', hide=hide)
                found1=False
                found2=False
                found3=False
                print(data_base)
                #Check to see if database already exists.
                for i in range(len(data_bases)):
                    if (data_bases[i])[0]==data_base:
                        if hide==False:
                            print('That database already exists.')
                        found1=True
                        break
                if type not in allowed_types:
                    if hide==False:
                        print('An incorrect data type has been entered.')
                    found2=False
                if type in allowed_types:
                    found2=True
                for i in range(len(data_base)):
                    if data_base[i] in alphabet:
                        found3=True
                    if data_base[i] not in alphabet:
                        found3=False
                        if hide==False:
                            print('Database name can only consist of lowercase letters.')
                        break
                #Check database for profanity.
                if profanityFilter.filter(data_base)==1:
                    if hide==False:
                        print(errors.profanityDetected(var=data_base, user=user_logged))
                else:
                #If database doesn't exist continue on creating it.
                    if found3 == True and found2 == True and found1 == False:
                        if hide==False:
                            print('Database created!')
                        num1=check_input(data_base)
                        num2=check_input(type)
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
        class get:
            def rows(data_base=None, database=None):
                '''Returns all rows Corrolated to that database'''
                pass
            def Column(database=None, column_name=''):
                '''Returns all data Corrolated to that column'''
                # Note column data is stored inside (data_bases) var. While rows are stored inside (row) var.
                #  --- Get columns ---
                database=database.lower()
                columns=None
                for i in range(len(data_bases)):
                    if (data_bases[i])[0] == database: # if db Found...
                        columns=(data_bases[i])[4] # Column info
                        break
                if columns is None:
                    print('Database not found.')
                    return None

                # --- Get index ---
                index = -1
                for i in range(len(columns)):
                    if columns[i] == column_name.lower():
                        index = i
                        break
                if index == -1:
                    print('Column not found.')
                    return None

                # --- Get data now!! ---
                columnLength=len(columns) # Saves compute if pre render amount is set before going through rows. If we len() each row instead, the speed would decrease significantly over time.
                # Now return all data for index from lists list[index
                indexedlist=[]
                for i in range(len(row)):
                    if row[i][0] == database:
                        indexedlist.append(row[i][1][index])
                if indexedlist==[]:
                    print('Returned Nothing...')
                return indexedlist
                
    class password_restrictions:
        def help():
            print('Branches:\n  password_restrictions.check_password()\n  password_restrictions.set_min_length()\n  password_restrictions.set_max_length()')
        def check_password(password):
            pass_1=0
            if len(password)>min_length-1 and len(password)-1<max_length:
                for i in range(len(password)):
                    if password[i] in allowedPassword_chars:
                        pass_1=1
                    else:
                        print('Incorrect Item:',password[i])
                        return 0
            return pass_1
        def set_min_length(value=None, hide=False):
            global min_length
            history.create_history(str(value), 'Set min length', hide=hide)
            num=check_input(value)
            #Check if value is a number
            if num==False and isinstance(value, int) == True:
                #Assign new value
                 min_length=value
            if isinstance(value, int) == False:
                print(errors.not_int(item='value'))
            if num == True:
                print(errors.cannot_call_func('password_restrictions.set_min_length()'))
        def set_max_length(value=None, hide=False):
            global min_length, max_length
            history.create_history(str(value), 'Set max length', hide=hide)
            num=check_input(value)
            #Check if value is a number
            if num == False and isinstance(value, int) == True:
                #Check to see if value is bigger than min_length
                if value>min_length:
                    #Assign new value
                    max_length=value
                else:
                    print('')
            if num == True:
                print(errors.cannot_call_func('password_restrictions.set_max_length()'))
    class errors:
        def help():
            print('Branches:\n  errors.MissingCPP()\n  errors.FileDoesNotExist()\n  errors.NotSignedIn()\n  errors.BackupNameExists()\n  errors.profanityDetected()\n  errors.doesNotObeyRestrictions()\n  errors.database_does_not_exist()\n  errors.cannot_call_func()\n  errors.incorrect_perm()\n  errors.user_exists()\n  errors.user_not_found()\n  errors.not_list()\n  errors.not_str()\n  errors.not_bool()\n  errors.not_int()')
        def MissingCPP():
            global UtilizeCPPCode
            UtilizeCPPCode=False
            return ("Missing CPP File. Compile the file 'hello.cpp' as a shared library or import the libfoo.so file to the app root folder.") 
        def FileDoesNotExist(var):
            history.create_history(var, 'FileDoesNotExist', manual_record=auto_error_record, hide=debug)
            print('(Error) File does not exist.')
        def NotSignedIn():
            history.create_history('None', 'NotSignedIn', manual_record=auto_error_record, hide=debug)
            print('(Error) No user is signed in to allow this function to work.')
        def BackupNameExists():
            history.create_history('admin', 'BackupNameExists', manual_record=auto_filter_profanity, hide=debug)
            print('(Error) A backup with the same name already exists.')
        def profanityDetected(var, user):
            try:
                history.create_history(user, 'profanityDetected', manual_record=auto_error_record, add_desc=True, desc=user+' tried to use a curse word known as: '+var, hide=debug)
            except:
                print(errors.cannot_call_func('<Null>'))
            print('Not Alllowed: ',var)
        def doesNotObeyRestrictions():
            history.create_history('doesNotObeyRestrictions', 'Error', manual_record=auto_error_record, hide=debug)
            return('(Error) Password given does not meet the requirments.')
        def database_does_not_exist():
            history.create_history('database_does_not_exist', 'Error', manual_record=auto_error_record, hide=debug)
            return '(Error) Database requested could not be found.'
        def cannot_call_func(var):
            history.create_history('cannot_call_func', 'Error', manual_record=auto_error_record, hide=debug)
            return '(Error) The function '+var+' that was called is missing 1 or more required variables.'
        def not_list(item=None):
            history.create_history('not_list', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A list was expected, but was not given.'
            if item != None:
                return '(Error) A list was expected, but was not given. Item: '+str(item)
        def user_not_found():
            history.create_history('user_not_found', 'Error', manual_record=auto_error_record, hide=debug)
            return '(Error) The user specified was not found.'
        def not_str(item=None):
            history.create_history('not_str', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A string was expected, but was not given.'
            if item != None:
                return '(Error) A string was excepted, but was not given. Item: '+str(item)
        def user_exists():
            history.create_history('user_exists', 'Error', manual_record=auto_error_record, hide=debug)
            return('(Error) This user already exists.')
        def not_bool(item=None):
            history.create_history('not_bool', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A bool was expected, but was not given.'
            if item != None:
                return '(Error) A bool was expected, but was not given. Item: '+str(item)
        def not_int(item=None):
            history.create_history('not_int', 'Error', manual_record=auto_error_record, hide=debug)
            if item==None:
                return '(Error) A int was expected, but was not given.'
            if item != None:
                return '(Error) A int was expected, but was not given. Item: '+str(item)
        def incorrect_perm():
            history.create_history('incorrect_perm','Error', manual_record=auto_error_record, hide=debug)
            return '(Error) The permission requested is not allowed.'
    if profanity_filter==True:
        profanityFilter.setup()
    if allow_windows_version == "11":
        allow_windows_version="10"
        #Windows 11 still thinks it's windows 10. I know, it's weird.
    if optimize_on_startup==True:
        optimize.run(hide=debug)
        #Optmize on startup if setting is set to True.
    if app_version_control==True and "-skipVersionCheck" not in n:
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
        if quiteStartup == False:
            print('Invalid setting. system=')
        history.create_history(usage='Invalid Setting', user='system=Error()', hide=debug)
    from sys import platform
    if platform == "linux" or platform == "linux2":
        if quiteStartup == False:
            print('OS: Linux Distro.')
        systemDetectedOperatingSystem='linux'
        #Linux
        if system != "linux" and set_operating_system==True:
            if quiteStartup == False:
                print('Incorrect OS')
            history.create_history(usage='Operating System Exception', user='linux', hide=debug)
            exit()
    elif platform == "darwin":
        if quiteStartup == False:
            print('OS: Mac OS')
        systemDetectedOperatingSystem='macos'
        # OS X
        if system != "macos" and set_operating_system==True:
            if quiteStartup == False:
                print('Incorrect OS')
            history.create_history(usage='Operating System Exception', user='macos')
            exit()
    elif platform == "win32":
        if quiteStartup == False:
            print('OS: Windows')
        systemDetectedOperatingSystem='windows'
        # Windows
        if system != "windows" and set_operating_system==True:
            if quiteStartup == False:
                print('Incorrect OS')
            history.create_history(usage='Operating System Exception', user='windows', hide=debug)
            exit()
    if setup_backup_response==True:
        if os.path.exists('count.py')==False:
            file=open('count.py','w')
            file.write('backup_count='+str(backup_startNumber))
            file.close()
            backup_count=backup_startNumber
    if quiteStartup == False:
        print('Cleaning Up Junk Files...')
    if clearHistoryOnStartup == True:
        try:
            os.remove('history.txt()')
            history.create()
        except:
            pass
    try:
        os.remove('barcode.png')
    except:
        pass
    if os.path.exists('backups')==False:
        os.mkdir('backups')
    # Remove 'hash.txt' if it exists
    try:
        os.remove('hash.txt')
    except FileNotFoundError:
        pass

    # If 'history_desc.py' doesn't exist, clear the history
    if not os.path.exists('history_desc.py'):
        history.clear()

    # Initialize history_id and history_description
    history_id = []
    history_description = []

    # Initialize count
    count = 0

    # If 'data_save.py' exists, remove 'data_save.aes'
    if os.path.exists('data_save.py'):
        try:
            os.remove('data_save.aes')
        except FileNotFoundError:
            pass

    # If 'history.txt' exists, remove 'history.aes'
    if os.path.exists('history.txt'):
        try:
            os.remove('history.aes')
        except FileNotFoundError:
            pass

    # If resetCollections is True and 'collections' exists, remove it
    if resetCollections and os.path.exists('collections'):
        shutil.rmtree('collections')

    # If 'collections' doesn't exist, create it
    if not os.path.exists('collections'):
        os.mkdir('collections')

    # If 'data_save.aes' is empty, remove it
    try:
        if open('data_save.aes', 'r').read() == "":
            os.remove('data_save.aes')
    except FileNotFoundError:
        pass

    # If 'history.aes' is empty, remove it
    try:
        if open('history.aes', 'r').read() == "":
            os.remove('history.aes')
    except FileNotFoundError:
        pass

    # If quiteStartup is False, check settings and setup profanity filter
    if not quiteStartup:
        print('Checking Settings...')
        check_settingsImproved(hide=logic.gate.not_gate(show_incorrect_settings))
        if profanity_filter:
            print('Setting Up Profanity Filter...')
            profanityFilter.setup()
        print('\nSystem Started Correctly!')

    # Print the startup time
    startup_time = round(time.time() - startupCount, 2)
    if not quiteStartup:
        print(f'Est StartUp Time: {startup_time if startup_time >= .01 else f"{startup_time}<"}')
    try:
    # Check if "-release" is in the command line arguments
        if "-release" in n:
            # Ask the user if this is a Beta or Full release
            while True:
                release_type = input("(1)Beta\n(2)Full\nIs this a Beta or Full release: ")
                if release_type in ["1", "2"]:
                    break

            # If it's a Beta release, ask for the beta version
            beta_version = ''
            if release_type == "1":
                release_type = "Beta"
                beta_version = input('What beta version is this: Ex: 1, 2, 3: ')
            elif release_type == "2":
                release_type = 'Full'

            # Ask for the version number
            version_number = input('Enter the Version: Ex: 0.2.7 or hit enter: ')
            if version_number == "":
                version_number = program_version

            # Set the backup name
            backup_name = f"{version_number} {release_type} {beta_version}" if beta_version else f"{version_number} {release_type}"

            # Set the list of files to backup
            files_to_backup = ['UpdateCommands.py','UpdateProgram.py','quid.jpeg','app.py', 'count.py', 'custom_database.py','data.py','get_directory.py','files_to_backup.py','history_desc.py','patch_notes.txt','profanity.txt','requirements.txt','settings.py','shell.py','vars_to_save.py','version_config.py']

            # Ask if the save file should also be compressed
            compress_save_file = input('Would you like to compress the save file also: ')
            if compress_save_file.lower() in ["yes", "y"]:
                files_to_backup.append('data_save.py')

            # Backup the files
            with ZipFile(backup_name+'.zip', 'w') as zipObject:
                for file in files_to_backup:
                    try:
                        zipObject.write(file)
                    except FileNotFoundError:
                        print(f"Couldn't find: {file}")

        # Check if "-v" is in the command line arguments
        if "-v" in n:
            from settings import program_version
            print(f'Current Version: {program_version}')

        # Check if "-info" is in the command line arguments
        if "-info" in n:
            print('Created By Brandon Robinson.')
            print('GitHub: github.com/sukadateam')

        # Check if "-reset" is in the command line arguments
        if "-reset" in n:
            # Set the list of files to remove
            files_to_remove = ['version.pyc','directory.pyc','history_desc.pyc','count.py','data_save.py','version.py', 'directory.py','history.txt','hash_other.aes','hash.aes','hash_other.txt','hash.txt','settings.pyc','app.pyc','data.pyc']

            # Remove the files
            for file in files_to_remove:
                try:
                    os.remove(file)
                except FileNotFoundError:
                    print(f"{file} not found")

            # Clear the backup and history
            backup.clear_all()
            history.clear()

            # Remove the '__pycache__' directory
            try:
                shutil.rmtree('__pycache__')
            except FileNotFoundError:
                pass

            print('Exiting...')
    except Exception as e:
        print(f"An error occurred: {e}")
    
    if "-help" in n:
        print('Current Arguments:\n  -skipVersionCheck (Bypasses Application Version Check)\n  -v (Prints Progam Version)\n  -info (Prints Import Info)\n  -reset (Resets Application)\n  -skipPythonCheck (Ignore Python Version)')
    if dontCloseAfterEmptyStart==True:
        input('Hit enter to Continue: ')

    
    # To trick the system in thinking it's running on another os, systemDetectedOperatingSystem='your os'. windows, macos, linux
    #You may set a Normal level password
    # Getting Started! To create a global password to user security run: users.setBank3('your password') - Needs to run on every start up.
    #You can set a global password if need be. Basically a backup.
    # Write below to experiment!!
    #To trick the system in thinking it's running on another os, systemDetectedOperatingSystem='your os'. windows, macos, linux
    # Test bench
    #Test bench
    #<--Indent to here for setup.
