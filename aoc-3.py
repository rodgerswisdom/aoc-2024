#!/usr/bin/env python3

"""
    there's sth about northpole
    computer have corrupt memory - our input
    Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

"""
    search the list and look for only what we need - regex 
    then add them
"""
import re

def aoc3(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            print(f"{file} has been read")
        
            input_string = content

            pattern =  r'mul\(\d+,\d+\)'

            matches = re.findall(pattern, input_string)
            print(f"{len(matches)}")

    except Exception as e:
        print(f"{e}")
    finally:
        if file in locals():
            file.close()
            print(f"{file} has been closed")


def main():
    file = '3i.txt'

    aoc3(file)

if __name__ == "__main__":
    main()
