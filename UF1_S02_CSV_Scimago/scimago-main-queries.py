# Our imports
import file_utils
# 3rd party imports
import pprint 
from operator import itemgetter

# File name and path.
csv_file_path: str = "scimago-medicine.csv"   

# -----------------------------------------------------------------------------
# Q1. How many entries are in scimago-medicine.csv?
# -----------------------------------------------------------------------------
def q1_num_entries(entries: list[dict]) -> int:
    '''Input: List of entries
    Output: The number of entries.'''
    num: int = len(entries)
    #print("First entry:")
    #pprint.pp(entries[0])
    return num

# -----------------------------------------------------------------------------
# Q2. Show the n first entries.
# -----------------------------------------------------------------------------
def q2_first_entries(entries: list[dict], num_first_entries: int) -> list[dict]:
    '''Input: List of entries, number of first items.
    Output: The number of first entries defined in num_first_entries.'''
    return entries[0:num_first_entries]

# -----------------------------------------------------------------------------
# Q3 - How many entries are from Spain? (Country = Spain)
# -----------------------------------------------------------------------------
def q3_spanish_entries(entries: list[dict]) -> int:
    '''Input: List of entries, number of first items.
    Output: The number of Spanish entries.'''
    numEntriesSpain: int = 0
    for entry in entries:
        if(entry['Country'] == 'Spain'):
            numEntriesSpain+=1

    return numEntriesSpain

#Solució 32, funcional.
def filterEntrySpain (entry:dict) -> bool:
    '''Input: List of entries.
    Output: True if the country of entry is Spain.'''      
    return entry['Country'] == 'Spain'

def q3_spanish_entries_v2(entries: list[dict]) -> int:
    '''Input: List of entries, number of first items.
    Output: The number of Spanish entries.'''
    return len(list(filter(filterEntrySpain,entries)))

# -----------------------------------------------------------------------------
# Q4 - Show all the journals (Type = journal) published in UK 
# (Country = United Kingdom) with an H-Index greater than 200, 
# sorted by H-index (biggest H-Index first)
# -----------------------------------------------------------------------------
def q4(entries: list[dict]) -> list[dict]:
    '''Input: List of entries.
    Output: The number of .'''
    filtered_entries: list[dict] = list(filter(filterUKJournalHIndex200,entries))
    filtered_sorted_entries = sorted(filtered_entries, key=itemgetter('H index'),reverse=True)
    return filtered_sorted_entries

def filterUKJournalHIndex200(entry:dict) -> bool:
    '''Input: List of entries.
    Output: True if the country is UK, type journal, H-Index greater than 200.'''            
    return entry['Country'] == 'United Kingdom' and entry['Type'] == 'journal' \
        and int(entry['H index']) > 200                          


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    entries: list[dict] = file_utils.read_csv_file(csv_file_path)
    # Test 
    # print(entries[0])

    # num_entries: list[dict] = q1_num_entries(entries)
    # print(f"There are {num_entries} entries.")
    
    # first_entries: list[dict] = q2_first_entries(entries,30)
    # # Prints the formatted representation of object followed by a newline. 
    # pprint.pp(first_entries[0])

    num_spanish_entries: list[dict] = q3_spanish_entries_v2(entries)
    # # Prints the formatted representation of object followed by a newline. 
    print(f"There are {num_spanish_entries} entries from Spain.")

    q4_entries: list[dict] = q4(entries)
    # # Prints the formatted representation of object followed by a newline.
    print('Query 4 results: journals from UK with H index greater than 200, sorted reverse') 
    print(q4_entries[0:4])
    print('---')
# -----------------------------------------------------------------------------