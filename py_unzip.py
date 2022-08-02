#!/usr/bin/env python3

import os
import sys
import zipfile,fnmatch,glob


#Set Current direct as root

rootPath = r"."

# look for .zip files and unzip each into its own folder using name of support.zip

pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print(os.path.join(root, filename))
        extn = filename.split(".")
        # Check if the filename of the zip file exists in the list of directories. 
        if (extn[0] not in dirs):
            zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, os.path.splitext(filename)[0]))


