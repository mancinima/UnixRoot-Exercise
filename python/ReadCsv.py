import pandas as pd
import sys
import os
import ROOT
from tqdm import tqdm
import numpy as np
import argparse
import csv
from datetime import datetime

#create a function reading a CSV file
def read_csv(filename):
    try:
        df = pd.read_csv(filename)
        return df
    except IOError:
        print(f"Error: Failed to read the file '{filename}'. Retry!")
        return pd.DataFrame()

#create a function ordering by date (direct o inverted)
def sort_entries(df, reverse=False):
    try:
        df['Date of birth'] = pd.to_datetime(df['Date of birth'], dayfirst=True, errors='coerce')
        df.dropna(subset=['Date of birth'], inplace=True)
        sorted_df = df.sort_values(by='Date of birth', ascending=not reverse)
        return sorted_df
    except KeyError:
        print("Error: Invalid CSV format. Retry!")
        return pd.DataFrame()

#create a function printing names by the required order
def print_entries(df):
    if not df.empty:
        print(df)
    else:
        print("No entries to print.")

def main():
    parser = argparse.ArgumentParser(description='Sort and print CSV entries by "Date of birth"')
    parser.add_argument('filename', type=str, help='CSV file name')
    parser.add_argument('-r', '--reverse', action='store_true', help='Print entries in reverse order')
    args = parser.parse_args()

    df = read_csv(args.filename)
    sorted_df = sort_entries(df, args.reverse)
    print_entries(sorted_df)

if __name__ == '__main__':
    main()