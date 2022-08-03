#!/usr/bin/env python3

import os
import sys
import zipfile,fnmatch,glob

def listToString(extn): 
    
    # initialize an empty string
    str1 = "" 
    
    # return string  
    return (str1.join(extn))

#Set Current direct as root

rootPath = r"."

# look for .zip files and unzip each into its own folder using name of support.zip

pattern = '*.zip'
for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print("Currently extracting:", os.path.join(root, filename))
        extn = filename.split(".")
        extn_1 = listToString(extn[0])
        extn_type = extn_1 + "_zip"
        # Check if the filename of the zip file exists in the list of directories. 
        if (extn_type not in dirs):
            zipfile.ZipFile(os.path.join(root, filename)).extractall(os.path.join(root, extn_type))
        else:
            print("\nExtraction failed. Error: Directory",extn_type,"already exists.")

