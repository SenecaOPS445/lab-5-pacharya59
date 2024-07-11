#!/usr/bin/env python3
# Author_ID: pacharya9 (100706225)

# Open the data.txt file in read mode.
f = open('data.txt', 'r')

# This function reads and returns the entire content of the specified file.
def read_file_string(file_name):
    file_contents = f.read()
    f.close()  # Close the file after reading.
    return file_contents

# This function reads the file and returns a list of its lines, with newline characters removed.
def read_file_list(file_name):
    f = open('data.txt', 'r')
    lines_list = f.readlines()
    lines_list = [item.strip() for item in lines_list]  # Removeing newline characters from each line.
    f.close()
    return lines_list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))  # Printing the full content of the file.
    print(read_file_list(file_name))    # Printing the list of lines from the file.

