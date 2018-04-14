#!/usr/bin/python3

def fun_read(file_name):
    with open(file_name, 'r') as f:
        read_line = f.readline()
        return read_line
