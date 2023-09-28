import scimago_main_queries
import file_utils

entries: list[dict] = file_utils.read_csv_file('scimago-medicine.csv')

expected_entries_q1: int = 7251

def test_q1_2022_7251():
    assert scimago_main_queries.q1_num_entries(entries) == expected_entries_q1

expected_entries_q3: int = 137

def test_q3_2022_spanish_entries():
    assert scimago_main_queries.q3_spanish_entries_v2(entries) == expected_entries_q3

expected_q2_input: int = 30
expected_q2_first: str = 'Ca-A Cancer Journal for Clinicians'
def test_q2_2022_first_entries():
    assert expected_q2_input == len(scimago_main_queries. \
        q2_first_entries(entries,expected_q2_input))
    assert expected_q2_first == scimago_main_queries. \
        q2_first_entries(entries,expected_q2_input)[0]['Title']


expected_result_q5: set[str] = \
    {'journal', 'book series', 'conference and proceedings', 'trade journal'}
def test_q5_2022_types():
    assert expected_result_q5 == set(scimago_main_queries. \
        q5_set_types_each_pub(entries))

# expected_result_q6: dict[str,int] = {'journal': 7082, 'book series': 27, 'conference and proceedings': 5, 'trade journal': 4}
expected_result_q6: dict[str,int] = {'journal': 7216, 'book series': 28, 'conference and proceedings': 5, 'trade journal': 4}
def test_q6_2022_num_types():
    assert expected_result_q6 == scimago_main_queries. \
        q6_number_types_each_pub(entries)
