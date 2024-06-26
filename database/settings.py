'''Used for custom_database.py. This file contains all the settings needed to run the program.
\nCurrently only the user can modify this file, as custom_database has not yet been programmed how to.
\nFeature Will be coming in the future. Experimental functions have been written to try and edit this file but leads to curruption or file deletion as of now.'''
#END **


#    ------------------------------------------------------------------------------------------------    #
# --| ( New Settings. These settings haven't been fully implemented for it's specific function(s)  ) |-- #
#    ------------------------------------------------------------------------------------------------    #
testExpermintalFeatures=False # Runs parts of the program that have issues and are in developement

bannedEntries=['\n','\t','\r', '#(!(h<|>h)!)#'] # Entries that are not allowed to be entered into a database.

disableUserEncryption=True # Disables the encryption for the user. Only use if you know what your doing.
'''Only disables encryption for new users. Older users that already have encryption will still have it. A function will be added in the future to remove encryption from all users.'''

# Settings For Forcing Compdability with older Database Handler. Set all to true if using older handler.
forceNormalSaveOeprations=True # Default False. Ingores saving of memory_bank6. Setting only added to allow forced support for the older database handler.


ShowCredentials=False # Shows Credentials when failed. Only to be used to debug issues with encryption. Security Issue if left True. 
#ShowCrendtials may be removed from this file if you want. I would recommend if your big on security.

ShowDebugInfo=False # Similar to ShowCredentials but limits it to not showing important security passwords unless above is set True.
                   #--Show debugging data for newly build functions. May be removed in the future.

DdosPreventionTimerEnabler=True # Enables ddos Prevention
DdosPreventionTimer=2 # The amount of time that must pass before another hash check can be done. If done to frequently then curroption will occur.

#Instead of loading the normal save file(s), you can now import any other Compadaible save file. Checks will be done to ensure working save file(comes at a later version. Not yet implemented.)
modifiedSafeFile=False

#Used to set max password lengths for student accounts. Default is 10
studentPasswordLength=10

# Currently testing encryption methods. Info related to tests will be released soon!
pyAesCryptMethod=False
ChaCha20Method=True

#UnverifiedHashDetection - If a hash is not verified, then the system will not allow the user to continue. It will beggin wiping the system.
DisableHashVerifacation=True # Default False. Added since hash verifaction isn't fully developed and has issues. Bypass.
UnverifiedHashDetection=False
AllowedAttempsBeforewipe=3 #How many attemps are allowed before the system is wiped. Counter is reset after a successful login.

'''Values: \n - admin\n - teacher'''
# -- END OF NEW SETTINGS


#User Settings --(FOR USERS)--

#Required python version to run program/Tested versions. You can try others if u want.
required_version=['3.10.0','3.10.1','3.10.2','3.10.3','3.10.4', "3.11.7"]
#Application version. Just for show.
program_version='0.9.3'
#Drive letter to store hash.aes file on root directory. Letter must be Uppercase. Windows only.
drive_letter='E'
#Drive name to store hash.aes file on root directory. Linux only. Setting is not required to be changed.
drive_name='Computer'
#Operating System or OS. Can be macos, windows or linux. Must be lowercase.
system='macos'
#Only allow set operating system. Change system variable to your choice.
set_operating_system=False
#Allowed windows versions. You can choose 7, 8, 10, 11. Only works if system setting is set to windows.
allow_windows_version='10'

#Filters bad words that people should not be using.
profanity_filter=True
#A backup password in case the other is forgotten.
global_password=True

#App version control --(Disable if needed)--
app_version_control=True

#min and max password lengths, and allowed characters
min_length=5 #Cannot be smaller than 5
max_length=25 #Cannot be bigger than 99
allowedPassword_chars='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890*()# '

#used for StudentManager.AllowedPermissions() - Users with these permissions are allowed to modify student accounts.
studentModifierPermissions=['admin', 'teacher']
#What is the name of your printer? For macOS. Windows uses default.
printer_name='iDPRT_SP310' #My prefered printer for labels and printing squidwards.







