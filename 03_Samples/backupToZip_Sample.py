#! python3

# backupToZip_Sample.py is the sample for the future backup app that i will be working on

# It generates an autoincremental filename ZIP file.

# Importing libraries and frameworks

import os
import datetime
import shutil

# Defining global variables

zipFileName = None
folder = None
workingDir = None

# User parameters

print('Stablish your working directory')
workingDir = input()

print('Input the directory to zip')
folder = input()

# Program logic

    # Defining the new ZIP filename
zipFileName = datetime.datetime.now().strftime("%Y-%m-%d_%H%M%S")

    # Establishing the working directory
os.chdir(str(workingDir))

    # Creating the ZIP file
shutil.make_archive(str(zipFileName), 'zip', str(folder))