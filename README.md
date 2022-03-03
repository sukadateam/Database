# Database
<br>Current Stage: Create a class to print and create barcodes.

To setup. Install all items in requirements.txt using pip and run custom_database.py. That's it!
<br>pip install -r requirements.txt
<br>python3 -m pip install -r requirements.txt

<br>Please note: Windows And MacOS are currently be used for application testing.
<br><br>Nerdy Stuff:<br>For the absolute latest version download the source code. Not in releases. May cause issues. It won't always be tested before updated. Do not do this if you are looking for a stable version.

<br>Latest Notes:<br>1. MacOS and Windows platforms are supported. MacOS is using a 4k display, Windows is for 1k display.
<br>2. Updates are being released in a slow pace at the moment. This application is nearly complete.

To start the program:
1. pip install -r requirements.txt (Universal) or python3 -m pip install -r requirements.txt (MacOS/UnAssigned)

2. Recommended python 3.10.2. if else: change required_version to your version in settings.py

3. Open Shell.py with python.

4. Enter 7, 1, 1. Now create a user. Use permission (admin).

5. Exit shell and open app.py and login. After login it will ask you to create a encrypt/decrypt password.


<br>To get live version(s) check out github.com/sukadateam/live_build

To use print_instructions.createBarcode() may need to do the following:
  (MacOS)
  1. Install Brew
  2. Run command "brew install pango"
  (Debian)
  1. Run command apt install libffi-dev

  (For More Info On this Part please head to):
    https://edinburgh-genome-foundry.github.io/blabel/
