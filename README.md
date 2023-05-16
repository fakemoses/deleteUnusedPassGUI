# Delete Unused Pass GUI
A lazy solution to delete unwanted/extinct credential from my uname password lists. Delete credentials and save them as new file. 

## Usage

1. Export your password entries from Google Password Manager:
   - Go to Settings > Password manager > Export Passwords.
   - Save the exported file into the working folder.

2. Rename the input file:
   - Rename the exported file to your desired input file name.
   - Make sure the input file is in CSV format.

3. Set the output file name:
   - Optionally, you can set the desired output file name.

4. Run the software:
   - Execute the Python script to launch the CSV Data Processor.
   - The software will start from the beginning of your CSV upon each new session.

5. Process the entries:
   - The current name, URL, username, and password will be displayed on the screen.
   - To delete an entry, click the "Delete" button.
   - To keep an entry and skip to the next one, click the "Keep" button.
   - The software will save your progress automatically when you click the "Save" button.

## Requirements

- Python 3.x
- pandas library

## Notice

Project might not be updated so feel free to use this and expand the functionality. 