#Developer Settings --(NOT USER SETTINGS!)-- Developer Settings


#Skip python check.
skip_pythonCheck=False
#Enable automated history_file for functions
auto_history_record=True
#Don't load save file. True: Skip save file -- False: Load defualt file not save file.
dont_load_save=False
#Automatically optimize on start up. USE AT YOUR OWN RISK. Currently in development phase.
optimize_on_startup=False
#If a prior task is equal to the current task, system will then ignore the task given.
skip_history_copy=True
#Enable automated history_file for functions. 
auto_error_record=True
#Quit app if one or more settings are incorrect. For safety purposes do not disable.
quit_ifIncorrect=False
#Record a more informed description of a item in history.txt
advanced_history=True
#Automatically check inputs for profanity. May use more CPU power than normal.
auto_filter_profanity=True
#Attempt to speed up the search on inputs by using a smaller version of profanity.txt. Only works if auto_filter_profanity is set to True.
auto_filter_profanity_speedBoost=False
#An attempt to use more than one cpu core. #Currently Not Functional.
multi_process=False
#Assign Digit number to history item for a more depth look into the item. And create a database to handle all the data for each assigned item.
assign_digit_forHistory=True
#How many digits are allowed to be used to store history. Max 30.
allowed_digists_forHistory=8
#Will still check for incorrect settings if quit_ifIncorrect is True, but won't display anything.
show_incorrect_settings=True
#Will deny the program from saving. No matter what. Will cause problems for long term.
disable_save=False
#Passwords have to meet the requirments set above.
strict_password=True
#If True system will not remove files after encrypt and decrypt. Will remove files if set to False.
do_not_remove=True
#Do not disable failsafe unless needed! Trust me. Don't disable it.
fail_safe=True
#Disable profanity filter for admin.
disable_filter_admin=False
#Prevents to many backups from being stored.
retain_backup_time=25 # Only (retain_backup_time) backups will be kept. If a new backup occurs, the oldest backup will be removed.
#Clear collections folder on app startup.
resetCollections=True
#If a setting is missing, not present, or not there, skip it.
skip_missing_settings=True
#Backups goes in order of numbers and this var changes where it starts. Only works on first backup.
backup_startNumber=1
#Allowed permissions to create, remove, edit backups.
#User must be signed in to create a backup.
allowed_backupPermissions=['admin','teacher']
#Setup backup response. Do not disable if using backup. Used for debugging.
setup_backup_response=True
#If custom_database.py is not started from an import. Do not close it.
dontCloseAfterEmptyStart=False
#If True, Encrypt Important files with given password. Else: Backup with no password.
encryptBackups=False
#Keep the terminal hush hush on startup. Only major errors will show.
quiteStartup=False
#Print in the terminal if prints fail and what printer it is using.
printer_debug=True #Default True
#Clears history file after each startup.
clearHistoryOnStartup=False
#Settings coming soon. Do not change unless your a dare devil.
#DarkMode For app.py.
darkModeApp=True
#Gives the app some color. darkModeApp and colorMode cannot be set to True at the same time.
colorMode=False
#Speeds up computation. May Not ever be fully functional :(
UtilizeCPPCode=False # Default False. Not in use yet, or maybe ever.
#Limits the amount of characters in a given string when writen to a text file.
Output_file_MaxLength=35
#IDk
allowed_digits_forHistory = 15 # Max 30, Min 1, Default 15.


#Remove if you aren't using my custom application.
#Settings for application.
show_background=True
button_color='white'
option_color='white'
bg_color='#80a8e8'
text_color='#000000'
button_height=2
button_width=15
text_font=30
entry_background_color='White'
entry_text_color='Black'
OnlyAllowKnownStudents=False
secretsAllowed=False
side_tilt=200
AskForEncryptionPassword=False
if colorMode==True:
    bg_color='red'
    text_color='blue'
    button_color="orange"
    option_color='green'
if darkModeApp==True:
    bg_color='#231F20'
    text_color='#000000'
    button_color="grey"
    option_color='white'
