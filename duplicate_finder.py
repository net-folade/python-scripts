'''
 Scans a folder (and its subfolders) and identifies duplicate files — not by filename, but by actual content.
'''

import os
import hashlib 

# set a folder path and a variable to read the files
directory_path = "" 

# function to compute the hash of a file using SHA-256 algorithm,
#  it reads the file in chunks to handle large files efficiently and returns the hexadecimal representation of the hash value.
#  If there is an error while computing the hash, it prints an error message and returns None.
def compute_hash(file_path):
    try:
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(8192)
                if not chunk: 
                    break
                hasher.update(chunk)
        return hasher.hexdigest()  
    except Exception as e:
        print(f"Error computing hash for {file_path}: {e}")
        return None
    

    # function to format the size of the file in a human-readable format
def format_size (bytes_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if bytes_size < 1024:
            return f"{bytes_size:.2f} {unit}"
        bytes_size /= 1024
    return f"{bytes_size:.2f} PB"
    
hash_group = {}

print(f"Scanning files...")

count = 0       # to count the number of files in the directory

# walk through the directory and compute the hash for each file, grouping them by their hash values
for parent_folder, subfolders, files in os.walk(directory_path):
    for file in files:
        fullpath = os.path.join(parent_folder, file) # get the full path of the file

        if file.startswith('.'): # skip hidden files
            continue

        file_hash = compute_hash(fullpath) # compute the hash of the file
        if file_hash is None:
            continue

        if file_hash in hash_group:         # group files by their hash values, if the hash already exists, append the file path to the list, otherwise create a new list with the file path
            hash_group[file_hash].append(fullpath)
        else:
            hash_group[file_hash] = [fullpath]

        count += 1
        #print(f"File: {fullpath}, Hash: {file_hash}") # print the file path and its hash

print (f"Found {count} files in the directory.")

# calculate wasted space 
wasted_space = 0
for file_hash, paths in hash_group.items():
    if len(paths) > 1:
        file_size = os.path.getsize(paths[0]) # get the size of one of the duplicate files
        group_waste = file_size * (len(paths) - 1) # calculate the wasted space for a group by multiplying the size of the file by the number of duplicates minus one
        wasted_space += group_waste
        print()
        print(f"Hash {file_hash} has {len(paths)} duplicates: {format_size(group_waste)} wasted")     # # print the duplicate files based on their hash values, if a hash has more than one file path, it means those files are duplicates

        for path in paths:
            print(f" - {path}")

print()
print(f"Total wasted space due to duplicates: {format_size(wasted_space)}")




