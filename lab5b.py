#!/usr/bin/env python3
# Author_ID: pacharya9 (100706225)

def read_file_string(file_name):
    f = open(file_name, 'r')
    file_contents = f.read()
    f.close()
    return file_contents

def read_file_list(file_name):
    f = open(file_name, 'r')
    lines_list = f.readlines()
    lines_list = [item.strip() for item in lines_list]
    f.close()
    return lines_list

def append_file_string(file_name, string_of_lines):
    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):
    f = open(file_name, 'w')
    for item in list_of_lines:
        f.write(item + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):
    f = open(file_name_read, 'r')
    list_of_lines = f.readlines()
    f.close()

    f = open(file_name_write, 'w')
    number_for_line = 1
    for item in list_of_lines:
        formatted_line = str(number_for_line) + ':' + item.strip()
        f.write(formatted_line + '\n')
        number_for_line += 1
    f.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line \n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))


