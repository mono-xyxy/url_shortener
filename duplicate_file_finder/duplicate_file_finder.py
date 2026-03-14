import os
import hashlib

print("Duplicate File Finder: ")

folder = input("Enter folder path: ")

hashes={}
duplicates=[]

for root ,dirs,files in os.walk(folder):
    for file in files:
        path = os.path.join(root,file)

        with open(path,"rb") as f:
            file_hash=hashlib.md5(f.read()).hexdigest()

        if file_hash in hashes:
            duplicates.append(path)
        else:
            hashes[file_hash]=path
    print("\nDuplicate Files Found:")

if duplicates:
    for file in duplicates:
        print(file)
else:
    print("\nDuplicate Files not  Found:")
