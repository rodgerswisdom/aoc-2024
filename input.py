#!/usr/bin/env python3

import argparse
import requests

def get_aoc_input(day, filename, session_cookie):
    year = 2024
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    headers = {"Cookie": f"session={session_cookie}"}

    response = requests.get(url, headers=headers)

    if response.ok:
        with open(filename, "w") as file:
            file.write(response.text.strip())

            print(f"Input for day {day} stored in {filename}")
    else:
        print(f"Failed to fetch input for day {day}: {response.status_code} {response.reason}")


def main():
    parser = argparse.ArgumentParser(
                prog = "aoc input",
                description = "Fetch Advent of Code Input and save it to a file",
                epilog = "Help at the bottom"
            )

    parser.add_argument("day", type=int, help="The day of the puzzle (e.g., 1 for Day 1).")
    parser.add_argument("filename", type=str, help="The name of the file to store the input.")
    
    session_cookie = '53616c7465645f5fc266ab0abed6a9949f0f7b3f451f6ce879fc346fdac67fe93890edc39e076334c35764a274ac650a42f9f9a58b351e0f3efef276cf06ea3a'

    args = parser.parse_args()

    get_aoc_input(args.day, args.filename, session_cookie)

if __name__ == "__main__":
    main()
