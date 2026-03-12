file = open(r"C:/Users/rohan/OneDrive/Desktop/dsa_study/log_file_parser/log.txt","r")

for line in file:
    if "ERROR" in line:
        print(line)