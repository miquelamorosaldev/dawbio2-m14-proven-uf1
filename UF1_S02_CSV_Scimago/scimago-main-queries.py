# Our imports
import file_utils
# 3rd party imports
import pprint 

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


# Main
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    
    entries: list[dict] = file_utils.read_csv_file(csv_file_path)
    # Test 
    # print(entries[0])

    num_entries: list[dict] = q1_num_entries(entries)
    print(f"There are {num_entries} entries.")
    
    first_entries: list[dict] = q2_first_entries(entries,30)
    # Prints the formatted representation of object followed by a newline. 
    pprint.pp(first_entries[0])
# -----------------------------------------------------------------------------