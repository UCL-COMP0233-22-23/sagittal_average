import subprocess


#must run this file in terminal
#these basically just let us run terminal commands when we run this python file from a terminal

subprocess.run(["ls", "-aF"], shell=True) #lists all files in current dir
subprocess.run(["ls", "-lh"], shell=True) #lists all files in current dir (in seperate linesw details)
subprocess.run(["echo", 'hello world'], shell=True) #prints hello world in the screen
subprocess.run(["date",  '+%Y%m%d'], shell=True) #prints today's date with the selected format
subprocess.run(["wc", "-l", "sagittal_brain.py"], shell=True) #counts the number of lines of the sagittal_brain.py file
subprocess.run(["wc", "-c", "AFileThatDoesNot.exist"], shell=True) #which should counts the number of characters, but should fail as the file doesn't exist