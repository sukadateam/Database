#If True system will not remove files after encrypt and decrypt. Will remove files if set to False.
do_not_remove=False
#Do not disable failsafe unless needed! Trust me. Don't disable it.
fail_safe=True
#Required python version to run program.
required_version='3.10.1'
#Application version. Just for show.
program_version='0.2.4'
#Drive letter to store hash.aes file on root directory. Letter must be Uppercase. Windows only.
drive_letter='E'
#Drive name to store hash.aes file on root directory. Linux only.
drive_name='Computer'
#Operating System or OS. Can be windows or linux. Must be lowercase.
system='windows'
#Filters bad words that people should not be using. USE AT YOUR OWN RISK. Currently in development phase.
profanity_filter=False
#Disable profanity filter for admin. USE AT YOUR OWN RISK. Currently in development phase.
disable_filter_admin=False
#A backup password in case the other is forgotten.
global_password=True
#Don't load save file. True: Skip save file -- False: Load defualt file not save file. USE AT YOUR OWN RISK. Currently in development phase.
dont_load_save=False
#Automatically optimize on start up. USE AT YOUR OWN RISK. Currently in development phase.
optimize_on_startup=False
