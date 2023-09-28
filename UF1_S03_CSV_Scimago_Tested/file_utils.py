# Imports
import csv

def read_csv_file(csv_file_path: str) -> list[dict]:
    '''Input:  The file contents as a single string.
      Output: A list of strings where each string is a row of the csv file.'''
    
    with open(csv_file_path, 'r', newline='', encoding='utf-8') as csv_file:
        # DictReader converts each row in csv_file in a dictionary.
        # The dictionary keys are the column names.
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        result     = [row_dict for row_dict in csv_reader]

    return result