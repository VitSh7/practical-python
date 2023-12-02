# fileparse.py
#
# Exercise 3.3

import csv
import sys

print(sys.path)


def parse_csv(filename, select=None, types=None, has_headers=True, delimiter=',', silence_errors=False):
    """
    Parse a CSV file into a list of records
    """
    if select is None:
        select = ['name', 'shares', 'price']
    with open(filename) as f:
        rows = csv.reader(f, delimiter=delimiter)

        # Read the file headers
        indices = []
        if has_headers:
            headers = next(rows)
            if select:
                indices = [headers.index(h) for h in headers if h in select]
                headers = select

        records = []
        for n, row in enumerate(rows):
            if not row:    # Skip rows with no data
                continue
            try:
                if indices:
                    row = [row[i] for i in indices]

                if types:
                    row = [func(item) for func, item in zip(types,row)]

                if has_headers:
                    record = dict(zip(headers, row))
                else:
                    record = tuple(row)
                records.append(record)
            except ValueError as e:
                if not silence_errors:
                    print(f"Row {n}: ", e)

    return records


#portfolio = parse_csv('Work/Data/missing.csv', types=[str, int, float],  silence_errors=True)
#print(portfolio)