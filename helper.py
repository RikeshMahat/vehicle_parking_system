from datetime import datetime
from time import strftime

def current_time():

    """

    :return: current time
    """
    return datetime.now()


def formatted_result(data):
    max_value_length = 0
    for i in data.values():
        i = i.copy()
        if 'wheel' in i:
            del i['wheel']
        current_max = len(max(list(i.values()), key=len))
        if max_value_length < current_max:
            max_value_length = current_max

    keys_list = [key for key in list(data.values())[0]]
    for key in keys_list:
        print(str.center(key, max_value_length), end='')

    print('\n')

    # Formatting and printing values
    for value in data.values():
        for i in range(0, len(keys_list)):
            val = str(value.get(list(keys_list)[i]))
            if len(val) < max_value_length:
                val = val.center(max_value_length)
            else:
                val = val.center(max_value_length+4)
            print(val, end='')
        print('')
