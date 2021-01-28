import os
import glob
import sys

"""
This script will delete all empty files in the designated folder and subfolders.
Argument 1: folder path
"""

# Can pass in the path of the directory as an argument
if len(sys.argv) == 2:
    path = sys.argv[1]  
    files = glob.glob(path+'**/**.*',recursive=True)

# If not it will use the current directory
else:
    files = glob.glob('**/**.*',recursive=True)

for file in files:
    # Checks to see if the file size is zero
    if os.stat(file).st_size == 0:
        try:
            os.remove(file)
        except:
            continue
        print('Removed empty file: ',file)

print('Finished deleting all empty files!')