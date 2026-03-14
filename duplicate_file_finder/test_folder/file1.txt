## How to Test Duplicate File Finder

To test the program, create a folder with some duplicate files.

### Example

1. Create a folder:

```
test_folder
```

2. Add files like this:

```
test_folder
│
├── file1.txt
├── file2.txt
├── copy_file1.txt
```

3. Make sure `file1.txt` and `copy_file1.txt` have the **same content**.

Example content:

```
Hello world
```

4. Run the program:

```
python duplicate_file_finder.py
```

5. Enter the folder path:

```
Enter folder path: test_folder
```

### Output

The program will display duplicate files:

```
Duplicate Files Found:
test_folder\copy_file1.txt
```
