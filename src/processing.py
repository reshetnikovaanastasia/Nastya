from typing import Iterable
import datetime

def filter_by_state(list_data_dictionaries: Iterable[list], state = 'EXECUTED') -> Iterable[list]:
    new_list_data=[]
    for data_dictionary in list_data_dictionaries:
        if data_dictionary['state'] == state:
            new_list_data.append(data_dictionary)
    return new_list_data
