#!/usr/bin/env python3

"""
    there's sth about northpole
    computer have corrupt memory - our input
    Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
"""

"""
    search the list and look for only what we need - regex 
    then add them

    the matches come as a list of string.
"""
import re

def aoc3(file):
    try:
        with open(file, "r") as f:
            content = f.read()
            print(f"{file} has been read")
        
            input_string = content

            pattern =  r'mul\(\d+,\d+\)'
            # pattern = r'\d+'

            matches = re.findall(pattern, input_string)
            return matches

    except Exception as e:
        print(f"{e}")
        return -1
    finally:
        if file in locals():
            file.close()
            print(f"{file} has been closed")

def calc_mul(matches):
    sum_of_products = 0

    for match in matches:
        numbers = re.findall(r'\d+', match)
#        print(numbers)

        if len(numbers) == 2:
            a, b = map(int, numbers)
        sum_of_products += a * b
    return sum_of_products

def main():
    file = '3i.txt'

    matches = aoc3(file)
    sln = calc_mul(matches)
    print(sln)

if __name__ == "__main__":
    main()
