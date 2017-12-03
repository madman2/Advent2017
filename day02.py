"""Day 02: Corruption Checksum"""

import itertools

def main():
    """Prints out the answers for both stars in Day 02 of AoC 2017"""
    with open('day02.txt', 'r') as spreadsheet_file:
        spreadsheet = []
        for row in spreadsheet_file.readlines():
            spreadsheet.append(list(map(int, row.split())))
        first_star(spreadsheet)
        second_star(spreadsheet)

def compute_range(row):
    """Computes the differences between max(row) and min(row)"""
    return max(row) - min(row)

def compute_quotient(row):
    """Computes the quotient n2 / n1 where n1 is the only number
    in 'row' that evenly divides n2, where n2 is a different number in 'row'"""
    for pair in itertools.permutations(row, r=2):
        if pair[1] % pair[0] == 0:
            return int(pair[1] / pair[0])

def compute_checksum(spreadsheet, checksum_fun):
    """Computes the sum of checksum_fun(row) for each row
    in a given int[][] spreadsheet"""
    checksum = 0
    for row in spreadsheet:
        checksum += checksum_fun(row)
    return checksum

def first_star(spreadsheet):
    """Prints the solution for the first star"""
    checksum = compute_checksum(spreadsheet, compute_range)
    print("Star #1: {}".format(checksum))

def second_star(spreadsheet):
    """Prints the solution for the second star"""
    checksum = compute_checksum(spreadsheet, compute_quotient)
    print("Star #2: {}".format(checksum))

if __name__ == "__main__":
    main()
