#Do not make any vars equal numbers. True or False are fine and "" are fine.

#If True system will not remove files after encrypt and decrypt. Will remove files if set to False.
do_not_remove=False
#Do not disable failsafe unless needed! Trust me. Don't disable it.
fail_safe=True
#Required python version to run program.
required_version='3.10.1'
#Application version. Just for show.
program_version='0.2.5'
#Drive letter to store hash.aes file on root directory. Letter must be Uppercase. Windows only.
drive_letter='E'
#Drive name to store hash.aes file on root directory. Linux only.
drive_name='Computer'
#Operating System or OS. Can be macos, windows or linux. Must be lowercase.
system='windows'
#Filters bad words that people should not be using. USE AT YOUR OWN RISK. Currently in development phase.
profanity_filter=False
#Disable profanity filter for admin.
disable_filter_admin=False
#A backup password in case the other is forgotten.
global_password=True
#Don't load save file. True: Skip save file -- False: Load defualt file not save file.
dont_load_save=False
#Automatically optimize on start up. USE AT YOUR OWN RISK. Currently in development phase.
optimize_on_startup=False
#Enable automated history_file
auto_history_record=True
#App version control --(Disable if needed)--
app_version_control=True
#Only allow set operating system. Change system variable to your choice. USE AT YOUR OWN RISK. Currently in development phase.
set_operating_system=True
#Allowed windows versions. You can choose 7, 8, 10, 11. Only works if system setting is set to windows.
allow_windows_version='10'




#Settings coming soon
#If a record prior what's asked is a duplicate, system will then ignore the task given.
skip_history_copy=False
