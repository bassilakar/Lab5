#!/usr/bin/env python3
# Author ID: Bakar

def read_file_string(file_name):

    f = open(file_name, 'r')
    content = f.read()
    f.close()
    return content

def read_file_list(file_name):

    f = open(file_name, 'r')
    lines = [line.strip() for line in f]
    f.close()
    return lines

def append_file_string(file_name, string_of_lines):

    f = open(file_name, 'a')
    f.write(string_of_lines)
    f.close()

def write_file_list(file_name, list_of_lines):

    f = open(file_name, 'w')
    for line in list_of_lines:
        f.write(line + '\n')
    f.close()

def copy_file_add_line_numbers(file_name_read, file_name_write):

    f_read = open(file_name_read, 'r')
    f_write = open(file_name_write, 'w')
    for line_number, line in enumerate(f_read, start=1):
        f_write.write(f"{line_number}:{line}")
    f_read.close()
    f_write.close()

if __name__ == '__main__':
    file1 = 'seneca1.txt'
    file2 = 'seneca2.txt'
    file3 = 'seneca3.txt'
    string1 = 'First Line\nSecond Line\nThird Line\n'
    list1 = ['Line 1', 'Line 2', 'Line 3']

    append_file_string(file1, string1)
    print(read_file_string(file1))

    write_file_list(file2, list1)
    print(read_file_string(file2))

    copy_file_add_line_numbers(file2, file3)
    print(read_file_string(file3))
