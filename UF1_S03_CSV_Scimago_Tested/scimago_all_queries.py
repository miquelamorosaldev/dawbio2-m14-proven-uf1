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


# -----------------------------------------------------------------------------
# Q5 - What types of scientific publications are in the file (paràmetre Type)? 
# -----------------------------------------------------------------------------
def q5_set_types_each_pub(entries: list[dict]) -> set[str]:
    '''Input: List of entries.
    Output: A set of types of scientific publications'''
    types_set: set = set()
    for entry in entries:
        types_set.add(entry['Type'])

    return types_set

# -----------------------------------------------------------------------------
# Q6 - Count the number of types of each scientific publication.
# -----------------------------------------------------------------------------
def q6_number_types_each_pub(entries: list[dict]) -> dict[str,int]:
    '''Input: List of entries.
    Output: A dict with the type (key) and number (value) of each scientific publication.'''
    num_entries_type = {}
    for entry in entries:
        # if Type don't exist, we add it in the dict.
        if (not (entry['Type'] in num_entries_type)):
            num_entries_type[entry['Type']]=1
        # if Type exist, we sum 1 more publication.
        else:
            num_entries_type[entry['Type']] = num_entries_type[entry['Type']] + 1

    return num_entries_type


# -----------------------------------------------------------------------------
# Q7 - Show all regions covered by all entries.
# -----------------------------------------------------------------------------
def q7_all_regions(entries: list[dict]) -> list[str]:
    '''Input: List of entries.
    Output: The list of regions covered by all entries.'''
# {'Northern America', 'Middle East', 'Western Europe', 'Asiatic Region', 'Pacific Region', 'Latin America', 'Eastern Europe', 'Africa/Middle East', 'Africa'}
    region_set:  set[str]  = {entry["Region"] for entry in entries}
    region_list: list[str] = sorted(region_set)
    return region_list

# -----------------------------------------------------------------------------
# Q8 - Mean of H-index by region.
# -----------------------------------------------------------------------------
def average(sum:int, len:int) -> float:
    '''Input: Sum of numbers list, length of numbers list 
    Output: Average number'''            
    return round(sum/len,4)

def q8_mean_hindex_each_region(entries: list[dict]) -> dict[str,int]:
    '''Input: List of entries.
    Output: A dict with the type (key) and number (value) of each scientific publication.'''
    dict_numentries_each_region = {}
    dict_hindex_each_region = {}
    # To calculate the average, first we need 
    # the sum of the H index of each region => dict_hindex_each_region
    # and the number of entries of each region => dict_numentries_each_region
    for entry in entries:
        # if H index from region don't exist, we add it in the dict.
        if (not (entry['Region'] in dict_numentries_each_region)):
            dict_numentries_each_region[entry['Region']] = 1
            dict_hindex_each_region[entry['Region']] = int(entry['H index'])
        # if H index from region exists, we sum it.
        else:
           dict_numentries_each_region[entry['Region']] = \
             dict_numentries_each_region[entry['Region']] + 1
           dict_hindex_each_region[entry['Region']] = \
             dict_hindex_each_region[entry['Region']] + int(entry['H index'])

    # print(dict_numentries_each_region)
    # print(dict_hindex_each_region)
    
    # Now, we can calculate the average getting the values
    # of two previous list
    list_regions = list(dict_hindex_each_region.keys())
    list_avg_hindex_each_region = \
        list(map(average,dict_hindex_each_region.values() \
            ,dict_numentries_each_region.values()))
    
    # Finally, we zip the two lists (region names and calculated 
    # in a dictionary as we want.
    dict_avg_hindex_each_region = dict(zip(list_regions,list_avg_hindex_each_region))
    
    return dict_avg_hindex_each_region


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

    # num_spanish_entries: list[dict] = q3_spanish_entries_v2(entries)
    # # # Prints the formatted representation of object followed by a newline. 
    # print(f"There are {num_spanish_entries} entries from Spain.")

    # q4_entries: list[dict] = q4(entries)
    # # # Prints the formatted representation of object followed by a newline.
    # print('Query 4 results: journals from UK with H index greater than 200, sorted reverse') 
    # print(q4_entries[0:4])
    # print('---')

    # q5_set_types: set[str] = q5_set_types_each_pub(entries)
    # #['journal', 'book series', 'conference and proceedings', 'trade journal']
    # print('Q5 - Types of scientific publications.')
    # print(q5_set_types)

    # q6_dict_types_number: dict[str,int] = q6_number_types_each_pub(entries)
    # # {'journal': 7082, 'book series': 27, 'conference and proceedings': 5, 'trade journal': 4}
    # print('Q6 - Number of types of each scientific publication.')
    # print(q6_dict_types_number)
    
    # q7_all_regions: list[str] = q7_all_regions(entries)
    # {'Northern America', 'Middle East', 'Western Europe', 'Asiatic Region', 'Pacific Region', 'Latin America', 'Eastern Europe', 'Africa/Middle East', 'Africa'}
    #print('Q7 - Show all regions covered by all entries.')
    #print(q7_all_regions)

    print('Q8 - Mean of H-index by region.')
    q8_mean_hindex_regions: list[str] = q8_mean_hindex_each_region(entries)
    print(q8_mean_hindex_regions)
# -----------------------------------------------------------------------------