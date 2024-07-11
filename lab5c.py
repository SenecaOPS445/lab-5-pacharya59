#!/usr/bin/env python3

# Author_ID: pacharya9 (100706225)

def add(number1, number2):
    try:
        result = int(number1) + int(number2)
        return result
    except ValueError:
        return 'error: could not add numbers'

def read_file(filename):
    try:
        file = open(filename, 'r')
        lines = file.readlines()
        stripped_lines = [line.strip() + '\n' for line in lines]
        file.close()  # Closing the file after reading
        return stripped_lines
    except FileNotFoundError:
        return 'error: could not read file'

if __name__ == '__main__':
    print(add(10, 5))
    print(add('10', 5))
    print(add('abc', 5))
    print(read_file('seneca2.txt'))
    print(read_file('file10000.txt'))

